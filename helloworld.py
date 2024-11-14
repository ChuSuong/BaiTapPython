# # # #In ra chữ "Hello World!"
# # # print('hello world !')

# # # #Khoi tạo 1 biến
# # # ten = 'suong'
# # # tuoi = 17
# # # PI = 3.14

# # # #in ra kiểu dữ liệu của biến
# # # ten, tuoi, PI = 'suong', 17, 3.14
# # # print(ten, tuoi, PI)
# # # print(type (ten))
# # # print(type (tuoi))
# # # print(type (PI))

# # #int
# # #Gán cho a = 4 và in ra kiểu dữ liệu của a <int>
# # a = 4
# # print(type(a))

# # #float
# # #Gán cho b = 1.23 và in ra kiểu dữ liệu của b <float>
# # b = 1.23 
# # print(type(b))

# # #Decimal
# # #Lấy toàn bộ nội dung của thư viện decimal
# # from decimal import*
# # #Lấy tối đa 30 chứ số phần nguyên và phần thập phân Decimal
# # getcontext().prec = 30
# # d = Decimal(10)/Decimal(3)
# # print(d)
# # print(type(d))

# # #Phân số: Fraction
# # from fractions import*
# # frac1 = Fraction(1,4)
# # frac2 = Fraction(3,9)
# # frac3 = Fraction(3,4)
# # frac4 = frac1 + frac2 + frac3
# # print(frac4)
# # print(type(frac4))

# # #Số phức: complex
# # #Ví dụ: gán biến c với số phức 1 + 3j. In ra c, in ra phần thực và phần ảo củ c
# # c = complex(1,3)
# # print(c)
# # print(c.real)   #Phần thực
# # print(c.imag)   #Phần ảo
# # print(type(c))  #kiểu dữ liệu

# # #Toán tử
# # e = 10
# # g = 4
# # h1 = e + g
# # h2 = e -g
# # h3 = e * g
# # h4 = e / g
# # h5 = e // g
# # h6 = e % g
# # h7 = e ** g
# # print(h1, h2, h3, h4, h5, h6, h7)

# # #Thư viện Math
# # import math
# # x = 10.3
# # y = 5
# # k1 = math.trunc(x)
# # k2 = math.floor(x)
# # k3 = math.ceil (x)
# # k4 = math.fabs(x)
# # k5 = math.sqrt(x)

# # print(k1, k2, k3, k4, k5)

# # #KIEU CHUOI
# # #PHAN 1
# # strA = "Hello  World!"
# # print(strA)
# # print(type(strA))
# # print('\'')
# #PHAN 2

# strA = 'o'
# strB = "Hello World!"
# strC = strA +" "+  strB
# strC = strC * (-1)
# strD = strA in strB
# strE = strB[None:None:-1 ]
# #đổi chữ 'e'  thành 'E'
# strF = strB[None:1] + "E" + strB[2:None] 
# # print(strC)
# # print(strD)
# print(strE)
# print(strF)

# #Định dạng bằng chuỗi f(f-string)
# name = 'Lab'
# address = 'Ha Noi'
# phone = '012345'
# result = f'Student: {name} \nAddress: {address}\nPhone: {phone}'
# print(result)
# print("\n")
# name = 'Csuong'
# g = '{:*^10}'.format(name) 
# print(g)

# Name = str(input("Họ và tên: "))
# Age = int(input("Tuổi: "))
# Gender= str(input("Giới tính Nam/Nữ:"))
# MaritalStatus = input("Tình trạng hôn nhân (Độc thân/ Đã kết hôn):")

# row_1 = '+ {:-<10} + {:-^15}+ {:-^15} + {:->10} +'.format('','','','')
# row_2 = '| {:<10} | {:^15} | {:^15} |{:>10} |'.format('Họ tên', 'Tuổi', 'Giới tính','Hôn nhân')
# row_3 = '| {:<10} | {:^15} | {:^15} |  {:>10} |'.format(Name,Age,Gender,MaritalStatus)
# row_5 = '+ {:-<10} + {:-^15} + {:-^15} + {:->10} +'.format('','','','')
# result = f'{row_1}\n{row_2}\n{row_3}\n{row_5}'
# print(result)

#Các phương thức biến đổi
#1. chữ hoa đầu : .capitalize()
# strQ = 'Hello World!'
# strH = strQ.capitalize()
# strK = strQ.center(20,'*')
# print(strH)
# print(strK)

# #Phương thức encode - decode
# strA = 'Chu Thị Sương'
# strB = strA.encode(encoding = 'utf-8', errors = 'strict')
# #Nối
# strC = strA.join(['1','2','3'])
# print(strB)
# print(strC)
# #Thay thế
# StrD = strA.replace('Thị', 'Ngọc')
# #Cắt
# strE = strA.strip('C')
# print(StrD)
# print(strE)
# #Tách 
# m = 'What&your&name'
# strF = m.rsplit('&', -2)
# print(strF)
# strW = m.find('a')
# print(strW)
# strQ = m.rfind('a')
# print(strQ)


#KIỂU LIST

## 1. Giới thiệu về list trong Python
    #Giới hạn bởi cặp ngoặc vuông []
    #Các phần tử của list cachs nhau bởi dấu phẩy
a = [1,3,4]
print(a)
    #List có khả năng chứa mọi giá trị đối tượng của python
    #bao gồm cả nó
b = [[[1,2,3], [4, 5, 6]], [['Hello Word!'], ["Xin chào!"]]]
print (b)

## 2. Khởi tạo 

    #Sử dụng cặp dấu []
c = [1,  3, 5, 'Hello!']
print (c)
empty_list = [] #Khới tạo list rỗng
print(empty_list)

    #Sử dụng list Comprehension
d = [suong for suong in range(0,3)]
print (d)
another_list = [[n, n*1, n*2] for n in range (0,3)]
print(another_list)

    #Sử dụng constructor list: list(iterable)
e = list([1, 2, 3])
print(e)
f = list('Suong')
print(f)
    # g = list(1) -> Không thể dùng int vì nó k phải là 1 iterable
    # print(g)

    #Sử dụng toán tử
    #Cộng
list1 = [1,2,3]
list1 += ['one', 'two']
print(list1)
 #list + chuỗi được, chuỗi + list là không
list1 += 'abc'
print(list1 )

    #Nhân : list * số -> gấp số lần
list2 = [1,4,5]
list2 *= 2  #gấp 2 lần
print(list2)

    #in : trả về True / False
list3 = [1,6,7]
k = 6 in list3
l = 'Suong' in list3
print(k)
print(l)

    #indexing và cắt list
list4 = [1, 2, 'a', 'b', [3, 4]]
a1 = list4[0:3:1]
a2 = list4[0:3:-1]
a3 = list4[0:3]
a4 = list4[3]
a5 = list4[:3]
a6 = list4[3:]
a7 = list4[::-1]
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)

    #Thay đổi nội dung trong List
list5 = [1, 4, 10]
list5[1] = 2
print(list5)

    #MA TRẬN
list6 = [[1, 2, 3], [2, 4, 5]]
newlist1 = list6[0][:2]
newlist2 = list6[1]
print(newlist1)
print(newlist2)

#3. Các phương thức tiện ích

    #Phương thức count
list7 = [1,3,1,5,6]
count = list7.count(1)
print(list7)
print(count)

    #Phương thức index
list8 = [1,3,5,7,9]
index = list8.index(7)
print(index)

    #Phương thức copy: có thẻ dùng số hoặc dùng str đều dk
list9 = [1,3,5,7,10]
copy = list9.copy()
print(copy)
copy[0] = 2     #trỏ tại vị trí nào đó 1 gtri mới, kqua sẽ thay đổi ở vị trí đó
print(copy)

    #Phương thức clear
list10 = [1,2,3,4,5]
list10.clear()
print(list10)


    #Phương thức append: không được append một list vào chính nó, vì sẽ tạo vòng lặp vô tận
list11 = [1,2,3,4,5,6]
list11.append(119)
list11.append([4,5]) 
print(list11)

    #Phương thức extend: khác với append
list12 = [1,2,3]
list12.extend([4,5])
list12.extend([[6,7], 8])
print(list12)

    #Phương thức insert
list13 = [7,8,9]
list13.insert(1,12) #[7,12,8,9] 
list13.insert(4,20) #Chèn vào vị trí 4 ptu 20: [7,12,8,9,20]
list13.insert(len(list13),50) #chèn vào vị trí 5(lúc này có 5ptu) ptu 50
print(list13)

    #Phương thức pop
list14 = [1,4,5,6,7,8]
list14.pop()
print(list14)

    #Phương thức sort
list19 = ['This', 'is', 'my', 'Laptop']
#Tạo 1 bản sao list19
list19_copy = list19.copy()
#Lọc bản cũ
list19.sort()
#Lọc bản copy theo key = len (độ dài của chuỗi)
list19_copy.sort(key=len)
print(list19)
print(list19_copy)

list20 = ['a', 1, 2, 'b', 'c']
list20.sort(key = str, reverse = True)
print(list20)

    #Su khac nhau giua hash object va unhash object
    #Hash object
s1 = 'Hello!'
s2 = 'My name is Suong.'
print(id(s1)) #1677994532176
print(id(s2)) #1677994538736
s1 = s1 + 'python'
s2 += 'python'
print(id(s1)) #1677994573104   => Co su thay doi
print(id(s2))  #1677994539312

    #Unhash object
list_1 = [1,2]
list_2 = [3,4]
print(id(list_1)) #2399464406344
print(id(list_2)) #2399464406536
list_1 = list_1 + [0]
list_2 += [0]
print(id(list_1)) #2399464406600
print(id(list_2)) #2399464406536


    #SET
set1 = {1,2,7,8}
check = 1 in set1
print(check)
set1.clear()
print(set1)
aq = {1, 2, 3, 4, 5}
bq = {2, 4, 5, 6}
cq = aq.union(bq)
print(cq)
set3= {1,2,3,6,7,8}
set3.remove(2)
print(set3)

q1 = {'1', 2, '3', 5, '5'}
q2= {'1', '3', '5'}
q3 = q2.issubset(q1)
print(q3)
        #DICT
f = [('ab'), ('cd')]
print(dict(f)) 

dic = {'name': 'Chu Suong', 'member': 69}
# print(dic)
# dic['name'] = 'Chu Thi Suong '
# dic['member'] = dic['member'] + 1
# print(dic)

    #Phương thức tiện ích get
dic2 = {'team': 'ChuSuong', (1, 2): 69}
value = dic2.get('ChuSuong', 'Chu Thi Suong')
print(value)

