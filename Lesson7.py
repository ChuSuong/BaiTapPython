                    #DAY 7: SET_DICTIONARY

                #BAI 1: SET


# #Nhập 2 set từ bàn phím: 
#         #input(): Nhập set dạng chuỗi
#         #.split(): phân tách chuỗi thành các phần tử con dựa trên cách mặc định, ta được list
#         #map(int..): các đối tượng trong list là kiểu int
#         #set(): chuyển thành set
# set1 = set(map(int, input("Nhập các phần tử của set1 : ").split()))
# set2 = set(map(int, input("Nhập các phần tử của set2 : ").split()))

# #1. Tạo ra 1 set mới gồm tất cả phần tử trong 2 set ban đầu và in ra màn hình
# set_union = set1 | set2
# print(f"Hợp của 2 set: {set_union}")

# #2. In ra màn hình những phần tử giống nhau trong 2 set ban đầu
# set_intersection = set1 & set2
# print(f"Giao của 2 set: {set_intersection}")

# #3.  In ra màn hình những phần tử có trong set 1 mà không có trong set 2, và ngược lại
# print(f'Phần tử thuộc set1 và không thuộc set2: {set1.difference(set2)}')
# print(f'Phần tử thuộc set2 và không thuộc set1: {set2.difference(set1)}')

# #Kiểm tra xem set 1 có phải là tập con hay tập chứa của set 2 hay không?
# #Xét tập con:
# if set1.issubset(set2):
#     print("set1 là tập con của set2")
# else:
#     print("set1 không phải là tập con của set2!")

# #Xét tập chứa
# if set1.issuperset(set2):
#     print("set1 là tập chứa của set2")
# else:
#     print("set1 không phải là tập chứa của set2!")

# #5. In ra dãy đã sắp xếp ở câu 1
# #Vì set không quan tâm đến vị trí của những phần tử (hash object)
# #Ta chuyển nó thành dạng unhash object để sắp xêps
# set_union1 = list(set_union)
# set_union1.sort() #Mặc định Key = None, reverse = False (bé - lớn)
# print(f"Dãy đã sắp xếp: {set_union1}")


                #BAI 2: 

        
# # Nhập chuỗi từ bàn phím
# text = input("Nhập chuỗi các từ: ")

# # Tách chuỗi thành các từ
# words = text.split()

# # Khởi tạo dictionary để đếm tần suất
# word_count = {}

# # Đếm tần suất của từng từ
# for word in words:
#     if word in word_count:
#         word_count[word] += 1  # Nếu từ đã có trong dictionary, tăng số đếm lên 1
#     else:
#         word_count[word] = 1  # Nếu từ chưa có trong dictionary, thêm vào với giá trị đếm = 1

# # # Sắp xếp các từ theo thứ tự từ điển
# sorted_words = sorted(word_count.keys())

# # # In kết quả theo yêu cầu
# for word in sorted_words:
#     print(f'{word} {word_count[word]}')



                    #BAI 3:
 
#Nhập list1: mã học phần
ma_hoc_phan = ["IT6002", "IT6126", "IT6067", "IT6120"]
chi_tiet = [
    {"ten_mon_hoc": "Cau truc du lieu va giai thuat", "so_tin_chi": 3},
    {"ten_mon_hoc": "He thong co so du lieu", "so_tin_chi": 4},
    {"ten_mon_hoc": "Kien truc may tinh va he dieu hanh", "so_tin_chi": 3},
    {"ten_mon_hoc": "Lap trinh huong doi tuong", "so_tin_chi": 3}
]

# chi_tiet = []
# for _ in range(len(ma_hoc_phan)):
#     ten_mon_hoc = input("Nhập tên môn học:")
#     so_tin_chi = input("Nhập số tín chỉ: ")
#     #Nối 2 biến với nhau và cho vào list
#     chi_tiet.append({"Ten_mon_hoc": ten_mon_hoc}, {"So_tin_chi": so_tin_chi})

#Tao dict từ 2 list
# mon_hoc = {}
# for i in range(len(ma_hoc_phan)):
#     mon_hoc[ma_hoc_phan[i]] = chi_tiet[i]

# print(f'Dữ liệu môn học: {mon_hoc}')
# def loc_mon_hoc(mon_hoc):
#     ket_qua = {}
#     for ma, chi_tiet in mon_hoc.items():
#         ten_mon_hoc = chi_tiet["ten_mon_hoc"]
#         so_tin_chi = chi_tiet["so_tin_chi"]
        
#         # Kiểm tra điều kiện
#         if len(ten_mon_hoc.split()) > 5 and so_tin_chi >= 3:
#             ket_qua[ma] = chi_tiet
#     return ket_qua

# # Gọi hàm và in kết quả
# mon_hoc_loc = loc_mon_hoc(mon_hoc)
# print("Dữ liệu môn học sau khi lọc:", mon_hoc_loc)



                        #BAI 4: TAO EMAILS
import random
import string
def password_random (length = 3):
    A_Z = string.ascii_uppercase 
    number = string.digits
    request = A_Z + number
    A = random.choices(request, k = length)
    return ''.join(A)

def create_mail (n):

    for _ in range(n):
    #Nhập mã sinh viên:
        username = input("Nhập mã sinh viên: ")
        while len(username) != 10 :
            print("Nhập lại mã sinh viên!")
            username = input("Nhập mã sinh viên theo yêu cầu: ")
        
        #Tạo dạng mail:
        mail = f'{username}@lab601.edu.vn'
        password = password_random() + username

        #Thêm thông tin vào dict
        edu_mail = {}
        edu_mail[username] = {
            "mail" : mail,
            "password": password
        }
    return edu_mail

n = int(input("Nhập số lượng thành viên: "))
edu_mail1 = create_mail(n)
print("Thông tin edu_mail: ", edu_mail1)