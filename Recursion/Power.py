def power(a, b):
    # Base case: b is 0, any number raised to the power of 0 is 1
    if b == 0:
        return 1
    # Recursive case: multiply a by the result of power(a, b-1)
    else:
        return a * power(a, b - 1)


# ตัวอย่างการเรียกใช้ฟังก์ชัน

a, b = map(int, input("Enter Input a b : ").split(" "))

print(power(a, b))
