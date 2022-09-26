#ifndef RECT_H
#define RECT_H
#define RECT_T
#include <stdint.h>


typedef struct {
    uint32_t width;
    uint32_t height;
} Rect_t;

void rect_set(Rect_t* rect, uint32_t width, uint32_t height);

uint32_t rect_area(const Rect_t* rect);

uint32_t rect_perimeter(const Rect_t* rect);


#endif //RECT_H

