#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>
#include <pthread.h>

#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif

typedef double MathFunc_t(double);
void waitChild();

double gaussian(double x)
{
	return exp(-(x*x)/2) / (sqrt(2 * M_PI));
}

double chargeDecay(double x)
{
	if (x < 0) {
		return 0;
	} else if (x < 1) {
		return 1 - exp(-5*x);
	} else {
		return exp(-(x-1));
	}
}

#define NUM_THREADS 4
#define MAX_CHILDREN 6
#define NUM_FUNCS 3
static MathFunc_t* const FUNCS[NUM_FUNCS] = {&sin, &gaussian, &chargeDecay};
static int numChildren = 0;
pthread_mutex_t numChildrenMutex = PTHREAD_MUTEX_INITIALIZER;

struct threadArgs {
    MathFunc_t* func;
    double rangeStart;
    double rangeEnd;
    size_t numSteps;
    double *totalSum;
    pthread_mutex_t *mutex;
};

void waitChild() {
    int status;
    while ((wait(&status) > 0) && numChildren > 0) {
        pthread_mutex_lock(&numChildrenMutex);
        if (numChildren > 0) {
            numChildren--;
        }
        pthread_mutex_unlock(&numChildrenMutex);
    }
}

//Integrate using the trapezoid method. 
void* integrateTrap(void* args)
{
    struct threadArgs* thread_args = (struct threadArgs*) args;
    double rangeSize = thread_args->rangeEnd - thread_args->rangeStart;
    double dx = rangeSize / thread_args->numSteps;

    double area = 0;
    for (size_t i = 0; i < thread_args->numSteps; i++) {
        double smallx = thread_args->rangeStart + i*dx;
        double bigx = thread_args->rangeStart + (i+1)*dx;

        area += ( thread_args->func(smallx) + thread_args->func(bigx) ); 
    }
    // race condition prevention of a shared variable
    pthread_mutex_lock(&numChildrenMutex);
    *(thread_args->totalSum) += (area * 0.5 * dx);
    pthread_mutex_unlock(&numChildrenMutex);

    return NULL;
}

double handleIntegration(MathFunc_t* func, double rangeStart, double rangeEnd, size_t numSteps) {
    double totalSum = 0;
    pthread_t threads[NUM_THREADS];
    struct threadArgs thread_args[NUM_THREADS];
    pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

    double totalRange = rangeEnd - rangeStart;
    double dx = totalRange / numSteps;

    // checking if there are less threads than numSteps
    size_t activeThreads = (numSteps < NUM_THREADS) ? numSteps : NUM_THREADS; 
    size_t stepsPerThread = numSteps / NUM_THREADS;
    size_t remainderSteps = numSteps % NUM_THREADS;

    double currentStart = rangeStart;
    for (int i = 0; i < activeThreads; ++i) {
        size_t stepsThisThread = stepsPerThread;

        if (i < remainderSteps) {
            stepsThisThread++;
        }
        double currentEnd = currentStart + stepsThisThread * dx;
        thread_args[i].func = func;
        thread_args[i].rangeStart = currentStart;
        thread_args[i].rangeEnd = currentEnd;
        thread_args[i].numSteps = stepsThisThread;
        thread_args[i].totalSum = &totalSum;
        thread_args[i].mutex = &mutex;
        
        pthread_create(&threads[i], NULL, integrateTrap, &thread_args[i]);
        currentStart = currentEnd;
    }
    for (int i = 0; i < activeThreads; ++i) {
        pthread_join(threads[i], NULL);
    }
    pthread_mutex_destroy(&mutex);
    return totalSum;
}

bool getValidInput(double* start, double* end, size_t* numSteps, size_t* funcId)
{
	//Read input numbers and place them in the given addresses:
	size_t numRead = scanf("%lf %lf %zu %zu", start, end, numSteps, funcId);

	//Return whether the given range is valid:
	return (numRead == 4 && *end >= *start && *numSteps > 0 && *funcId < NUM_FUNCS);
}

int main(void) {
    double rangeStart;
    double rangeEnd;
    size_t numSteps;
    size_t funcId;
    pid_t child_pid;

    signal(SIGCHLD, &waitChild);
    while (getValidInput(&rangeStart, &rangeEnd, &numSteps, &funcId)) {
        // locking shared variable
        pthread_mutex_lock(&numChildrenMutex);
        numChildren++;
        pthread_mutex_unlock(&numChildrenMutex);

        if ((child_pid = fork()) < 0) {
            perror("fork");
            exit(1);
        }
        // In a child process
        else if (child_pid == 0) {
            fclose(stdin);
            double totalSum = handleIntegration(FUNCS[funcId], rangeStart, rangeEnd, numSteps);
            printf("The integral of function %zu in range %g to %g is %.10g\n", funcId, rangeStart, rangeEnd, totalSum);
            exit(0);
        }

        // In the parent process
        else {
            while (numChildren >= MAX_CHILDREN) {
                wait(NULL);
                pthread_mutex_lock(&numChildrenMutex);
                numChildren--;
                pthread_mutex_unlock(&numChildrenMutex);
            }
        }
    }
    // waits for all the children to finish before proceeding
    while (wait(NULL) > 0) {} 
    return EXIT_SUCCESS;
}