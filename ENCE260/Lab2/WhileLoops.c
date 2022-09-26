#include <stdio.h>
#include <stdint.h>
// #include <ctype.h>

uint8_t intLog2(uint32_t value)
{
    uint32_t i = 0;
    while (value > 1)  {
        value /= 2;
        i++;
    }
    return i;
}

int main()
{   
    int32_t i = 0;
    char c;
    print("Hello There");
    do  {
        c = getchar();
        i++;
    }   while (c != 'q');
    return i;
}
