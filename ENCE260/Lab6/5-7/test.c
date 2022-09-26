#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>


typedef struct  {
    uint16_t key;
    char string[127];
    uint8_t charLength;
} Caesar_t;

// Caesar_t caesar_init(uint16_t key, char string)
// {
//     Caesar_t init = {{key, string}};
//     return init;
// }


void caesarCipher(Caesar_t caesar)
{   
    for (size_t i = 0; i < caesar.charLength; i++) {
        char letter = caesar.string[i];
        char str[2] = { letter };
        int num = strtol(str, NULL, 36) - 9;
        printf("%d\n", num);
    }
}


int main(void)
{
    Caesar_t instance = {1, "gdkkn", 5};
    caesarCipher(instance);
}