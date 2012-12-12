#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main (int argc, char const* argv[])
{
    int ans, cur;

    printf("Game Start!\n");
    printf("Loading...\n");
    srand((unsigned)time(0));
    ans = rand() % 1000;
    printf("Ready! Go!\n");

    while (1) {
        printf("Guess Number: ");
        scanf("%d", &cur);

        if (cur > ans) {
            printf("Your number is bigger than the answer.\n");
        } else if (cur < ans) {
            printf("Your number is smaller than the answer.\n");
        } else {
            break;
        }
    }

    printf("You Got It!\n");
    printf("The answer is %d.\n", ans);

    return 0;
}
