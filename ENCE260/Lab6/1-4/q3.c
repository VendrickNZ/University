#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


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
    int16_t* data = ramp(5);
    for (size_t i = 0; i < 5; i++) {
        printf("%d ", data[i]);
    }
    free(data);
}