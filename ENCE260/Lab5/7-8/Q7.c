#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <ctype.h>
#include <string.h>

size_t readString(char* string, size_t max_string_length)
{
    size_t count = 0;
    int8_t character = getchar();

    while ((count < max_string_length) && (character != '\n') && (character != EOF))   {
        string[count] = character;
        character = getchar();
        count++;
    }
    string[count] = '\0';
    return strlen(string);
}




int main(void)
{
    size_t len=0;
    char string[11];
    len = readString(string, 10);
    printf("Read String (%s) of length (%I64u)\n", string, len);
}