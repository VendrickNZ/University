#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

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

SignMag_t signMag_read(void)
{
    SignMag_t instance;
    instance.isNegative = false;
    char c[127];
    uint16_t i = 1;
    uint16_t chr;
    chr = getchar();
    if (chr == '-') {
        i--;
        instance.isNegative = true;
    }
    if (!(isdigit(chr) || chr == '-' || chr == '+')) {
        instance.magnitude = 0;
        instance.isNegative = true;
        return instance;
    }
    c[0] = chr;
    while (isdigit(chr) != 0 || chr == '-' || chr == '+'|| i <= sizeof(chr) - 1) {
        chr = getchar();
        c[i] = chr;
        i++;
    }
    instance.magnitude = atoi(c);
    if (atoi(c) >= 65535) {
        instance.magnitude = 65535;
    }
    return instance;
}


int main(void)
{
    SignMag_t val = signMag_read();
    printf("%s%hu ", val.isNegative ? "-" :"+", val.magnitude);
    val = signMag_read();
    printf("%s%hu ", val.isNegative ? "-" :"+", val.magnitude);
    val = signMag_read();
    printf("%s%hu ", val.isNegative ? "-" :"+", val.magnitude);
}

