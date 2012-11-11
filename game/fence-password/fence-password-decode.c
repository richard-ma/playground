#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char const* argv[])
{
    char buf[256];
    int i, len, gap, end;

    scanf("%s", buf);
    len = strlen(buf);

    if (len % 2 == 0) {
        gap = len / 2;
        end = gap;
    } else {
        gap = (len - 1) / 2 + 1;
        end = len / 2 + 1;
    }

    for (i = 0; i < end; i++) {
        printf("%c", buf[i]);
        printf("%c", buf[i+gap]);
    }
    printf("\n");

    return 0;
}
