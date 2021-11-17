# Name: Woohyuk Kim
#
# Q2. Base Converter
# Date: November 16th, 2021

class Transformer(object):

    decimal_digits = '0123456789'

    def __init__(self, digits):
        self.digits = digits

    def from_decimal(self, i):
        return self._convert(i, self.decimal_digits, self.digits)

    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits))

    def _convert(self, number, fromdigits, todigits):
        raise NotImplementedError


# the _convert method in the base Transformer class raises NotImplementedError as it is an abstract method.
# It is for that reason that derived class, ChildTransformer was created in order to orverride the method
class ChildTransformer(Transformer):
    # this method does not access the class attribute or the instance attribute
    # does not have cls or self parameter
    @staticmethod
    def _convert(number, fromdigits, todigits):
        # integers can be negative
        isNegative = False
        digit = 0

        if type(number) == str:
            # check if the number is negative
            if number[0] == '-':
                number = number[1:]
                isNegative = True

            base = len(fromdigits)
            # converting base N string to base 10 integer by converting the characters
            # to their equivalent value based on the fromdigits
            for c in number:
                char_value = fromdigits.index(c)
                digit = digit * base + char_value

            if isNegative:
                digit = int(digit) * -1

            return digit

        else:
            if number < 0:
                number *= -1
                isNegative = True

            digit = number

            # convert base 10 integer to base N string
            if digit == 0:
                return 0

            else:
                result = ""
                base = len(todigits)

                # using the following mathmatical algorithm, base 10 integer can be converted to base N string
                # q0 = n; i = 0; while qi > 0 do (ri = qi mod b; q(i + 1) = qi div b; i = i + 1)
                while digit > 0:
                    remainder = digit % base
                    result = todigits[remainder] + result
                    digit = int(digit / base)

                if isNegative:
                    result = '-' + result
            return result


def main() -> None:
    # test cases
    base20 = ChildTransformer('0123456789abcdefghij')
    print(base20.from_decimal(1234))
    print(base20.to_decimal('31e'))

    binary_transformer = ChildTransformer('01')
    print(binary_transformer.from_decimal(10))
    print(binary_transformer.to_decimal('1010'))

    hex_transformer = ChildTransformer('0123456789ABCDEF')
    print(hex_transformer.from_decimal(580))
    print(hex_transformer.to_decimal('244'))

    base62_transformer = ChildTransformer(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')
    print(base62_transformer.from_decimal(920))
    print(base62_transformer.to_decimal('Oq'))


# main function call
if __name__ == "__main__":
    main()
