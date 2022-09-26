#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main()
{
    size_t objSize;

    objSize = sizeof(float);
    printf("The object size is %zu bytes\n", objSize);
}
