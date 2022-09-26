#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef enum {
    NORTH,
    SOUTH,
    EAST,
    WEST
} Heading_t;



int main(){
    Heading_t dir = NORTH;
    printf("%d\n", dir == NORTH);
}