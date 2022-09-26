#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <ctype.h>


int main(void)
{   

    char input;
    while (scanf("%c", &input) != EOF)   {
        if (input == '\012') {
            printf("'\\n'\n");
        }
        else {
            if (isdigit(input)) {
                printf("'%c': Digit %c\n", input, input);
            }
            else if (isalpha(input)) {
                char str[2] = { input };
                int num = strtol(str, NULL, 36) - 9;
                printf("'%c': Letter %d\n", input, num);
            }
            else {
                printf("'%c': Non-alphanumeric\n", input);
            }
        }
    }
}