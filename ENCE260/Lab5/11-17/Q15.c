#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>


void processBuffer(void* buffer, size_t numElements, size_t elementSize, void (*processFunc)(void*))
{
    for (size_t i; i < (numElements * elementSize); i += elementSize) {
        processFunc(&buffer[i]);
    }
}


void processU64(void* element)
{
    printf("%I64u\n", *(uint64_t*)element);
}


int main (void)
{
    uint64_t arr[11] = {0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};
    processBuffer((void*)arr, 11, sizeof(uint64_t), &processU64);
}