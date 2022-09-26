#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


void fillRamp(int16_t* data, size_t n)
{   
    for (size_t i = 0; i < n; i++)  {
        data[i] = (i + 1);
    }
}

int16_t* ramp(size_t n)
{
    int16_t *array = calloc(n, sizeof(int16_t));
    for (size_t i = 0; i < n; i++)  {
        array[i] = (i + 1);
    }
    return array;
}

int main(void)
{
    int16_t* data = calloc(4, sizeof(int16_t));
    fillRamp(data, 4);
    for (size_t i = 0; i < 4; i++) {
        printf("data[%I64u] = %d\n", i, data[i]);
    }
    free(data);
}