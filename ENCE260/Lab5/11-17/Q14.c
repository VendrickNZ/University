#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

typedef struct Button_s Button_t;

struct Button_s {
    uint16_t x;
    uint16_t y;
    uint16_t width;
    uint16_t height;
    void (*func)(Button_t*);
};


Button_t button_init(uint16_t x, uint16_t y, uint16_t width, uint16_t height, void (*func))
{
    Button_t instance;
    instance.x = x;
    instance.y = y;
    instance.width = width;
    instance.height = height;
    instance.func = func;
    return instance;
}

void button_click(Button_t* button)
{
    button->func(button);
}


void clickFunc(void)
{
    puts("Button Clicked!");
}


int main (void)
{
    Button_t button = button_init(480, 320, 64, 32, &clickFunc);
    button_click(&button);
}