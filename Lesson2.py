                #CAU DIEU KIEN : if else _ Kieu Boolen
       


             #BAI 1: KIEM TRA NĂM NHUÂN
    #Input : 2021   2004    2019
    #Output: NO     YES      NO

# def kiem_tra_nam_nhuan(year):
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         return "YES"
#     else:
#         return "NO"
# year = int(input("Nhập năm cần kiểm tra: "))
# print(kiem_tra_nam_nhuan(year))

           
           

                 #BAI 1: PHAT QUA

    #Input : n=10, m=6, k=4 
    #Output: Không chia đều được cho các bạn  
    #Input : n=4, m=9, k=4 
    #Output: Chia đều được cho các bạn      

# def phat_qua (sum_sotui): 
#     if sum_sotui % n == 0:
#         print('Chia đều được cho các bạn ')
#     else: 
#         print('Không chia đều được cho các bạn!')
     
# n = int(input("Nhập số bạn: "))
# m = int(input("Nhập số hộp quà: "))
# k = int(input("Nhập túi qua : "))
# sum_sotui = m * k
# phat_qua(sum_sotui)

           



                 #BAI 2: XEP LOAI HOC SINH

    # - Xếp loại A nếu tổng điểm từ 8.50 trở lên. 
    # - Xếp loại B nếu tổng điểm từ 7.00 tới cận 8.49. 
    # - Xếp loại C nếu tổng điểm từ 5.00 tới cận 6.99. 
    # - Xếp loại D nếu điểm từ 4.00 tới 4.99.
    # - Còn lại xếp loại F và in ra màn hình “Bạn đã đánh mất 3.112.500!”

# def xep_loai_hs (diem):
#     if (diem >= 8.5):
#         print("Xếp loại A")
#     elif (diem >= 7.00 and diem <= 8.49):
#         print("Xếp loại B")
#     elif (diem >= 5.00 and diem <= 6.99):
#         print("Xếp loại C")
#     elif (diem >= 4.00 and diem <= 4.99):
#         print("Xếp loại D")
#     else:
#         print("Xếp loại F\nBạn đã đánh mất 3.112.500! ")

# diem = float(input("Nhap diem: "))
# xep_loai_hs(diem)

                




                        #BAI 3: 

    # Không dùng cấu trúc if-else hãy so sánh a và b.
    #Nếu a>b in ra “YES” còn lại in ra “NO”. với a, b là 2 số được nhập từ bàn phím.

# a = float(input("Nhập vào số a: "))
# b = float(input("Nhập vào số b: "))
# check = a > b
# print((check and "YES") or "NO" )


                



                 #BAI 4: CHECK KHOANG CACH
    #input: A(1,1), B(2,2), C(3,3)
    #output: Nhà A gần trường nhất. Nhà C xa trường nhất

# #1. import thư viên math để tính cthuc khoảng cách
# import math

# #2. tính khoảng cách mot diem (x,y) - goc toa do O(0,0)
# def tinh_khoang_cach(x,y):
#     return math.sqrt(x**2 + y**2) 

# #3.Nhập tọa độ của các điểm
# #split : chia chuoi thanh cac ptu rieng le -> map(int,..) chuyen ptu thanh so nguyen
# x1, y1 = map(int, input("Nhập tọa độ của A (x1, y1): ").split())
# x2, y2 = map(int, input("Nhập tọa độ của B (x2, y2): ").split())
# x3, y3 = map(int, input("Nhập tọa độ của C (x3, y3): ").split())

# #4. Tinh khoang cach
# kc_A = tinh_khoang_cach(x1, y1)
# kc_B = tinh_khoang_cach(x2, y2)
# kc_C = tinh_khoang_cach(x3,y3)


# #5. Kiểm tra xem kc nào kc nào lớn nhất?
# if kc_A >= kc_B and kc_A >= kc_C:
#     xa_nhat = 'A'
# elif kc_B >= kc_A and kc_B >= kc_C:
#     xa_nhat = 'B'
# else:
#     xa_nhat = 'C'

# #5. Kiểm tra xem kc nào kc nào ngan nhất?
# if kc_A <= kc_B and kc_A <= kc_C:
#     gan_nhat = 'A'
# elif kc_B <= kc_A and kc_B <= kc_C:
#     gan_nhat = 'B'
# else:
#     gan_nhat = 'C'

# print(f'Nha {gan_nhat} gần trường nhất.')
# print(f'Nha {xa_nhat} xa trường nhất.')




                #BAI 5: ĐIỀU KIỆN KHUYẾN MÃI

        #1. Khách mới : giảm 15% >< 10%
        #2. Số lượng: 1-5sp: không giảm, 6-10 : 5%, >10 : 10%
        #3. Tổng giá trị: 10K - 50K : 8%, > 50K : 15%
        #4. Khách ưu tiên: khách mới + sp > 10 + tổng gtri > 100K : 20%

# #Dùng hàm để tạo biến giảm giá = 0 trước khi thực hiện các đkien
# def tinh_tong_tien (loai_khach_hang, so_san_pham, tong_gia_tri ):
#     giam_gia = 0

#     #4. Xét trường hợp giảm giá khách ưu tiên trước
#     if(loai_khach_hang == 'Yes' and so_san_pham > 10 and tong_gia_tri > 100000):
#         giam_gia += 20
    
#     else: 
#         #1. Giảm giá theo loại khách hàng 
#         if loai_khach_hang == 'Yes': #khách mới
#             giam_gia = giam_gia + 15
#         else:#'khách cũ'
#             giam_gia = giam_gia + 10

#         #2. Giảm giá theo số sản phẩm mua
#         if (so_san_pham >= 1 and so_san_pham <= 5):
#             return 0
#         elif(so_san_pham >=6 and so_san_pham <=10):
#             giam_gia = giam_gia + 5
#         elif(so_san_pham > 10):
#             giam_gia = giam_gia + 10
        
#         #3. Giảm giá theo số tiền khách mua
#         if (tong_gia_tri >= 10000 and tong_gia_tri <= 50000 ):
#             giam_gia += 8
#         elif(tong_gia_tri > 50000):
#             giam_gia += 15
    
#     #Tinh tien sau khi giam:
#     #Dùng round để chỉnh dấu thập phân
#     tien_phai_tra = tong_gia_tri *(1- (giam_gia / 100))
#     return round(tien_phai_tra,2)

# #Nhap gia tri
# loai_khach_hang = input("Khach hang mới/cũ: ")
# so_san_pham = int(input("So san pham mua: "))
# tong_gia_tri = float(input("Tổng giá trị: "))

# #Xuat ra số tiền sau khi được giảm
# tong_tien = tinh_tong_tien(loai_khach_hang, so_san_pham, tong_gia_tri)
# print(f'Tong tien phai tra:{tong_tien}VND')




                    #BAI 6 : KIEM TRA CHIEU CAO (k dung if else and max)
                #input: An 180, Linh 165, Duc 175, Nam 155.5
                #output: An

#dùng split để phân cách 2 giá trị nhập vào
An,cao_An = input("Nhap chieu cao cua An: ").split()
Linh,cao_Linh = input("Nhap chieu cao cua Linh: ").split()
Duc,cao_Duc = input("Nhap chieu cao cua Duc: ").split()
Nam,cao_Nam = input("Nhap chieu cao cua Nam: ").split()

#ép kiểu cho chiều cao từng bạn
cao_An = float(cao_An)
cao_Linh = float(cao_Linh)
cao_Duc = float(cao_Duc)
cao_Nam = float(cao_Nam)

#So sanh ai la nguoi cao nhat
An_cao_nhat = (cao_An > cao_Linh) and (cao_An > cao_Duc) and (cao_An > cao_Nam)
Linh_cao_nhat = (cao_Linh > cao_An) and (cao_Linh > cao_Duc) and (cao_Linh > cao_Nam)
Duc_cao_nhat = (cao_Duc > cao_An)  and (cao_Duc > cao_Linh) and (cao_Duc > cao_Nam)
Nam_cao_nhat = (cao_Nam > cao_An) and (cao_Nam > cao_Linh) and (cao_Nam > cao_Duc)

#Chọn 1 trong 3 người cao nhất
cao_nhat_lop = (An_cao_nhat and An) or (Linh_cao_nhat and Linh) or (Duc_cao_nhat and Duc) or (Nam_cao_nhat and Nam)
print(f'Ban {cao_nhat_lop} cao nhat')