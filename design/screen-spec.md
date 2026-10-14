# Đặc tả màn hình thiết kế (Screen Specification)

Tài liệu này mô tả chi tiết ý đồ thiết kế, nội dung hiển thị, và mối liên kết với User Flow cho toàn bộ **9 màn hình** của ứng dụng **EXE Match** (kích thước chuẩn `360 × 800 dp`).

---

## Danh mục màn hình & Ánh xạ Flow

| Mã màn hình | Tên màn hình | Mục đích chính | Thuộc Flow |
| :--- | :--- | :--- | :--- |
| **SCR-01** | Onboarding & Phân vai | Định hướng mục tiêu ban đầu của sinh viên | Khởi động |
| **SCR-02** | Khám phá (Discovery Feed) | Lướt danh sách các nhóm dự án EXE đang tuyển | Flow 1, Flow 3 |
| **SCR-03** | Bộ lọc nâng cao (Filter Modal) | Lọc sâu theo chuyên ngành, số giờ commit | Flow 1, Flow 3 |
| **SCR-04** | Chi tiết nhóm (Group Detail) | Xem thông tin dự án, slot trống, mentor | Flow 1, Flow 3 |
| **SCR-05** | Hồ sơ năng lực (Member Profile) | Xem hồ sơ ứng viên, skill matrix và link CV | Flow 2 |
| **SCR-06** | Form nộp đơn (Pitch Sheet) | Nhập lời giới thiệu bản thân và ứng tuyển | Flow 1 |
| **SCR-07** | Quản lý đơn (Request Management)| Theo dõi trạng thái đơn gửi đi & đơn apply đến | Flow 1, Flow 2 |
| **SCR-08** | Bảng điều khiển nhóm (Team Dashboard)| Không gian làm việc nhóm khi đã kết nạp đủ | Flow 2 |
| **SCR-09** | Thông báo (Notifications) | Nhận thông báo mời nhóm, duyệt đơn, deadline | Flow 2 |

---

## Đặc tả chi tiết từng màn hình

### 1. SCR-01: Onboarding & Lựa chọn vai trò (Role Selection)
* **Ý đồ thiết kế:** Giảm thiểu ma sát (friction) khi mới vào app, lập tức phân loại sinh viên thành 2 nhóm nhu cầu chính để hiển thị luồng trải nghiệm phù hợp nhất.
* **Nội dung hiển thị:**
  * Illustration sinh viên hợp tác khởi nghiệp.
  * Tiêu đề lớn: *"Khởi đầu dự án EXE cùng đồng đội lý tưởng"*.
  * Hai thẻ lựa chọn nổi bật:
    * Thẻ 1: *"Tôi đã có ý tưởng / Đang tìm thành viên"* (Dành cho Leader).
    * Thẻ 2: *"Tôi muốn gia nhập một nhóm dự án"* (Dành cho Member/Ứng viên).
  * Nút CTA chính: `"Bắt đầu ngay"`.

### 2. SCR-02: Trang chủ / Khám phá nhóm EXE (Discovery Feed)
* **Ý đồ thiết kế:** Màn hình trung tâm của Flow 1. Thiết kế theo dạng thẻ (Card-based) giúp lướt nhanh, dễ nắm bắt sĩ số thành viên còn thiếu và hạn chót nộp danh sách.
* **Nội dung hiển thị:**
  * **App Bar:** Avatar sinh viên (chạm để xem hồ sơ), tiêu đề "EXE Match", icon Thông báo (có badge chấm đỏ).
  * **Search & Quick Filter:** Thanh tìm kiếm dự án; các chip bộ lọc nhanh (`Tất cả`, `EdTech`, `FinTech`, `E-Commerce`, `Tiện ích`); nút mở bộ lọc nâng cao.
  * **Danh sách Card nhóm:**
    * Badge trạng thái: Tỷ lệ phù hợp (`96% Phù hợp`), Hạn chót còn lại (`Hạn chót: 5 ngày`).
    * Tên dự án: Ví dụ `EduConnect - AI Tutor`.
    * Tag vai trò còn thiếu (màu cam/xanh mềm): `Cần: Marketing Lead`, `Cần: Kế hoạch kinh doanh`.
    * Tiến độ thành viên: `3/5 thành viên` kèm avatar các thành viên hiện tại và progress bar.
    * Mức độ cam kết thời gian: `12 giờ/tuần`.
    * Nút hành động: Button `Xem chi tiết ->`, icon Bookmark lưu tin.
  * **Bottom Navigation Bar:** 4 tab: Khám phá (active), Đơn của tôi, Nhóm của tôi, Thông báo.

### 3. SCR-03: Modal Bộ lọc nâng cao & Bản đồ kỹ năng (Filter Modal)
* **Ý đồ thiết kế:** Mở dạng Bottom Sheet phủ lên SCR-02. Cho phép người dùng lọc chính xác nhóm theo ngành nghề để giải quyết pain point tìm người đa ngành.
* **Nội dung hiển thị:**
  * Header: Tiêu đề "Bộ lọc tìm nhóm", nút "Đặt lại" (Reset).
  * Nhóm 1 - Chuyên ngành cần tuyển: Checkbox/Chips chọn `Kinh tế / Quản trị`, `Marketing`, `Kỹ thuật phần mềm`, `Thiết kế đồ họa`.
  * Nhóm 2 - Lĩnh vực đề tài: `EdTech`, `FinTech`, `Bền vững / Môi trường`, `Thương mại điện tử`.
  * Nhóm 3 - Thời gian cam kết: Slider chọn từ `5 - 20 giờ/tuần`.
  * Nút bấm cố định dưới đáy: Button `"Áp dụng bộ lọc (Hiển thị 12 kết quả)"`.

### 4. SCR-04: Chi tiết nhóm dự án (Project / Group Detail)
* **Ý đồ thiết kế:** Cung cấp thông tin đầy đủ nhất để ứng viên quyết định có nộp đơn hay không.
* **Nội dung hiển thị:**
  * Top App Bar: Nút Back, Tiêu đề dự án, Nút Share và Bookmark.
  * Banner thông tin chung: Tên dự án, Lĩnh vực, Trạng thái (Đang phôi thai ý tưởng / Đã có MVP), Giảng viên hướng dẫn dự kiến.
  * Tiến độ sĩ số: Box nổi bật `3/5 Thành viên đã tham gia` (Cần tuyển thêm 2 vị trí).
  * Mô tả dự án (Problem & Solution): Đoạn văn ngắn 3-4 câu tóm tắt ý tưởng khởi nghiệp.
  * Danh sách thành viên hiện tại: Avatar, Tên, Chuyên ngành và Vai trò (ví dụ: Trần Minh - Leader/Tech, Nguyễn An - Design).
  * Các vị trí đang mở tuyển: Card nhỏ mô tả yêu cầu công việc cho vị trí `Marketing Lead`.
  * Nút CTA cố định dưới cùng: Button `"Xin gia nhập nhóm"` (luôn hiển thị nổi bật).

### 5. SCR-05: Hồ sơ năng lực thành viên (Member Profile & Skill Matrix)
* **Ý đồ thiết kế:** Nơi Leader xem và đánh giá năng lực của ứng viên trong Flow 2.
* **Nội dung hiển thị:**
  * Header: Avatar lớn, Họ tên, Chuyên ngành (Kỹ thuật phần mềm), Khóa (K16/K17).
  * Chỉ số tin cậy: Điểm đánh giá từ các môn đồ án trước (ví dụ: `4.9/5 ★ - Hoàn thành 100% deadline`).
  * Bản đồ kỹ năng (Skill Chips): Flutter, React Native, UI/UX, Git Workflow, Lập trình hướng đối tượng.
  * Các liên kết portfolio: Nút mở nhanh GitHub, LinkedIn, Behance, CV PDF.
  * Mức độ cam kết: Có thể dành `15 giờ/tuần`, rảnh các buổi tối và cuối tuần.
  * Thanh hành động dưới cùng (khi Leader xem): Nút Outlined `"Từ chối"`, Nút Filled `"Chấp nhận vào nhóm"`.

### 6. SCR-06: Form nộp đơn xin gia nhập (Apply / Pitch Sheet)
* **Ý đồ thiết kế:** Mở dạng Modal Bottom Sheet khi người dùng bấm "Xin gia nhập" ở SCR-04. Đơn giản hóa quá trình ứng tuyển trong dưới 3 thao tác.
* **Nội dung hiển thị:**
  * Tiêu đề: "Ứng tuyển vào nhóm EduConnect".
  * Lựa chọn vai trò ứng tuyển: Dropdown chọn `Technical Lead / Developer`.
  * Ô nhập liệu (Text Area): *"Giới thiệu ngắn về kinh nghiệm của bạn và lý do chọn đề tài này"* (Placeholder gợi ý rõ ràng, giới hạn 300 từ).
  * Đính kèm nhanh: Toggle `"Chia sẻ hồ sơ kỹ năng đầy đủ"`.
  * Nút CTA: Button `"Gửi đơn ứng tuyển"`.

### 7. SCR-07: Quản lý đơn & Yêu cầu ghép nhóm (Request Management)
* **Ý đồ thiết kế:** Giúp người dùng theo dõi mọi tương tác kết nối mà không bị thất lạc thông tin như trên Facebook.
* **Nội dung hiển thị:**
  * Tab 1: *"Đơn đã gửi (3)"* - Hiển thị danh sách các nhóm đã nộp kèm trạng thái (Badge xanh: `Đã duyệt`, Badge vàng: `Đang chờ`, Badge xám: `Bị từ chối`).
  * Tab 2: *"Yêu cầu cần duyệt (2)"* - Dành cho Leader, hiển thị danh sách các bạn xin vào nhóm kèm nút xem nhanh hồ sơ.
  * Trạng thái hoàn tác: Cho phép người dùng bấm `"Rút lại đơn"` nếu nhóm phản hồi quá lâu.

### 8. SCR-08: Bảng điều khiển nhóm chính thức (Team Workspace Dashboard)
* **Ý đồ thiết kế:** Màn hình đích của Flow 2 khi nhóm đã chốt đủ thành viên.
* **Nội dung hiển thị:**
  * Thẻ đếm ngược: *"Còn 2 ngày trước hạn chót nộp danh sách phòng Đào tạo"*.
  * Banner trạng thái: Badge xanh `"ĐÃ ĐỦ SĨ SỐ 5/5 THÀNH VIÊN"`.
  * Danh sách 5 thành viên chính thức kèm số điện thoại, tài khoản Zalo, vai trò cụ thể.
  * Nút hành động nhanh: `"Xuất file danh sách nhóm (PDF/Excel)"` và `"Tham gia nhóm Zalo nội bộ"`.

### 9. SCR-09: Thông báo (Notifications)
* **Ý đồ thiết kế:** Điểm kích hoạt (Trigger) cho Flow 2 khi có sự kiện mới.
* **Nội dung hiển thị:**
  * Bộ lọc thông báo: `Tất cả`, `Lời mời`, `Hệ thống`.
  * Thẻ thông báo: Icon chuông/người, Tiêu đề *"Lê Quốc Huy vừa gửi đơn xin gia nhập nhóm EduConnect"*, thời gian *"5 phút trước"*, nút bấm tắt *"Xem hồ sơ"*.
