program calc;
var
    a, b, err, ans: integer;
    op: char;
begin
    read(a);
    writeln(a);
    read(op);
    writeln(op);
    read(b);
    writeln(b);

    err := 0;
    if (op = '+') then ans := a + b
    else if (op = '-') then ans := a - b
    else if (op = '*') then ans := a * b
    else if (op = '/') then ans := a div b
    else err := 1;

    if (err = 1) then writeln('An Error Occurred')
    else writeln(ans);
end.
