#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

void printData(int argc, char** argv)
{
    for (size_t i=0; i < argc; i++) {
        printf("[%I64u] %s\n", i, argv[i]);  
    }
}


int main(int argc, char** argv)
{
    printData(argc, argv);
}
