#!/usr/bin/env python
# for python3

# base x (max x is 62)
# encode(integer, base_x) convert base 10 integer to base x string
# decode(string, base_x) convert base x string to base 10 integer

import math

class BaseXConverter(object):

    DICT = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    DIGIT_START = 0
    UPPER_START = 10
    LOWER_START = 36

    @staticmethod
    def encode(integer, base_x = 62):
        """convert base 10 integer to base x string

        :integer: base 10 integer
        :returns: base x string

        """
        ans = list()
        while integer > 0:
            integer, reminder = divmod(integer, base_x)
            ans.append(reminder)
        ans = list(reversed(ans))
        ans = list(map(lambda x: BaseXConverter.DICT[x], ans))
        ans = ''.join(ans)
        return ans

    @staticmethod
    def decode(string, base_x = 62):
        """@todo: Docstring for decode.

        :string: base x string
        :returns: base 10 integer

        """
        l = list(reversed(list(map(lambda x: BaseXConverter.DICT.index(x), string))))
        ans = 0
        for k, v in enumerate(l):
            ans += v * math.pow(base_x, k)
        return int(ans)

if __name__ == '__main__':
    test_num = 32767
    print("========Base 62========")
    base = 62
    ans = BaseXConverter.encode(test_num, base)
    print(ans)
    print(BaseXConverter.decode(ans, base))
    print("========Base 16========")
    base = 16
    ans = BaseXConverter.encode(test_num, base)
    print(ans)
    print(BaseXConverter.decode(ans, base))
    print("========Base 10========")
    base = 10
    ans = BaseXConverter.encode(test_num, base)
    print(ans)
    print(BaseXConverter.decode(ans, base))
    print("========Base 8========")
    base = 8
    ans = BaseXConverter.encode(test_num, base)
    print(ans)
    print(BaseXConverter.decode(ans, base))
    print("========Base 2========")
    base = 2
    ans = BaseXConverter.encode(test_num, base)
    print(ans)
    print(BaseXConverter.decode(ans, base))
