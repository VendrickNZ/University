#ifndef LIFT_H
#define LIFT_H

#include <stdint.h>


typedef struct {
    int16_t currFloor;
    uint8_t numPassengers;
    uint8_t passengerLimit;
} Lift_t;

Lift_t lift_init(uint8_t maxPassengers, int16_t startFloor);

void lift_onboard(Lift_t* lift, uint8_t peopleOff, uint8_t peopleOn);

int16_t lift_goToFloor(Lift_t* lift, int16_t floor);



#endif //LIFT_H

