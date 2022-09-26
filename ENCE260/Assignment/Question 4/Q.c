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


SignMag_t signMag_sum(SignMag_t sm1, SignMag_t sm2)
{   
    uint16_t sum = 1;
    SignMag_t instance;
    instance.isNegative = false;
    if (sm1.isNegative && sm2.isNegative) {
        instance.isNegative = true;
        sum = sm1.magnitude + sm2.magnitude;
        if ((sm1.magnitude + sm2.magnitude) >= 65535) {
            sum = 65535;
        } 
    } else if (sm1.isNegative) {
        if (sm1.magnitude > sm2.magnitude) {
            sum = (sm1.magnitude - sm2.magnitude);
            instance.isNegative = true;
        } else {
            sum = (sm2.magnitude - sm1.magnitude);
        }
        if (sum >= 65535) {
            sum = 65535;
        }        
    } else if (sm2.isNegative) {
        if (sm1.magnitude > sm2.magnitude) {
            sum = (sm1.magnitude - sm2.magnitude);
        } else {
            sum = (sm2.magnitude - sm1.magnitude);
            instance.isNegative = true;
        }
        if (sum >= 65535) {
            sum = 65535;
        }        
    } else {
        sum = (sm1.magnitude + sm2.magnitude);
        if ((sm1.magnitude + sm2.magnitude) >= 65535) {
            sum = 65535;
        }  
    }
    instance.magnitude = sum;
    return instance;
}   

int main(void)
{
	
	
    SignMag_t val1 = {false, 7};
    SignMag_t val2 = {true, 92};
    SignMag_t sum = signMag_sum(val1, val2);
    printf("%s%hu ", sum.isNegative ? "-" :"+", sum.magnitude);

    
}

