#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

uint32_t countRushes(float screeHeight, float rushHeight, float slideBack)
{
    uint32_t i = 0;
    float currHeight = 0;
    if (screeHeight >= rushHeight){
        do  {
            currHeight += rushHeight;
            i++;
            if (currHeight >= screeHeight){
                return i;
            }
            currHeight -= slideBack;
        }   while ((currHeight < screeHeight) && (screeHeight > rushHeight));
    }   else{
        return 0;
    }
    return i;
}


void printPrimesInRange(uint32_t n1, uint32_t n2)
{
    bool x = false;
    for (uint32_t i = n1; i <= n2; i++) {
        for (uint32_t j = 2; j <= n2 - 1; j++)   {
            if ((i % j == 0) && j != i) {
                x = true;
            }
            if ((j == n2 - 1) && (x == false)){
                printf("%d\n", i);
            }
        }
        x = false;
    }
}

int main()
{
    printPrimesInRange(2, 40);
    printPrimesInRange(60, 65);

}