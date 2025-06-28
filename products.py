import openpyxl
import os

# Hàm kiểm tra và tải/lưu file Excel
def initialize_workbook(file_name):
    if os.path.exists(file_name):
        wb = openpyxl.load_workbook(file_name)
        ws = wb.active
    else:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Product Information"
        headers = ["ID sản phẩm", "Tên sản phẩm", "Phí sản xuất", "Phí vận chuyển",
                   "Tỷ lệ lợi nhuận", "Giảm giá (%)", "Giá bán sản phẩm"]
        ws.append(headers)
    return wb, ws

# Nhập ID sản phẩm
def get_product_id():
    while True:
        pid = input("Nhập ID sản phẩm: ").strip()
        if pid:
            return pid
        print("ID không được để trống.")

# Nhập tên sản phẩm và chi phí
def get_product_info():
    while True:
        name = input("Tên sản phẩm: ").strip()
        if name:
            break
        print("Tên không được để trống.")

    while True:
        try:
            prod_cost = float(input("Phí sản xuất: "))
            if prod_cost >= 0:
                break
            print("Phí phải >= 0.")
        except:
            print("Vui lòng nhập số hợp lệ.")

    while True:
        try:
            ship_cost = float(input("Phí vận chuyển: "))
            if ship_cost >= 0:
                break
            print("Phí phải >= 0.")
        except:
            print("Vui lòng nhập số hợp lệ.")

    return name, prod_cost, ship_cost

# Nhập lợi nhuận
def get_profit_margin():
    while True:
        try:
            margin = float(input("Tỷ lệ lợi nhuận (ví dụ 0.2): "))
            if 0 < margin < 1:
                return margin
            print("Phải nằm trong khoảng 0 đến 1.")
        except:
            print("Vui lòng nhập số hợp lệ.")

# Nhập thông tin khuyến mãi
def get_discount():
    while True:
        try:
            option = int(input("Có khuyến mãi không? (0: Không, 1: Có): "))
            if option in [0, 1]:
                break
            print("Chỉ nhập 0 hoặc 1.")
        except:
            print("Vui lòng nhập số.")

    discount = 0
    if option == 1:
        while True:
            try:
                percent = int(input("Nhập % khuyến mãi (vd: 10, 20): "))
                if 0 < percent < 100:
                    discount = percent
                    break
                print("Phải từ 1 đến 99.")
            except:
                print("Vui lòng nhập số.")

    return discount

# Tính giá bán
def calculate_price(prod_cost, ship_cost, margin, discount_percent):
    base = (prod_cost + ship_cost) / (1 - margin)
    if discount_percent > 0:
        base *= (1 - discount_percent / 100)
    return round(base, 2)

# Hàm chính
def main():
    file_name = "product_info.xlsx"
    wb, ws = initialize_workbook(file_name)

    while True:
        print("\n--- Nhập sản phẩm mới ---")
        pid = get_product_id()
        name, prod_cost, ship_cost = get_product_info()
        margin = get_profit_margin()
        discount = get_discount()

        price = calculate_price(prod_cost, ship_cost, margin, discount)
        ws.append([pid, name, prod_cost, ship_cost, margin, discount, price])
        print(f"Đã tính xong giá bán: {price}")

        cont = input("Nhập sản phẩm tiếp? (y/n): ").strip().lower()
        if cont != 'y':
            break

    wb.save(file_name)
    print("Đã lưu file thành công.")

main()