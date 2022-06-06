class ReverseString(str):
    def __str__(self) -> str:
        # print the string reverse
        return self[::-1]

stringOperator = ReverseString('Encoded By Reverse')
print(stringOperator)