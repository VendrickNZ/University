#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

typedef struct {
    int32_t* (*func)(int32_t*, size_t);
} Func_t;


//Define a type Func_t which is a pointer to a function that takes an int32_t* and a size_t and returns an int32_t*.



int32_t* offsetArray(int32_t* array, size_t offset){
    return array + offset;
}

int main(void)
{
    Func_t func = &offsetArray;
    
    int32_t arr[5] = {1, 2, 3, 4, 5};
    int32_t* offsetArr = (*func)(arr, 2);
    printf("%I64d\n", offsetArr - arr);
}