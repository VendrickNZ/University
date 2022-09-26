#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct {
    char* name;
    int age;
    double height;
} Person_t;

Person_t newPerson(char* name, int age, double height)
{

}


void freePerson(Person_t* person);
{
    
}

int main(void)
{
    Person_t* employee = newPerson("Billy", 30, 1.68);
    printf("%s is age %d and is %.2f m tall\n", employee->name, employee->age, employee->height);
    freePerson(employee);
}


