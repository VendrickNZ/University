#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

typedef struct {
    bool isNegative;
    uint16_t magnitude;
} SignMag_t;

int main(void)
{
    SignMag_t val1 = {false, 15};
    printf("%s%hu\n", val1.isNegative ? "-" : "+", val1.magnitude);
}