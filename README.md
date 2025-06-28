# 🧾 Chương trình 1: Nhập Thông Tin Người Dùng (`user_information.py`)

## Tính năng
- Nhập: họ tên, ngày sinh, email, số điện thoại, công việc, tình trạng hôn nhân, sinh viên (y/n).
- Kiểm tra định dạng ngày, email, số điện thoại.
- Tính tuổi, phân loại "Trên 18"/"Dưới 18", gán mã trạng thái:
  - 1: Sinh viên
  - 2: Trên 18, thất nghiệp
  - 3: Trên 18, có việc
- Lưu dữ liệu vào `user_info.xlsx`.

## Cách chạy
```bash
python user_information.py
```

# 📦 Chương trình 2: Nhập Thông Tin Sản Phẩm (`products.py`)

## Tính năng
- Nhập: ID sản phẩm, tên sản phẩm, phí sản xuất, phí vận chuyển.
- Chọn loại hàng:
  - `0`: Không khuyến mãi  
  - `1`: Có khuyến mãi (nhập thêm % giảm giá)
- Nhập tỷ lệ lợi nhuận và tự động tính **giá bán sản phẩm** theo công thức:
  - `(phí sản xuất + phí vận chuyển) / (1 - tỷ lệ lợi nhuận)`
  - Nếu có khuyến mãi → trừ thêm phần trăm khuyến mãi
- Lưu thông tin vào file `products.xlsx`, với các cột:
  - ID sản phẩm, Tên sản phẩm, Phí sản xuất, Phí vận chuyển, Tỷ lệ lợi nhuận, Giá bán sản phẩm

## Cách chạy
```bash
python products_info.py

## 📧 Liên hệ
Võ Văn Minh Trí  
📩 vovanminhtri2002@gmail.com
