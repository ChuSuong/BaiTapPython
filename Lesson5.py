# #                 #BAI TAP : Practice


# #             #BAI 1:

# import math

# def prime_number(n):
#     #Kiểm tra số nguyên tố: 
#     if n <= 1: 
#         return False

#     for value in range(2, int(math.sqrt(n)) + 1): #duyệt từ 2 đến căn bậc 2 của n
#         if n % value == 0:
#             return False  #Nếu chia hết cho value thì không phải số nguyên tố
        
#     return True #Còn lại là số nguyên tố

# def symmetry_number(n):
#     #Kiểm tra số đối xứng
#     number = n 
#     symmetry = 0
#     while n > 0:
#         chu_so_cuoi = n % 10 #Lấy chữ số cuối cùng
#         symmetry = symmetry * 10 + chu_so_cuoi #Tạo ra số đảo ngược
#         n = n // 10 #Loại bỏ chữ số cuối đi và tiếp tục thực hiện vòng lặp
#     return number == symmetry

# def check_prime_symmetry (n):
#     #Kiểm tra n có phải là số nguyên tố và đối xứng không
#     return prime_number(n) and symmetry_number(n)

# #Nhập số nguyên n và kiểm tra điều kiện < 7 chữ số
# while True: 
#     n = input("Nhập số nguyên n ít hơn 7 chứ số: ")
#     if len(n) < 7: #Là số nguyên dương và ít hơn 7 chữ số
#         n = int(n)
#         break #Nếu đúng, thoát vòng lặp để check các đkiều kiện khác
#     else:
#         print("Số nhập vào không đúng.Vui lòng nhập lại!")

# if check_prime_symmetry (n):
#     print(f'Số {n} là số nguyên tố và đối xứng!')
# else: 
#     print(f'Số {n} không là số nguyên tố và đối xứng!')



                    #BAI 2 : TRO CHƠI MINION

#Ý tưởng:
#Kiếm tra chuỗi con bắt đầu bằng kí tự nào, nếu là nguyên âm Kevin + 1đ, ngược lại Staurt +1đ
# Stuart: Chuỗi con bắt đầu bằng phụ âm
# Kevin : Chuỗi con bắt đầu bằng nguyên âm (a,e,i,o,u,y)

# def minion_game(S):
#     vowels = "AEIOUY"
#     stuart_score = 0
#     kevin_score = 0


#     #Tinh điểm cho Stuart: 
#     for i in range(len(S)):
#         if S[i] in vowels: 
#             kevin_score += S.count(S[i])
#         else:
#             stuart_score += S.count(S[i])

#     print("Kevin", kevin_score)
#     print("Stuart", stuart_score)

    # if kevin_score > stuart_score:
    #     print("Kevin", kevin_score)
    # elif kevin_score < stuart_score:
    #     print("Stuart", stuart_score)
    # else : 
    #     print("None")

# while True:
#     S = input("Nhập chuỗi S:")
#     #.isalpha : ktra ký tự từ a -z (A-Z) và .isupper(): ktra tất cả là chữ in hoa
#     if S.isalpha() and S.isupper() and (len(S) > 0 and len(S) < 10 ** 6):
#         break
#     else:
#         print("Chuỗi không hợp lệ. Vui lòng nhập lại!")

# minion_game (S)                  
                   
                   
                   
                   
                    #BAI 3: TINH GÓC

#Ý tưởng:
        #Tính góc MBC bằng arctan(BC/AB)
        #Chuyển radian sang độ
# import math
# AB = int(input("Nhập độ dài cạnh AB: "))
# BC = int(input("Nhập độ dài cạnh BC: "))

# tan_MBC = BC / AB
# goc_MBC_rad = math.atan(tan_MBC) #Tính góc arctan bằng math.atan 
# goc_MBC_deg = int(math.degrees(goc_MBC_rad)) #Chuyển sang độ
# #Chuyển sang int 
# print(f'Góc MBC bằng = {goc_MBC_deg} độ')


                    #BAI 4: 
        ### LỖI            
#Ý tưởng: 
# 1. Kiểm tra xem thẻ có bắt đầu bằng 4, 5, 6 không
# 2. Kiểm tra số thẻ có đúng 16 chữ số (bao gồm cả các dấu gạch nối)
# 3. Kiểm tra dấu gạch nối chỉ xuất hiện gữa các nhóm 4 chứ số
# 4. Kiểm tra không có 4 chữ số liên tiếp lặp lại

import re 
def check_card_number (card_number):
    #Kiểm tra thẻ có đúng dạng
    #'^[456]: Bắt đầu bằng 4, 5, hoặc 6
    #\d{3} : Sau đó là 3 chữ số
    #\d{4}){3} : 3 nhóm số có 4 chữ số phân cách bới '-'
    #{16}$ : độ dài 16 số
    pattern = r'^[456]\d{3}(-\d{4}){3}$'
    if not re.match(pattern, card_number):
        return False
    
    #Kiểm tra không có 4 chữ số lặp lại liên tiếp
    #Loại bỏ dấu '-' để kiểm tra
    card_number = card_number.replace('-', '')
    
    for i in range (len(card_number) - 3):
        if card_number[i] == card_number[i+1] == card_number[i+2] == card_number[i+3]:
            return False
    
    return True

card_number = input("Nhập số thẻ tín dụng: ")

if check_card_number(card_number):
    print("Số thẻ hợp lệ!")
else:
    print("Số thẻ không hợp lệ!")
    




