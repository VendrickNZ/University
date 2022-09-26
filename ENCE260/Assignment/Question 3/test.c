#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <ctype.h>


typedef struct {
    bool isNegative;
    uint16_t magnitude;
} SignMag_t;


void func()
{
    int ch, i = 1;
    char str[6];

    ch = getchar();
    str[0] = ch;

    while(isdigit(ch)) {
        ch = getchar();
        str[i] = ch;
        i++;
    }
    printf("%s", str);
}

int main(void)
{
    func();
}