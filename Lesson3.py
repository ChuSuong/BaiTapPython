                #VONG LAP

            #BAI 1: 

#1. Tinh tong tu 1 -> N
# def ham_Sum (n):
#     sumN = 0
#     for value in range (1,n+1): #dung n+1 de gtri chay tu 1 -> n
#         sumN = sumN + value
#     return sumN

# def ham_check (n):
#     for value in range (1,n+1):
#         #Bỏ qua số chia hết cho 3 và tiếp tục thực hiện
#         if value % 3 == 0:
#             continue
        
#         #Dừng hẳn nếu số đó chia hết cho 10
#         if value % 10 == 0:
#             break
        
#         print(value, end=' ') #dùng end để in các số trên 1 dòng và cách nhau 1 khoảng trắng

# import math
# def check_prime (n):
#     if n < 2: 
#         return False

#     for value in range(2, int(math.sqrt(n)) + 1): #duyệt từ 2 đến căn bậc 2 của n
#         if n % value == 0:
#             return False
#         #Nếu chia hết cho value thì không phải số nguyên tố

#     return True #Còn lại là số nguyên tố

# def sum_prime (n):
#     sumNT = 0 #Khởi tạo biến tổng 
#     for value in range (1, n+1):
#         if check_prime(value): #nếu check_prime True : là số nto thì tính tổng 
#             sumNT = sumNT + value
#     return sumNT

# def draw_triangle(n):
#     #dòng thứ value
#     for value in range(1, n + 1):
#         #in khoang trắng để căn giữa 
#         for spaces in range(n - value):
#             print(" ", end ="")
#         #Kí tự sao *
#         for stars in range (value):
#             print("* ", end="")
#         print() #xuống dòng

# #Nhập: 
# n = int(input('Nhập số nguyên n:'))

# #Xuất
# sum1 = ham_Sum(n)
# print(f'Tong cac so tu 1 den {n} la: {sum1}')

# print("Dãy số 1-n không chia hết cho 3 và 10: ", end='')
# check = ham_check(n)

# sum2 = sum_prime(n)
# print(f'\nTong cac so nguyen tố từ 1 đến {n}: {sum2}')

# draw_triangle(n)



                    #BAI 2: 
# #input() chuỗi số -> split() chia nhỏ danh sách con -> map(int,..) chuyển sang int -> list() tạo danh sách con đó thành một list
# ages = list(map(int,input("Nhập số tuổi các thành viên:").split()))

# #Gán giá trị cho max_age ở vị trí [i]
# max_age = ages[0]
# min_age = ages[0]

# #Gán vị trí ban đầu = 0
# max_position = 0
# min_position = 0

# #Duyệt i từ 0 đến độ dài của list
# for i in range(len(ages)):
#     #Tại giá trị ở vị trí i nếu lớn hơn max thì gán giá trị ở vị trí i cho max
#     #Ví dụ: tại vị trí 0 ages[1] = 10 so với max_age trước đó ở ages[0] = 5, -> 10>5 gán 10 cho max 
#     if ages[i] > max_age:
#         max_age = ages[i]
#         max_position += i

#     if ages[i] < min_age:
#         min_age = ages[i]
#         min_position += i

# print("Người lớn tuổi nhất đứng ở vị trí:", max_position)
# print("Người nhỏ tuổi nhất đứng ở vị trí:", min_position)





                    #BAI 3: SO HOÀN HẢO
#Ý tưởng: 
    #Nhập số n, check có thuộc (1,1000), nếu thuộc : check có phải số hoàn hảo k?
        #Check số hoàn hảo: tính tổng ước của số đó và so sánh nếu tổng = chính nó -> số hoàn hảo

# def is_perfect_number (n):
#     #Kiểm tra số đó có thuộc 1 - 1000 không
#     if ( n >= 1 and n <= 1000): #Nếu thuộc(1,1000) check số hoàn hảo
#         sum = 0
#         for i in range(1,n):
#             if n % i == 0:
#                 sum = sum + i #cộng các ước đã ktra đúng lại với nhau
        
#         #Trả về nếu tổng đó = n
#         if (sum == n):
#             return True
#         else:
#             return False
#     else: 
#         print("Số không thuộc trong khoảng 1 - 1000.")
#         return False


# n = int(input("Nhập số tuổi của hải:"))
# #Nhập tuổi HẢi và check xem có phải là số hoàn hảo k
# if is_perfect_number(n):
#     print ('Tuổi của Hải là số hoàn hảo')
# else:
#     print ('Tuổi của Hải không là số hoàn hảo')


                    #BAI 4: TACH SỐ
#Ý tưởng : 
        # Tách từng chữ số bằng cách chia lấy số dư
        # Số dư lấy được chèn vào vị trí đầu

# numbers = int(input("Nhap số nguyên dương: "))
# def numbers_division (numbers):
#     empty_list = [] #tạo list rỗng
#     while numbers > 0: #thực hiện cho tới khi số đó < 0
#         a = numbers % 10 #chia lấy số dư
#         empty_list.insert(0, a) #cho các số chia dư vào vị trí đầu của list
#         numbers = numbers // 10 #Bỏ chữ số cuối
#     return empty_list

# sau_tach = numbers_division(numbers)
# print(f'Các chữ số sau khi tách: {sau_tach}')


                    #BAI 5: Bài toán "Số bước tới 1"
                #Nếu n là số chẵn, ta chia n cho 2.
                #Nếu n là số lẻ, ta nhân n với 3 và cộng 1.
                #Quy tắc này được áp dụng lặp lại cho số kết quả cho đến khi n = 1

#Ý tưởng : Nhập n, kiểm tra chẵn lẻ -> đến khi n = 1 thì dừng -> đếm số bước

def so_buoc (n):
    count = 0 #Tạo biến count để đếm bao nhiêu bước để n đến 1
    while n != 1: #kiểm tra nếu n 
        if (n % 2 == 0):
            n = n // 2
        else:
            n = 3*n + 1
        count = count + 1
    return count

n = int(input("Nhập số nguyên dương n: "))
tong_so_buoc = so_buoc(n)
print(f'Số bước để {n} đi đến 1 là: {tong_so_buoc}')


            