// ANY MODIFICATIONS MADE HERE WILL BE IGNORED
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>

#include "months.h"

int main(void)
{
    Month_t month = JANUARY;
    puts(month + 5 == JUNE ? "true" : "false");
}