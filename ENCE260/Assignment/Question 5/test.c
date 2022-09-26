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

int main(void)
{
    SignMag_t sum1 = {true, 55000};
    SignMag_t sum2 = {true, 70};
    SignMag_t sum3= {true, 32000};
    SignMag_t sum4 = {false, 1};
    SignMag_t sum5 = {false, 32};
    SignMag_t sum6 = {false, 20};

    SignMag_t array[6] = {sum1, sum2, sum3, sum4, sum5, sum6};
	signMag_accumulate(array, 6);  // = -23
    //-93 + 18 + 52 = -23
    // all true or all false = +-123
}


// SignMag_t signMag_accumulate(const SignMag_t* array, size_t arraySize)
// {
//     uint16_t totalsum;
//     SignMag_t instance;
//     uint16_t instanceArray[arraySize];
//     uint16_t arrayCount;
//     bool negativeArray[arraySize];
//     bool negativeSum = false;
//     for (uint16_t i = 0; i < arraySize; i++){
//         if (instance.magnitude >= 65535) {
//             instance.magnitude = 65535;
//         }
//         instance = signMag_sum(array[i], array[i+1]); 
//         instanceArray[arrayCount] = instance.magnitude;
//         i++;
//         arrayCount++;
//         if (instance.isNegative) {
//             negativeArray[arrayCount] = true;
//         } else {
//             negativeArray[arrayCount] = false;
//         }
//     }
//     printf(negativeArray[0] ? "true\n" : "false\n");
//     for (int loop = 0; loop < (arraySize / 2); loop++){
//         if (totalsum >= 65535) {
//             totalsum = 65535;
//         } 
//         if (negativeArray[loop]){
//             if (instanceArray[loop] < 65535){
//                 printf("Total sum: %d, InstanceArray value: %d\n\n\n", totalsum, instanceArray[loop]);
//                 if (totalsum < instanceArray[loop]) {
//                     totalsum += instanceArray[loop];
//                     negativeSum = true;
//                 } else {
//                     totalsum -= instanceArray[loop];
//                 }
//             } else {
//                 totalsum = 65535;
//                 } 
//         } else {
//             if (instanceArray[loop] < 65535) {
//                 totalsum += instanceArray[loop];
//                 printf("Total sum: %d, InstanceArray value: %d\n\n\n", totalsum, instanceArray[loop]);
//             } else {
//                 totalsum = 65535;
//             }
//         }
//     } 
//     instance.magnitude = totalsum;
//     printf("%d\n", instance.magnitude);
//     printf(instance.isNegative ? "true\n" : "false\n");
//     printf(negativeSum ? "true neg sum \n" : "false neg sum\n");
//     if (negativeArray[0]){
//     return instance;
//     }
//     return instance;
// }