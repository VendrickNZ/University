#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>


typedef struct {
    int32_t x;
    int32_t y;
} Vec_t;


typedef struct {
    Vec_t position;
    Vec_t velocity;
} Particle_t;

void setVelocity(Particle_t* particle, int32_t vx, int32_t vy)
{   
    particle->velocity.x += vx;
    particle->velocity.y += vy;
}


Vec_t vecSum(Vec_t v1, Vec_t v2)
{   
    Vec_t sum = {v1.x + v2.x, v1.y + v2.y};
    return sum;
}


void update(Particle_t* particle)
{   
    particle->position.x += particle->velocity.x;
    particle->position.y += particle->velocity.y;
    vecSum(particle->position, particle->velocity);

}

int main(){
    Particle_t mote = {{0, 1}, {0, 0}};
    setVelocity(&mote, 3, 4);
    update(&mote);
    printf("v = %d, %d\n", mote.velocity.x, mote.velocity.y);
    printf("x = %d, y = %d\n", mote.position.x, mote.position.y);
}