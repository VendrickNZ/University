#include <stdio.h>
#include <stdint.h>

void oof(char* p1, char* p2)
{
    *p1 = *p2;
}

void printViaPtr(int16_t* intPtr)
{
    printf("%d\n", *intPtr);
}

void print2Ints(int16_t number1, int16_t number2)
{   
    printViaPtr(&number1);
    printViaPtr(&number2);
}


void swap(uint8_t* address1, uint8_t* address2)
{   
    uint8_t address1Hold = *address1;
    *address1 = *address2;
    *address2 = address1Hold;    
}
int main(void)
{      
    uint8_t i = 10, j = 20;
    swap(&i, &j);
    printf("%d %d\n", i, j);


    // print2Ints(11, -93);


    // char c = 0;
    // char other = '#';
    // scanf("%c", &c); // Reads a single character into c
    // oof(&other, &c);
    // printf("%c\n", other);
}