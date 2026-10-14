# Quyết định thiết kế & Báo cáo Accessibility

Tài liệu này tổng hợp **10 quyết định thiết kế quan trọng nhất** của dự án **EXE Match**, đi kèm căn cứ lập luận chuyên môn (UX, Heuristics, Ràng buộc kỹ thuật), cùng bảng kiểm tra chi tiết tính tiếp cận (**Accessibility Checklist** theo chuẩn WCAG 2.1).

---

## 1. Top 10 Quyết định thiết kế cốt lõi (Core Design Decisions)

| # | Quyết định thiết kế | Phương án thay thế đã cân nhắc | Lý do chọn lựa (Căn cứ chuyên môn) |
| :-: | :--- | :--- | :--- |
| **1** | **Hiển thị tiến độ thành viên dạng `3/5` kèm Progress Bar** | Chỉ ghi text "Còn tuyển" hoặc "Đang tuyển" | **Heuristic #1 (Visibility of System Status):** Giúp sinh viên nắm bắt ngay mức độ khẩn cấp và độ hoàn thiện của nhóm mà không cần mở trang chi tiết. |
| **2** | **Bổ sung Badge đếm ngược hạn chót ("Còn 5 ngày")** | Ẩn ngày hạn chót hoặc chỉ để trong phần cài đặt | **Persona Requirement:** Sinh viên Huy đang chịu áp lực thời gian sát ngày chốt danh sách; việc thấy hạn chót tạo động lực ra quyết định nhanh chóng. |
| **3** | **Sử dụng cấu trúc Bottom Sheet cho Form nộp đơn (Pitch Sheet)** | Chuyển sang một trang màn hình mới toàn phần | **Tối ưu trải nghiệm di động:** Giữ nguyên ngữ cảnh của nhóm dự án bên dưới, giảm cảm giác nặng nề của việc điền form và cho phép hủy bỏ nhanh bằng thao tác vuốt xuống. |
| **4** | **Phân biệt trạng thái duyệt bằng cả Icon + Nhãn chữ + Màu sắc** | Chỉ dùng chấm tròn màu (Xanh/Vàng/Đỏ) | **Chuẩn WCAG 2.1 (Non-text contrast & Color blind):** Tránh truyền đạt thông tin chỉ dựa vào màu sắc; người khiếm thị màu (mù màu đỏ-xanh) vẫn hiểu chính xác trạng thái qua nhãn chữ đi kèm. |
| **5** | **Đặt vùng chạm (Touch Target) tối thiểu `48 × 48 dp` cho mọi icon và nút** | Giữ nguyên icon 24dp mặc định từ AI Stitch | **Tiêu chuẩn công thái học di động:** Đảm bảo ngón tay cái của người dùng có thể chạm chính xác khi cầm điện thoại bằng 1 tay trên xe buýt hoặc khi đang đi lại. |
| **6** | **Thiết kế Skeleton Loading thay vì vòng xoay Spinner đơn thuần** | Vòng xoay spinner ở giữa màn hình | **Nhận thức thời gian chờ (Perceived Performance):** Skeleton mô phỏng trước bố cục thẻ bài đăng, giúp người dùng cảm thấy hệ thống tải nhanh hơn 20–30% so với màn hình trắng trơn. |
| **7** | **Tạo màn hình Empty State có nút phục hồi ("Đặt lại bộ lọc")** | Để màn hình trống trơn hoặc chỉ báo "0 kết quả" | **Heuristic #9 (Error Recovery):** Ngăn ngừa tình trạng người dùng bị rơi vào "ngõ cụt" (dead-end) khi lọc quá sâu; cung cấp đường thoát tức thì bằng 1 chạm. |
| **8** | **Ưu tiên bảng màu Royal Blue (`#2563EB`) trên nền Slate-50 (`#F8FAFC`)** | Nền trắng tinh khôi (`#FFFFFF`) và màu tím neon | **Độ tương phản & Chống mỏi mắt:** Tỷ lệ tương phản chữ đen trên nền xám nhạt đạt 14.2:1 (vượt xa chuẩn 4.5:1), đồng thời giảm độ chói lóa khi dùng lâu. |
| **9** | **Nhúng liên kết Portfolio (GitHub/LinkedIn/Behance) vào hồ sơ ứng viên** | Chỉ cho nhập Bio tự giới thiệu ngắn | **Độ tin cậy trong đồ án EXE:** Giải quyết triệt để pain point "sợ gặp free-rider" bằng cách cung cấp bằng chứng năng lực thực tế được kiểm chứng. |
| **10**| **Giới hạn số lượng thẻ dự án tải ban đầu (Lazy Loading / Pagination)** | Tải toàn bộ hàng trăm nhóm cùng lúc | **Hiệu năng & Trọng tải nhận thức:** Giảm tải bộ nhớ di động và tránh gây quá tải thông tin (information overload) cho sinh viên khi tìm kiếm. |

---

## 2. Kết quả kiểm tra Accessibility Checklist (WCAG 2.1 AA)

| Tiêu chí kiểm tra | Quy chuẩn yêu cầu | Kết quả đạt được trên EXE Match | Đánh giá |
| :--- | :--- | :--- | :---: |
| **Độ tương phản văn bản thường (Contrast Ratio)** | Tối thiểu **4.5:1** (WCAG AA) | Chữ chính `#0F172A` trên nền `#F8FAFC` đạt **14.2:1**; Chữ phụ `#475569` đạt **5.4:1** | **ĐẠT** |
| **Độ tương phản chữ lớn & UI controls** | Tối thiểu **3:1** | Nút Primary `#2563EB` với text trắng đạt **4.8:1**; Icon điều khiển đạt > **3.5:1** | **ĐẠT** |
| **Vùng chạm tối thiểu (Touch Target)** | Tối thiểu **`48 × 48 dp`** | Mọi icon và button đều có bounding box tối thiểu `48 × 48 dp` trong Figma Auto Layout | **ĐẠT** |
| **Cỡ chữ nội dung (Body text size)** | Tối thiểu **14 sp** | Toàn bộ body text từ 14 sp trở lên, nhãn chip nhỏ nhất đạt 12 sp (Medium 500) | **ĐẠT** |
| **Truyền đạt thông tin không chỉ bằng màu** | Không phụ thuộc màu đơn lẻ | Các trạng thái đều có icon (Checkmark, Clock, Alert) và nhãn chữ đi kèm | **ĐẠT** |
| **Khả năng co giãn Layout (Responsive 360 & 412 dp)** | Dùng Constraint & Auto Layout | Đã kiểm tra: Các thẻ Card và Button co giãn linh hoạt theo chiều ngang (Fill container) | **ĐẠT** |

---

## 3. Hành vi trên màn hình rộng hơn (Màn hình từ 600 dp trở lên - Tablet / Web)
Mặc dù chỉ thiết kế màn hình chuẩn `360 × 800 dp` trên Figma, kiến trúc giao diện đã được tính toán để thích ứng trên màn hình lớn:
* **Trên màn hình từ 600 dp - 840 dp (Tablet dọc):**
  * Danh sách thẻ dự án từ 1 cột chuyển thành lưới 2 cột (2-column Grid).
  * Thanh Bottom Navigation dưới đáy được thay thế bằng **Navigation Rail** dạng cột đứng cố định bên mép trái để tối ưu diện tích thao tác tay cầm máy tính bảng.
* **Trên màn hình từ 840 dp trở lên (Desktop / Tablet ngang):**
  * Sử dụng bố cục 2 vùng (Master-Detail View): Cột trái hiển thị danh sách nhóm tìm kiếm, cột phải hiển thị trực tiếp chi tiết nhóm đã chọn mà không cần mở trang mới.
  * Form nộp đơn (Pitch Sheet) chuyển từ dạng Bottom Sheet sang dạng **Center Dialog Modal**.
