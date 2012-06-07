/*
 * $ gcc -pg gprof-test.c
 * $ gprof a.out
 */

#include <stdio.h>
#include <stdlib.h>

int func (int n) {
    int i;

    for (i = 0; i < n; i++) {
        printf("%d\n", i);
    }

    return 0;
}

int main (int argc, char const* argv[])
{

    func(10);
    func(100000);

    return 0;
}
