#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int32_t x;
    int32_t y;
    int32_t vx;
    int32_t vy;
} Particle_t;

void setVelocity(Particle_t* particle, int32_t vx, int32_t vy)
{
    (*particle).vx = vx;
    (*particle).vy = vy;

}

void update(Particle_t* particle)
{
    particle->x += particle->vx;
    particle->y += particle->vy;
}

int main(void)
{
    Particle_t mote = {
    .x = 0,
    .y = 1,
    .vx = 0,
    .vy = 0
};
    setVelocity(&mote, 3, 4);
    update(&mote);
    printf("v = %d, %d\n", mote.vx, mote.vy);
    printf("x = %d, y = %d\n", mote.x, mote.y);
}