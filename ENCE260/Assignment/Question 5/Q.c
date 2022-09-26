#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    bool isNegative;
    uint16_t magnitude;
} SignMag_t;


SignMag_t signMag_init(bool isNegative, uint16_t magnitude)
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


SignMag_t signMag_accumulate(const SignMag_t* array, size_t arraySize)
{   
    SignMag_t instance;
    SignMag_t sum = {0, false};
    bool hugeNumber = false;
    for (uint16_t i = 0; i < arraySize; i++) {
        instance = signMag_sum(array[i], array[i+1]);
        if ((instance.magnitude + sum.magnitude) > 65535 || instance.magnitude + sum.magnitude < 0) {
            hugeNumber = true;
        }
        if (instance.isNegative) {
            if (sum.isNegative) {
                sum.magnitude += instance.magnitude;
            } else {
                if (instance.magnitude > sum.magnitude) {
                    sum.magnitude = instance.magnitude - sum.magnitude;
                    sum.isNegative = true;
                } else {
                    sum.magnitude -= instance.magnitude;
                }
            }    
        } else {
            if (sum.isNegative) {
                if (instance.magnitude > sum.magnitude) {
                    sum.magnitude = instance.magnitude + sum.magnitude;
                    sum.isNegative = true;
                } else {
                    sum.magnitude -= instance.magnitude;
                }
            } else {
                sum.magnitude += instance.magnitude;
            }
        }
        i++;
    }
    if (hugeNumber) {
        sum.magnitude = 65535;
    }
    return sum;
}


bool signMag_max(SignMag_t* num1, SignMag_t* num2, SignMag_t** max)
{
    //max points to the biggest number, return bool whether num1 or num2 is > 65535
    bool largest = false;
    if (num1->magnitude >= 65535 || num1->magnitude < 0) {
        (*max) = num1;
    return max;
    }
}
int main(void)
{   
    SignMag_t* num1 = {65535, true};
    SignMag_t* num2 = {3, false};
    SignMag_t** max = {0, false};
    signMag_max(num1, num2, max);
}