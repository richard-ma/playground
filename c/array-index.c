#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char const* argv[])
{

    int i[10];
    memset(i, 0, sizeof(int) * 10);

    1[i] = 7; /* okey, this is not i[1] */

    printf("%d\n", i[1]);

    return 0;
}
