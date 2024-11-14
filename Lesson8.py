#                     #BAI TAP : STRING

# def CTV_thongtin (n):
#     students = []
#     for _ in range(n):
#         infor = input("Ma sinh vien, Ho Ten, Gioi Tinh, Diem: ").split(" ")
#         student = {
#             "ma_sv": infor[0],
#             "ho_ten":infor[1],
#             "gioi_tinh": infor[2],
#             "diem": float(infor[3])
#         }
        
#         students.append(student)

#     students.sort(key=lambda x: x['diem'], reverse=True)
#     top_3 = students[:3]
#     return top_3

# n = int(input("Nhập số lượng CTV: "))
# while n < 5:
#     print("Nhập lại số lượng CTV")
#     n = int(input("Nhập lại số lượng CTV (n>=5): "))

# top_3ctv = CTV_thongtin(n)
# index = 1
# for student in top_3ctv: 
#     print(f"{student['ma_sv']} {student['ho_ten']} {student['diem']}")
#     index += 1 



#                     #BAI 2:
# import string  
# def check_password(pw):
#     #1. Kiểm tra độ dài
#     if len(pw) < 6:
#         return False
#     #2. Điều kiện chữ và số
#     #Dùng any() để ktra: khi nhập vào nếu là chữ cái lập tức trả về True
#     letter = any(char.isalpha() for char in pw)
#     digit = any(char.isdigit() for char in pw)
#     special = any(char not in string.ascii_letters + string.digits for char in pw)

#     if letter and digit and not special:
#         return True
#     return False

# def count(n):
#     count = 0
#     for pw in strings:
#         if check_password(pw):
#             count += 1
#     return count

# n = int(input("Nhập số mật khẩu cần check: "))
# strings = []
# for _ in range(n):
#     strings.append(input("Nhập chuỗi: "))
# result = count(n)
# print(f'Số lượng mật khẩu hợp lệ: {result}')


                    #BAI 3: 
mang1 = set(('tài', 'thủy', 'thạch', 'trường', 'tiến'))
mang2 = set(('hải', 'tài', 'nhật minh', 'cao minh', 'đặng anh', 'hùng', 'trường'))

#Phần tử ở mang1 không ở mang2
# ketqua1 = mang1.difference(mang2)
# ketqua2 = mang2.difference(mang1)
ketqua1 = mang1 - mang2
ketqua2 = mang2 - mang1
print(ketqua1)
print(ketqua2)





                    #BAI 4:
#input: str1: "Welcome" - str2: "home"
#output: "comehome"
# str1 = input("Nhập chuỗi 1: ")
# str2 = input("Nhập chuỗi 2: ")
# while len(str1) !=  len(str2): #lặp cho đến khi độ dài str1 = str2
#     if len(str1) > len(str2):
#         str1 = str1[len(str1) - len(str2):] 
#     else:
#         str2 = str2[len(str2) - len(str1):]
    
# result = str1 + str2
# print(result)



