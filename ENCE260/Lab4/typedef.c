#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    float lat;
    float lon;
    float alt;
} Coord_t;

bool isBelowSeaLevel(const Coord_t coord)
{
    return coord.alt < 0;
}

uint64_t numBelowSeaLevel(const Coord_t coords[], size_t n)
{
    uint8_t i;
    uint8_t count;
    for (i = 0; i < n; i++)  {
        if (coords[i].alt < 0)  {
            count++;
        }

    }
    return count;
}



typedef struct {
    Vec_t position;
    Vec_t velocity;
} Particle_t;

// void setVelocity(Particle_t* particle, int32_t vx, int32_t vy)
// {
//     (*particle).vx = vx;
//     (*particle).vy = vy;

// }

void update(Particle_t* particle)
{
    (*particle).position.x += (*particle).velocity.x;
}


typedef struct {
    int32_t x;
    int32_t y;
} Vec_t;

Vec_t vecSum(Vec_t v1, Vec_t v2)
{
    int32_t x_sum = v1.x + v2.x;
    int32_t y_sum = v1.y + v2.y;
    Vec_t sum = {x_sum, y_sum};
    return sum;
}

int main(){
    Particle_t mote = {{0, 1}, {0, 0}};
    setVelocity(&mote, 3, 4);
    update(&mote);
    printf("v = %d, %d\n", mote.velocity.x, mote.velocity.y);
    printf("x = %d, y = %d\n", mote.position.x, mote.position.y);
}