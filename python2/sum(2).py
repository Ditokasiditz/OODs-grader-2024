def find_triplets_with_sum_five(arr):
    n = len(arr)
    result = []
    
    
    # ใช้การวนลูปแบบสามชั้นเพื่อหาชุดของสามพจน์ที่มีผลรวมเท่ากับ 5
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 5:
                    result.append([arr[i], arr[j], arr[k]])
    
    return result

def unique_triplets(triplet_list):
    unique_set = set()
    for triplet in triplet_list:
        # แปลง triplet เป็น tuple เพื่อให้ง่ายต่อการใช้งานกับ set
        sorted_triplet = tuple(sorted(triplet))
        unique_set.add(sorted_triplet)
    
    # แปลงกลับเป็น list ของ list
    unique_list = [list(t) for t in unique_set]
    
    return unique_list



# รับ input จากผู้ใช้
input_list = input("Enter Your List : ")
array = list(map(int, input_list.split()))

# Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป
if len(array) < 3:
    print('Array Input Length Must More Than 2')
else:
    triplets = find_triplets_with_sum_five(array)
    unique_triplet_list = unique_triplets(triplets)
    print(unique_triplet_list)
