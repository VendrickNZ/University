#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    uint64_t id;
    uint8_t age;
    float gpa;
} Student_t;


Student_t newStudent(uint64_t id, uint8_t age, float gpa)
{
    Student_t t = {id, age, gpa};
    return t;
}

void printStudent(const Student_t* student)
{
    printf("%lu: Age %d, GPA %.2f\n", student->id, student->age, student->gpa);

}

void updateGpa(Student_t* student, float newGpa)
{
    student->gpa = newGpa;
}



int main(){
    Student_t student = newStudent(12345678, 19, 5.62);
    printStudent(&student);
    updateGpa(&student, 6.2);
    printStudent(&student);
}