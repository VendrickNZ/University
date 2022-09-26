#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define FREEZING_PT 32
#define SCALE_FACTOR (5 / 9)
#define THING 4 + 2

int main(void)
{   
    int32_t fahrenheit = 50;
    int32_t celsius = 0;
    int silly = THING * THING;

    celsius = (fahrenheit - FREEZING_PT) * SCALE_FACTOR;

    printf("%d degrees Fahrenheit is equivalent to %d degrees Celsius\n", fahrenheit, celsius);
    printf("Hello ENCE260!\n");
    printf("%d", silly);

    return EXIT_SUCCESS;
}