#include <stdio.h>
#include <stdlib.h>

int main (int argc, char const* argv[])
{
    int a, b, err, ans;
    char op;

    scanf("%d %c %d", &a, &op, &b);

    err = 0;
    if (op == '+') {
        ans = a + b;
    } else if (op == '-') {
        ans = a - b;
    } else if (op == '*') {
        ans = a * b;
    } else if (op == '/') {
        ans = a / b;
    } else {
        err = 1;
    }

    if (err) {
        printf("An Error Occurred\n");
    } else {
        printf("%d\n", ans);
    }

    return 0;
}
