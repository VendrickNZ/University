#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <ctype.h>
#include <string.h>

FILE* openInputFile(char* filename)
{
    FILE *aFile;
    char mode[] = "r";
    aFile = fopen(filename, mode);
    if (aFile == NULL)  {
        fprintf(aFile, "Input file can't be opened");
        exit(EXIT_FAILURE);
    }
    return aFile;
}

FILE* openOutputFile(char* filename)
{
    FILE *aFile;
    char mode[] = "w";
    aFile = fopen(filename, mode);
    if (aFile == NULL)  {
        fprintf(aFile, "Output file can't be opened");
        exit(EXIT_FAILURE);
    }
    return aFile;
}

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
    
}