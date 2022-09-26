/* First C program */

#include <stdio.h>
#include <stdint.h>

int main(void)
{
    // The declarations
    int32_t number1;
    int32_t number2;
    int32_t total;
    int32_t n = 60000;
    int32_t number = 10;
    int32_t result = 0;

    // Some code
    number1 = 10;
    number2 = 20;
    total = number1 + number2;
    printf("The sum of %d and %d is %d\n", number1, number2, total);
    printf("%d\n", n * 60000);
    result = 5 * number--;
    printf("%d\n", result);


    return 0;
}