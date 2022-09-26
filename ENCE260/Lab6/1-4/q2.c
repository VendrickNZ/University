#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


typedef struct {
    char random;
    int8_t junk;
} Data_t;


Data_t* newData(char random, int8_t junk)
{
    Data_t* instance = malloc(sizeof(Data_t));
    instance->junk = junk;
    instance->random = random;
    return instance;

}

void freeData(Data_t* data)
{
    free(data);
}

int main(void)
{
    Data_t* data = newData('A', 1);
    printf("%c %d\n", data->random, data->junk);
    freeData(data);
}