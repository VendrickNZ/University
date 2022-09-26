#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef enum {
    REVERSE = -1,
    NEUTRAL,
    FIRST,
    SECOND,
    THIRD,
    FOURTH,
    FIFTH
} Gear_t;



int main(){
    Gear_t currentGear = FIRST;
    printf("%d\n", currentGear + THIRD);
}