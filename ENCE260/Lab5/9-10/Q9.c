#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

char* words[] = {"never", "a", "truer", "word", "was", "said", "in", "jest"};


int main(void)
{   
    for (int i = 0; i < sizeof(words); i++){
    printf("%s\n", words[i]);
    }
}