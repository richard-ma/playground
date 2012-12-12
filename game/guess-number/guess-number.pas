program guess_number;
var
    ans, cur: longint;
begin
    assign(input, '');
    assign(output, '');
    reset(input);
    rewrite(output);

    writeln('Game Start!');
    writeln('Loading...');
    randomize;
    ans := random(1000) + 1;
    writeln('Ready! Go!');

    while (true) do
    begin
        write('Guess Number: ');
        readln(cur);

        if (cur > ans) then writeln('Your number is bigger than the answer.')
        else if (cur < ans) then writeln('Your number is smaller than the answer.')
        else break;
    end;

    writeln('Got It!');
    writeln('The answer is ', ans);

    close(input);
    close(output);
end.
