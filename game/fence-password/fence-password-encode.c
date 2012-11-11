#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char const* argv[])
{
    char buf[256];
    int i, j, len;

    scanf("%s", buf);
    len = strlen(buf);

    for (j = 0; j < 2; j++) {
        for (i = j; i < len; i+=2) {
            printf("%c", buf[i]);
        }
    }
    printf("\n");

    return 0;
}
