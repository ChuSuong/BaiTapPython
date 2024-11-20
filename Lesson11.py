#                     #BÀI TẬP : OOP


#             # Bài 1: Phiếu Hàng Hóa

# #Phân tích:
# #   - 1. Thông tin chi tiết: Mã phiếu, Ngày lập, Mã NCC, Tên NCC, Địa Chỉ
# #   - 2. Thông tin hàng hóa: Tên hàng, Đơn giá, Số lượng, Thành tiền
# #   - 3. Tổng cộng: Tổng tirnf tất cả giá trị hàng hóa

# class ChiTiet:
#     #1. Khởi tạo đối tượng của lớp ChiTiet
#     def __init__(self, tenPhieu, maPhieu, ngayLap, maNCC, tenNCC, diaChi):
#         self.tenPhieu = tenPhieu
#         self.maPhieu = maPhieu
#         self.ngayLap = ngayLap
#         self.maNCC = maNCC
#         self.tenNCC = tenNCC
#         self.diaChi = diaChi

#     #Gán các giá trị cho thuộc tính của đối tượng, hiển thị thông tin của đối tượng 
#     def __str__(self):
#         return(
#             f"{self.tenPhieu:>30}\n"
#             f"Mã phiếu: {self.maPhieu}     Ngày lập: {self.ngayLap}\n"
#             # f'Ngày lập : {self.ngayLap}\n'
#             f"Mã NCC: {self.maNCC}         Tên NCC: {self.tenNCC}\n"
#             # f'Tên NCC : {self.tenNCC}\n'
#             f'Địa chỉ: {self.diaChi}\n'
#         )

# class Hang:
#     #2. Quản lý thông tin từng mặt hàng
#     def __init__(self, tenHang, donGia, soLuong):
#         self.tenHang = tenHang
#         self.donGia = donGia
#         self.soLuong = soLuong
#         self.thanhTien = self.soLuong * self.donGia

#     #Thiết kế cách hiển thoị thông tin của từng hàng hóa, :<10 canh trái và dành 10 ký tự
#     def __str__(self):
#         return(
#             f'{self.tenHang: <10}{self.donGia: <10}{self.soLuong: <10}{self.thanhTien:<10.1f}'
#         )
#         #:.1f : hiển thị gtri dạng float với 1 chữ số thập phân

# class PhieuNhapHang:
#     #3. Quản lý toàn bộ phiếu
#     def __init__(self, thong_tin):
#         self.thong_tin = thong_tin
#         self.danhSach = []  #Tạo list rỗng để chứa các thuộc tính

#     def them_hang(self, themhang):
#         self.danhSach.append(themhang) #Thêm các phần tử vào list trên

#     def tinhTien(self): #Dùng vòng for duyệt từng đối tượng hang và cộng lại 
#         return sum(hang.thanhTien for hang in self.danhSach)

#     def __str__(self):
#         title = f"{'Tên hàng':<10} {'Đơn Giá':<10} {'Số Lượng':<10} {'Thành Tiền':<10}\n "
#         hangHoa = "\n".join(str(hang) for hang in self.danhSach)
#         tongTien = self.tinhTien()
#         return(
#             f"{self.thong_tin}\n"
#             f"{title}"
#             f"{hangHoa}\n"
#             f"{'Cộng thành tiền':>30} {tongTien:<10.2f}\n"
#         )

# from Lesson11 import ChiTiet, Hang, PhieuNhapHang 
# #Tạo thông tin của phiếu
# thong_tin = ChiTiet(
#     tenPhieu= 'PHIẾU NHẬP HÀNG',
#     maPhieu= 'PH001.',
#     ngayLap= '1/1/2007',
#     maNCC= 'NCC1',
#     tenNCC= 'LG-Electronic',
#     diaChi= 'Khu công nghiệp Như Quỳnh A'
# )

# #Tạo phiếu nhập hàng
# phieu = PhieuNhapHang(thong_tin)
# phieu.them_hang(Hang("TiVi", 30, 2))
# phieu.them_hang(Hang("Quạt", 1.2, 3))
# phieu.them_hang(Hang("Mobi", 5, 10))

# #In phiếu ra màn hình
# print(phieu)


                        #BAI 2: Quản lý Sách
class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    #1. Title 
    @property   #Getter cho title
    def title(self):
        return self.__title

    @title.setter   #Setter cho title
    def title(self, value):
        self.__title = value    

    #2. Author
    @property       #Getter cho author
    def author(self):
        return self.__author

    @author.setter  
    def author(self, value):
        self.__author = value

    #3. Price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError
        self.__price = value


    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Price: {self.price}\n"
        )

class SoftCoverBook(Book):
    def __init__(self, title, author, price, discount):
        super().__init__(title, author, price)
        self.__discount = discount

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        if not (value >= 0 and value <= 100):
            raise ValueError
        self.__discount = value

    
    def calculate_discounted_price(self):
        discounted_price = self.price * (1- self.discount/100)
        return discounted_price

    def __str__(self):
        return (
            f"{super().__str__()}\n Discount: {self.discount}%\n"
            f"Discounted Price: {self.calculate_discounted_price()}"
        )


class HardCoverBook(Book):
    def __init__(self, title, author, price, weight):
        super().__init__(title, author, price)
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,value):
        if value <= 0:
            raise ValueError
        self.__weight = value
    
    def calculate_shipping_cost(self):
        shipping_cost = self.weight * 15000
        return shipping_cost

    def __str__(self):
        shipping_cost = self.calculate_shipping_cost()
        return (
            f"{super().__str__()} Weight: {self.weight}kg\n"
            f"Shipping cost: {shipping_cost}"
        )
    
class BookStore:
    def __init__(self):
        self.__books = []

    @property
    def books(self):
        return self.__books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self,title):
        self.books = [book for book in self.__books if book.title != title]
    
    def total_revenue(self):
        return sum(book.price for book in self.__books)

    def __str__(self):
        if not self.__books:
            return "Bookstore is empty."
        return "\n".join(str(book) for book in self.__books)



# Thử nghiệm
if __name__ == "__main__":
    # Tạo đối tượng sách
    soft_cover = SoftCoverBook("Python", "John Doe", 300, 5)
    hard_cover = HardCoverBook("Advanced Python", "Jane Doe", 500, 1.5)

    # Tạo cửa hàng sách
    bookstore = BookStore()
    bookstore.add_book(soft_cover)
    bookstore.add_book(hard_cover)

    # Hiển thị thông tin sách
    print("Bookstore inventory:")
    print(bookstore)

    # Tính toán các thông tin liên quan
    print("\nCalculations:")
    print(f"Soft Cover Book Discounted Price: {soft_cover.calculate_discounted_price():.1f}")
    print(f"Hard Cover Book Shipping Cost: {hard_cover.calculate_shipping_cost():,.1f}")
    print(f"Total Revenue: {bookstore.total_revenue():,.2f}")
    
        

        
        