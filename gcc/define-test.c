/*
 * $ gcc -DTEST define-test.c
 * $ gcc define-test.c  
 */

#include <stdio.h>
#include <stdlib.h>

int main (int argc, char const* argv[])
{

#ifdef TEST
    printf("TEST Defined.\n");
#else
    printf("Normal Running.\n");
#endif


    return 0;
}
