#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

uint32_t increment(uint32_t x)
{
    x++;
    return x;
}

uint64_t square(int32_t x)
{
    return x*x;
}

void printNumber(int32_t x)
{
    printf("%d\n", x);
}

int main()
{
    printf("%lu\n", square(3));
    printNumber(1642);
    printNumber(-20);

    uint32_t x = 0;
    uint32_t y = 0;

    increment(x);
    y = increment(y);
    printf("%d %d\n", x, y);

}
