#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct {
    uint8_t day;
    uint8_t month;
    uint16_t year;
} Date_t;

Date_t setDate(uint8_t day, uint8_t month, uint16_t year)
{
    Date_t date = {day, month, year};
    return date;
}

typedef enum {
    January = 1,
    Febuary,
    March,
    April,
    May,
    June,
    July,
    August,
    September,
    October,
    November,
    December
} Months;

void printDate(const Date_t* date)
{   
    Months curr_month = date-> month;
    switch (curr_month)  {
    case 1:
        printf("%d January %d\n", date->day, date-> year);
        break;
    case 2:
        printf("%d February %d\n", date->day, date-> year);
        break;
    case 3:
        printf("%d March %d\n", date->day, date-> year);
        break;
    case 4:
        printf("%d April %d\n", date->day, date-> year);
        break;
    case 5:
        printf("%d May %d\n", date->day, date-> year);
        break;
    case 6:
        printf("%d June %d\n", date->day, date-> year);
        break;
    case 7:
        printf("%d July %d\n", date->day, date-> year);
        break;
    case 8:
        printf("%d August %d\n", date->day, date-> year);
        break;
    case 9:
        printf("%d September %d\n", date->day, date-> year);
        break;
    case 10:
        printf("%d October %d\n", date->day, date-> year);
        break;
    case 11:
        printf("%d November %d\n", date->day, date-> year);
        break;
    case 12:
        printf("%d December %d\n", date->day, date-> year);
        break;
    } 
}



int main(){
    // Date_t date = setDate(20, 7, 1969);
    // printDate(&date);

    Date_t date = setDate(1, 1, 1970);
    printDate(&date);
}
