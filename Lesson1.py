#Cau 1: In ra chuỗi “Xin chao”
print("Xin chao!")

#Cau 2: 
print("Chao mung den LabAI HaUI")
print('Khoa CNTT thuoc truong DH Cong nghiep Ha Noi - “10 diem”')
strA = "Khoa CNTT thuoc truong DH Cong nghiep Ha Noi"

#dung tham số end ="" để giữ các chữ cái trên 1 dòng
#dùng for..in.. để lặp các kí tự trong strA
#sùng .isupper() -> in chữ cái in hoa, .islower() -> chu cai in thuong
for strB in strA:
    if strB.isupper():
        print(strB, end=" ")
print("\n")

for strC in strA:
    if strC.islower():
        print(strC, end=" ")

# #Kiem tra "CNTT" có thuộc chuỗi A bằng if...else
print("\n")
if "CNTT" in strA:
    print("Yes!")
else:
    print("No!")


#Thay the cac chữ in hoa thành thường và ngược lại
print("\n")
strA = strA.swapcase()
print(strA)

#Cau 3: 
#Nhập *, dùng toán tử nhân để gấp 5 lên, dùng for..in để lặp số dòng
print("\n")
sao = '*'
sao = sao * 5 
for i in range(3):
    print(sao)

#Ý 2: căn lề *
print("\n")
sao = '*'
g = '{:^5}'.format(sao)
print(g)
sao = sao * 5
for i in range(2):
    print(sao)

#Cau 4: 
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# In kết quả của các phép toán
print("a + b =", a + b)      # Cộng
print("a - b =", a - b)      # Trừ
print("a * b =", a * b)      # Nhân
print("a / b =", a / b)      # Chia
print("a // b =", a // b)    # Chia lấy phần nguyên
print("a % b =", a % b)      # Chia lấy phần dư
print("a ^ b =", a ** b)     # Lũy thừa (a^b)

#Cau 5:

Name = str(input("Họ và tên: "))
Age = int(input("Tuổi: "))
Gender= str(input("Giới tính Nam/Nữ:"))
MaritalStatus = input("Tình trạng hôn nhân (Độc thân/ Đã kết hôn):")
print("\n---Thông tin Sinh viên LAbAI HAUI---") 
#dùng định dạng bằng chuỗi f (f'giá trị chuỗi')
result = f'Họ và tên: {Name}\nTuổi: {Age}\nGiới tính: {Gender}\nTình trạng hôn nhân: {MaritalStatus}'
print(result)
