#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>



void printSquares(uint32_t n)
{
    for (uint32_t i = 1; i <= n; i++)    {
        printf("%d\n", i * i);
    }
}

int main(void)
{
    printSquares(4);

}