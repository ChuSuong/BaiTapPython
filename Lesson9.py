                #BAI 9: FUNCTION

#                 #Bai 1: 
# def say_hello():
#     print("Hello, World!")

# say_hello()


#                 #Bài 2:

# def generate_laugh(n):
#     return "Ha" * n

# n = int(input("Nhập số lần lặp: "))
# print(generate_laugh(n))

#                 #Bai 3: CHECK INT NUMBER

# def is_int(value):
#     return isinstance(value, int)

# def tinh_tong(n1, n2):
#     if is_int(n1) and is_int(n2):
#         return n1 + n2
#     else:
#         return " Cả 2 gtri không phải là số nguyên"

# try: 
#     n1 = int(input("Nhập n1: "))
#     n2 = int(input("Nhập n2: "))
#     print(tinh_tong(n1,n2))
# except ValueError:
#     print("Vui lòng nhập số nguyên hợp lệ")


                #BAI 4: GIA KHUYEN MAI

# def chia_khuyen_mai(gia_moi, phan_tram_khuyen_mai):
#     gia_sau_khuyen_mai = gia_moi * (1 - phan_tram_khuyen_mai/100)
#     return gia_sau_khuyen_mai

# gia_moi = int(input("Nhập giá mới:"))
# phan_tram_khuyen_mai = int(input("Nhập phần trăm khuyến mãi: "))

# price = chia_khuyen_mai(gia_moi, phan_tram_khuyen_mai)
# print(f'Giá sau khi khuyến mãi là: {int(price)}')


                #BAI 5: TIM SO CHAN
# def tim_cac_so_chan(n):
#     for i in range(n+1):
#         if i % 2 == 0:
#             print(i,end=' ')

# n = int(input("Nhập số nguyên dương n: "))
# tim_cac_so_chan(n)


                    #BAI 6: ĐẾM CHUỖI
# def dem_tu_trong_chuoi(str):
#     # count = 0
#     # for i in str:
#     #     count = count + 1
#     # return count
#     return len(str) #Có thể dùng len để xét độ dài của chuỗi khi đã được tách

# str = (input("Nhập chuỗi: ")).split() #Nhập chuỗi và tách
# dem = dem_tu_trong_chuoi(str)
# print (f'Số từ trong chuỗi: {dem}')


                    #BAI 7: FIBONACCI
def tinh_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return[0]
    
    fibonacci = [0,1]
    for i in range (2, n):
        next_fib = fibonacci[-1] + fibonacci[-2] #bằng tổng 2 số trc nó
        fibonacci.append(next_fib)

    return fibonacci
        
n = int(input("Nhập n số đầu tiên: "))
list_fib = tinh_fibonacci(n)
print(f"Dãy các số fibonacci: {list_fib}")