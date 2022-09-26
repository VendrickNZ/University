#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    //char = ch, string = s, sentence = sen
    char ch;
    scanf("%c", &ch);
    printf("%c", ch);
    
    char s[100];
    scanf("%s", s);
    printf("\n%s", s);

    char sen[100];
    printf("");
    gets(sen);

    printf("%s", sen);
    puts(sen);

    return 0;
}

    // int BUFFSIZE = 256;
    
    // char c;
    // char str[BUFFSIZE];
    // char sen[BUFFSIZE];
    
    // scanf("%c ", &c);
    // scanf("%s ", str);
    // fgets(sen, BUFFSIZE, stdin);
    
    // printf("%c\n", c);
    // printf("%s\n", str);
    // printf("%s\n", sen);
    