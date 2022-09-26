#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

typedef struct {
    bool isNegative;
    uint16_t magnitude;
} SignMag_t;

SignMag_t signMax_init(bool isNegative, uint16_t magnitude)
{
    SignMag_t init = {isNegative, magnitude};
    return init;
}

void signMag_print(SignMag_t value)
{
    if (value.isNegative == true) {
        printf("-%d", value.magnitude);
    } else {
        printf("%d", value.magnitude);
    }
}

int main(void)
{
    SignMag_t monkey = {false, 200};
    signMag_print(monkey);
}