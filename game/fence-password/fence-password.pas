program fence_password;
var
    buffer: string;
begin
    assign(input, 'fence_password.in');
    assign(output, 'fence_password.out');
    reset(input);
    rewrite(output);

    readln(buffer);
    len = length(buffer);



    close(input);
    close(output);
end.
