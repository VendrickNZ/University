#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include "temp.h"


static Temp_t kelvinToCelsius(Temp_t temp)
{
    temp.temperature -=  273.15;
}

static Temp_t kelvinToFahrenheit(Temp_t temp)
{
    temp.temperature = ((temp.temperature - 273.15) * 9/5 + 32);
}
static Temp_t fahrenheitToKelvin(Temp_t temp)
{
    temp.temperature = ((temp.temperature - 32) * 5/9 + 273.15);
}
static Temp_t fahrenheitToCelsius(Temp_t temp)
{
    temp.temperature = ((temp.temperature - 32) * 5/9);
}
static Temp_t celsiusToKelvin(Temp_t temp)
{
    temp.temperature += 273.15;
}
static Temp_t celsiusToFahrenheit(Temp_t temp)
{
    temp.temperature = ((temp.temperature * 9/5) + 32);
}


static Temp_t convert(Temp_t temp, Unit_t toUnit)
{   
    Unit_t unitToChange = temp.unit;

    if (unitToChange == KELVIN && toUnit == CELSIUS) {
        kelvinToCelsius(Temp_t temp);
    }
    //I'm given a temperature, a unit, and the unit to convert to.
    //Kelvin to Cels, Kelvin to Fahrenheit,
}

void temp_set(Temp_t* temp, float value, Unit_t unit)
{
    temp->temperature = value;
    temp->unit = unit;
}

void temp_print(const Temp_t* temp, Unit_t unit)
{
    printf("");
}





int main(void)
{
    Temp_t temp;
    float value;
    scanf("%f", &value);
    temp_set(&temp, value, CELSIUS);
    temp_print(&temp, CELSIUS);
    temp_print(&temp, FAHRENHEIT);
    temp_print(&temp, KELVIN);
}