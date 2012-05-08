#include <stdio.h>
#include <stdlib.h>

int main (int argc, char const* argv[])
{

    unsigned int var_ui;
    int var_i;

    var_ui = 0x7fffffff;
    var_i = 0x7fffffff;

    var_ui++;
    var_i++;

    printf("%d %d\n", var_i > 0x7fffffff, var_ui > 0x7fffffff);

    return 0;
}
