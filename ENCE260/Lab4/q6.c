#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int32_t x;
    int32_t y;
} Vec_t;


void addToVec(Vec_t* v1, Vec_t v2)
{
    v1->x += v2.x;
    v1->y += v2.y;
}


int main(){
    Vec_t v1 = {1, 1};
    Vec_t v2 = {2, 3};
    addToVec(&v1, v2);
    printf("%d, %d\n", v1.x, v1.y);
}