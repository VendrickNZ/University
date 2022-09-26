#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


int main(void)
{
    uint64_t* i = malloc(sizeof(int64_t));
    scanf("%I64d", i);
    printf("%I64d", *i);
    
    free(i);

    return 0;
}