#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

void convertDistance(const double* metres, double* centimetres, double* kilometres)
{
    *centimetres = *metres * 100;
    *kilometres = *metres / 1000;
}


// void printArray(int32_t* const array, size_t n)
// {
//     for (size_t i = 0; i < n; i++)   {
//         printf("%d\n", *(array + i));
//     }
// }

void squareArray(int32_t array[], size_t n)
{
    for (size_t i = 0; i < n; i++)   {
        int32_t num = *(array + i);
        *(array + i) = num * num;
    }
}

bool isInData(const uint8_t* data, size_t arraySize, const uint8_t* ptr)
{
    return ptr < arraySize + data && ptr >= data;
}

void copyArray(const int32_t *src, int32_t *dest, size_t n)
{
    for (size_t i = 0; i < n; i++)  {
        *(dest + i) = *(src + i);
    }
}

int32_t index2d(int32_t* array, size_t width, size_t i, size_t j)
{   
    int8_t position = ((i * width) + j);
    return array[position];
}

bool isWonRow(char player, const char game[3][3], uint8_t rowNum)
{   
    bool x = true;
    for (size_t i = 0; i < 3; i++) {
        if (game[rowNum][i] != player)  {
            x = false;
        }
    }
    return x;
}

int main(void)
{
    const char game[3][3] = {{'X', 'O', ' '},{' ', ' ', ' '}, {'X', 'X', 'O'}};
    printf(isWonRow('X', game, 2) ? "true\n" : "false\n") ;
}
