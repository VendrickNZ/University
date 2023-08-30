#include <pthread.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>
#include <assert.h>

int has_run[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

void runMe(int *arg) {
  int value = (*arg);
  assert(value >= 0 && value < 5 && "Bad argument passed to 'runMe()!'");
  
  has_run[value] = 1;
  
  int *ret = (int*)malloc(sizeof(int));
  *ret = value * value; 

  pthread_exit((void*)ret);
}
/**
 * 1) Spawn n threads which call runMe which pass in a pointer to int (int*) pointing to consecutive values from (0 to n - 1)

    2) Wait for all threads to finish and collect the exit codes (another int* cast to void*)
    3) Return the sum of the exit codes from run_threads() 

    Note - check the documentation for pthread_exit and pthread_join very carefully for clues how to get the return value.

    Before submission check your answers carefully. Use 'valgrind' to check for memory problems. 
    In your submission, don't print anything to stdout.

**/
int run_threads(int n) {
    pthread_t threads[n];
    int address[n];
    void* dummy;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        address[i] = i;
        pthread_create(&threads[i], NULL, (void* (*)(void*))runMe, (void*)&address[i]);
    }

    for (int i = 0; i < n; ++i) {
        pthread_join(threads[i], &dummy);
        int *exitCode = (int*)dummy;
        sum += *exitCode;
        free(exitCode);
    }
    return sum;
}

int main (int argc, char **argv) { 
  
  int sum = run_threads(5);

  int correct = 0;
  for(int i = 0; i < 5; ++i) {
    if(has_run[i]) correct++;
  }

  printf("%d %d", correct, sum);

  return 0;
}

void set_data()
{
    printf("Setting data\t");
    /* use: global_data = rand(); */
    // my code below this
    pthread_mutex_lock(&mutex1); // locks the mutex, entering critical region
    global_data = rand(); // randomizing the global
    pthread_mutex_unlock(&mutex1); // unlocks the mutex, exiting critical region
    // my code above this
}

void read_data()
{
    int data; // the data to read
    //my code below this
    pthread_mutex_lock(&mutex1); // locks the mutex, entering critical region
    data = global_data; // setting the local data to the global_data
    printf("Data: %d\n", data);
    pthread_mutex_unlock(&mutex1); // unlocks the mutex, entering critical region
    //my code above this


}