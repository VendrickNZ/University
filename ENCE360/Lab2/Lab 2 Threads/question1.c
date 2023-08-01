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
void* runMeAdapter(void *arg) {
  runMe((int *)arg);
  return NULL;
}

int run_threads(int n) {
    /* spawn n threads which call runMe which 
    pass in a pointer to int pointing to consecutive values from 0 to n-1*/
    pthread_t threads[n];
    int address[n];
    void* dummy;
    int sum = 0;

    for (int i = 0; i < n; ++i)
    {
      address[i] = i;
      pthread_create(&threads[i], NULL, (void* (*)(void*))runMe, (void*)&address[i]);
    }



    // wait for all threads to finish then collect exit codes
    for (int i = 0; i < n; ++i)
    {
        pthread_join(threads[i], &dummy);
        int *exitCode = (int*)dummy;
        sum += *exitCode;
        free(exitCode);
    }
    return sum;
    // return sum of exit codes from run_threads()
}

int main (int argc, char **argv) { 
  
  int sum = run_threads(5);

  int correct = 0;
  for(int i = 0; i < 5; ++i) {
    if(has_run[i]) correct++;
  }

  return 0;
}