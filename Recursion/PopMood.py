# ในยุคสมัยที่กระแสวงการสายมูมาแรงมากแซงทางโค้ง ท่านประธานบริษัทป็อปมู้ด (Pop Mood) ต้องการออกไลน์โปรดักส์ใหม่เป็นสินค้าอาร์ตทอย (Art Toy) ที่กำลังได้รับความนิยมสุดๆ ขายดีเป็นเทน้ำเทท่าจนต้องไปต่อคิวรอกันเลยทีเดียว โดยการเกิดขึ้นของโปร์ดักส์ใหม่นี้ก็เพราะว่าท่านประธานต้องการขยายฐานลูกค้าบุกตลาดผู้ชื่นชอบของสะสมเสริมดวงชะตาชีวิต ซึ่งคุณเจ๊บหัวหน้าฝ่ายโปรดักส์จะต้องไปขูดเพื่อหาตัวเลขศักดิ์สิทธิ์ ณ สถานที่แห่งนึง โอ้ พระเจ้า คุณเจ๊บพบตัวเลขนั้นจริงด้วย คุณเจ๊บต้องออกแบบตัวเลขที่เป็นไปได้ทั้งหมด เพื่อเสนอไปที่ท่านประธานให้เลือกว่าอยากจะทำคอลเลกชันใหม่นี้ด้วยเลขเซตไหนดี คุณเจ๊บค่อนข้างจะเหนื่อยกับงานมากๆ แค่ขูดหาตัวเลขก็หมดพลังจึงได้ขอร้องให้คุณที่เป็นโปรแกรมเมอร์ไฟแรง “ช่วยเขียนโปรแกรมเพื่อแสดงผลคำตอบทั้งหมดที่เป็นไปได้จากเลขโดดให้หน่อย”

# ปล. ใช้ฟังก์ชั่น sort ได้ (ควร)


def generate_numbers(sequence, current=""):
    result = []

    if current:
        result.append(int(current))

    for i in range(len(sequence)):
        next_current = current + sequence[i]
        remaining = sequence[:i] + sequence[i + 1 :]
        result.extend(generate_numbers(remaining, next_current))

    return result


input_numbers = input("Enter digits : ")

digits = input_numbers.split()
if not all(d.isdigit() for d in digits):
    print("Invalid input")
else:
    all_numbers = generate_numbers(digits)

    unique_numbers = sorted(set(all_numbers))

    print("Output :", unique_numbers)
