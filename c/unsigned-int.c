#include <stdio.h>
#include <stdlib.h>

int main (int argc, char const* argv[])
{
    int var_i;
    unsigned int var_ui;
    
    printf(" i: %d\n", sizeof(int));
    printf("ui: %d\n", sizeof(unsigned int));
    printf("\n");

    /* Bin: 0111 1111 1111 1111 1111 1111 1111 1111 */
    var_i = 0x7fffffff;
    var_ui = 0x7fffffff;
    printf(" i: %x\t\t%d\t\t%u\n", var_i, var_i, var_i);
    printf("ui: %x\t\t%d\t\t%u\n", var_ui, var_ui, var_ui);
    printf("\n");

    /* Bin: 1000 0000 0000 0000 0000 0000 0000 0000 */
    var_i = 0x80000000;
    var_ui = 0x80000000;
    printf(" i: %x\t\t%d\t\t%u\n", var_i, var_i, var_i);
    printf("ui: %x\t\t%d\t\t%u\n", var_ui, var_ui, var_ui);
    printf("\n");

    var_i = -1;
    var_ui = -1;
    printf(" i: %x\t\t%d\t\t%u\n", var_i, var_i, var_i);
    printf("ui: %x\t\t%d\t\t%u\n", var_ui, var_ui, var_ui);
    printf("\n");

    /* condition expr */
    /* Bin: 0111 1111 1111 1111 1111 1111 1111 1111 */
    var_i = 0x7fffffff;
    var_ui = 0x7fffffff;
    var_i++; var_ui++;
    printf(" i: %d\n", var_i > 0x7fffffff);
    printf("ui: %d\n", var_ui > 0x7fffffff);
    printf("\n");

    return 0;
}
