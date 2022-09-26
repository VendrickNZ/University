#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// char* skipping(const char* string, size_t n)
// {   uint16_t count = 0;
//     char **array = calloc(n, sizeof(char*));
//     for (size_t i = 0; i < n; i++) {
//         array[i] = calloc(1, 50);
//     }
//     for (size_t i = 0; i < n; i++) {
//         if (i % 2 == 0) {
//             *array[count] = string[i];
//             count++;
//         }
//     }
//     printf("%s", array);
//     return *array;
// }


char* skipping(const char* string, size_t n)
{   
    uint16_t count = 0;
    char *array = calloc(n+1, sizeof(char));
    for (size_t i = 0; i < n; i++) {
        if (i % 2 == 0) {
            array[count] = string[i];
            count++;
        }
    }
    return array;
}


int main(void)
{
    char* s = skipping("", 0);
    printf("%s\n", s);
    free(s);
}


