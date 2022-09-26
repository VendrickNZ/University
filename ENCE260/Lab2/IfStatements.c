#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

void printThreshold(uint32_t x)
{
    if (x < 100) {
        printf("x is less than 100\n");
    } else {
        printf("x is not less than 100\n");
    }
}

void meetsCondition(int64_t x)
{
    // prints true if number is even and >= 0
    // prints true if number is odd and < 0
    // comments bug the question if i am wondering why it says more than 1 if

    if ((x >= 0 && (x%2) == 0) || (x < 0 && (x%2) != 0)) {
        printf("true\n");
    } else {
        printf("false\n");
    }
}


void printDigitName(uint8_t digit)
{
    switch (digit) {
        case 1:
            printf("One\n");
            break;
        case 2:
            printf("Two\n");
            break;
        case 3:
            printf("Three\n");
            break;
        case 4:
            printf("Four\n");
            break;
        case 5:
            printf("Five\n");
            break;
        default:
            printf("Out of bounds\n");
    }
}

void printValueName(uint8_t value)
{
    switch (value) {
        case 11:
            putchar('J');
        case 12:
            putchar('Q');
        case 13:
            putchar('K');
    }
}


int32_t gringe(int32_t boink, int32_t flunk) 
{
    // int32_t floodle = 0;
    // if (boink == flunk) {
    //     floodle = 42;
    // } else {
    //     floodle = flunk - 11;
    // }
    // return floodle;

    return (boink == flunk) ? 42 : flunk - 11; 
}


int main()
{    	
    // printThreshold(32);
    // printThreshold(100);
    // printThreshold(115);
    // meetsCondition(0);
    // meetsCondition(-2);
    // printDigitName(1);
    // printDigitName(6);
    // printDigitName(5);
    // printValueName(11);
    printf("%d\n", gringe(23, 23));
    printf("%d\n", gringe(23, 24));

}