#ifndef TEMP_H
#define TEMP_H

#include <stdint.h>


typedef enum {
    CELSIUS,
    FAHRENHEIT,
    KELVIN
} Unit_t;

typedef struct {
    float temperature;
    Unit_t unit;
} Temp_t;

#endif //TEMP_H

