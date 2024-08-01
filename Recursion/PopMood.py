# ในยุคสมัยที่กระแสวงการสายมูมาแรงมากแซงทางโค้ง ท่านประธานบริษัทป็อปมู้ด (Pop Mood) ต้องการออกไลน์โปรดักส์ใหม่เป็นสินค้าอาร์ตทอย (Art Toy) ที่กำลังได้รับความนิยมสุดๆ ขายดีเป็นเทน้ำเทท่าจนต้องไปต่อคิวรอกันเลยทีเดียว โดยการเกิดขึ้นของโปร์ดักส์ใหม่นี้ก็เพราะว่าท่านประธานต้องการขยายฐานลูกค้าบุกตลาดผู้ชื่นชอบของสะสมเสริมดวงชะตาชีวิต ซึ่งคุณเจ๊บหัวหน้าฝ่ายโปรดักส์จะต้องไปขูดเพื่อหาตัวเลขศักดิ์สิทธิ์ ณ สถานที่แห่งนึง โอ้ พระเจ้า คุณเจ๊บพบตัวเลขนั้นจริงด้วย คุณเจ๊บต้องออกแบบตัวเลขที่เป็นไปได้ทั้งหมด เพื่อเสนอไปที่ท่านประธานให้เลือกว่าอยากจะทำคอลเลกชันใหม่นี้ด้วยเลขเซตไหนดี คุณเจ๊บค่อนข้างจะเหนื่อยกับงานมากๆ แค่ขูดหาตัวเลขก็หมดพลังจึงได้ขอร้องให้คุณที่เป็นโปรแกรมเมอร์ไฟแรง “ช่วยเขียนโปรแกรมเพื่อแสดงผลคำตอบทั้งหมดที่เป็นไปได้จากเลขโดดให้หน่อย”

# ปล. ใช้ฟังก์ชั่น sort ได้ (ควร)


def generate_combinations(numbers):
    def recursive_combinations(prefix, remaining):
        if prefix:
            combinations.add(int("".join(map(str, prefix))))
        for i in range(len(remaining)):
            new_prefix = prefix + [remaining[i]]
            new_remaining = remaining[:i] + remaining[i + 1 :]
            recursive_combinations(new_prefix, new_remaining)

    combinations = set()  # ใช้ set เพื่อป้องกันค่าซ้ำ
    sorted_numbers = sorted(numbers)
    recursive_combinations([], sorted_numbers)

    if len(combinations) == 0:
        return None
    else:
        return sorted(combinations)


def main():
    input_digits = input("Enter digits : ").split()

    if all(digit.isdigit() for digit in input_digits) and all(
        int(e) <= 10 for e in input_digits
    ):

        numbers = [int(digit) for digit in input_digits]
        all_combinations = generate_combinations(numbers)
        print("Output :", all_combinations)

    else:
        print("Invalid input")


# เรียกใช้ฟังก์ชันหลัก
main()
