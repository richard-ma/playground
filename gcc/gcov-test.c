/*
 * $ gcc -fprofile-arcs -ftest-coverage gcov-test.c 
 * $ ./a.out
 * $ gcov gcov-test.c
 */

#include <stdio.h>
#include <stdlib.h>

int main (int argc, char const* argv[])
{

    int i;

    for (i = 1; i < 10; i++) {
        if (i % 3 == 0) {
            printf("%d / 3\n", i);
        } else if (i % 11 == 0) {
            printf("%d / 11\n", i);
        }
    }

    return 0;
}
