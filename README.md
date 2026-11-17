# Phần Mềm Tra Cứu Phi Tròng Tối Đa (Lab Rx Matrix Checker)

Hệ thống hỗ trợ kỹ thuật viên và nhân viên tư vấn khúc xạ kiểm tra khả năng sản xuất và **đường kính phôi tối đa (Phi tròng lớn nhất)** theo từng toa kính (SPH / CYL) theo thời gian thực.

---

## 1. Cách mở và sử dụng
- **Truy cập Localhost:** [http://localhost:3000](http://localhost:3000)
- **Hoặc chạy trực tiếp:** Bạn có thể **click đúp vào file `index.html`** trên bất kỳ máy tính nào mà không cần cài web server.

---

## 2. Danh mục tròng kính đã số hóa

### A. SV VIP 1.67 (Mã `05587 : Aspherique_Mr7_SF`)
* **Vật liệu:** Chiết suất 1.67 MR-7, Đơn tròng phi cầu Semi-Finished.
* **Dải đo:**
  * Độ cầu (SPH): Từ `+8.00` đến `-16.00 D`
  * Độ loạn (CYL): Từ `0.00` đến `-6.00 D`
* **Quy ước Phi tối đa:**
  * 🌸 **Hồng (Magenta):** Phi tối đa **Ø80** (vùng rộng nhất)
  * 🟣 **Tím (Purple):** Phi tối đa **Ø75**
  * 🔵 **Xanh dương (Blue):** Phi tối đa **Ø70**
  * 🟢 **Xanh lá (Green):** Phi tối đa **Ø65**
  * 🟠 **Cam (Orange):** Phi tối đa **Ø60**
  * 🔴 **Đỏ (Red):** Phi tối đa **Ø55**

### B. SV VIP 1.60 (Mã `00466 : Aspherique_MR8_SF_Extended`)
* **Vật liệu:** Chiết suất 1.60 MR-8, Đơn tròng phi cầu Semi-Finished Extended.
* **Dải đo:**
  * Độ cầu (SPH): Từ `+10.00` đến `-13.00 D`
  * Độ loạn (CYL): Từ `0.00` đến `-6.00 D`
* **Quy ước Phi tối đa:**
  * 🟣 **Tím (Purple):** Phi tối đa **Ø75** (vùng rộng nhất)
  * 🔵 **Xanh dương (Blue):** Phi tối đa **Ø70**
  * 🟢 **Xanh lá (Green):** Phi tối đa **Ø65**
  * 🌸 **Hồng (Magenta):** Phi tối đa **Ø60** (vùng viễn cao + loạn cao)

---

## 3. Cấu trúc thư mục
```
ODS/
├── index.html                   # Giao diện chính (Real-time Live Checker)
├── data/
│   ├── sv_vip_167.js & .json    # Dữ liệu phôi 1.67
│   └── sv_vip_160.js & .json    # Dữ liệu phôi 1.60
├── docs/
│   ├── catalog_05587_matrix.jpg # Ảnh ma trận gốc 1.67
│   ├── catalog_00466_matrix.jpg # Ảnh ma trận gốc 1.60
│   └── ...
├── tests/
│   └── test_matrix.py           # Unit test tự động kiểm thử toàn bộ dữ liệu
└── README.md
```
