#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include "lift.h"

#define MAX_PASSENGERS 12


Lift_t lift_init(uint8_t maxPassengers, int16_t startFloor)
{
    Lift_t init = {startFloor, 0, maxPassengers};
    return init;
}

void lift_onboard(Lift_t* lift, uint8_t peopleOff, uint8_t peopleOn)
{
    lift->numPassengers -= peopleOff;
    lift->numPassengers += peopleOn;
}

int16_t lift_goToFloor(Lift_t* lift, int16_t floor)
{
    if (lift->numPassengers <= lift-> passengerLimit)   {
        lift->currFloor = floor;
        return floor;
    } 
    return lift->currFloor;
}
