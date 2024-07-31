# ***** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# หา Factorial ของ input ที่รับมา โดยใช้ Recursive


def factorial(n):
    # Base case: n is 0 or 1, the factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial(n-1)
    else:
        return n * factorial(n - 1)


inp = int(input("Enter Number : "))

print(str(inp) + "! =", factorial(inp))
