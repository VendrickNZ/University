#include <stdio.h>
#include <stdint.h>
#include <math.h>

void printRoots(float a, float b, float c)
{
    double x = 0;
    double y = 0;
    x = (-b - sqrt((b*b) - 4.0*a*c))/(2.0*a);
    y = (-b + sqrt((b*b) - 4.0*a*c))/(2.0*a);

    if (a == 0) {
        printf("Not a quadratic\n");
    }

    else if ((b*b - 4.0*a*c) < 0)  {
        printf("Imaginary roots\n");
    }
    
    else {
        if (x > y){
        printf("Roots are %.4f and %.4f\n", y, x);
        }   else    {
            printf("Roots are %.4f and %.4f\n", x, y);
        }
    }
}


int main()
{
    printRoots(1, -4, 3);
    printRoots(1, 2, 3);
    printRoots(0, 2, 3);
    printRoots(1, 0, -1);
    printRoots(-1, 0, 1);

}