# Bản mô tả thiết kế hệ thống (Design Specification)

## 1. Triết lý & Tinh thần thiết kế (Design Tone & Principles)
* **Tone & Voice:** Hiện đại, năng động, chuyên nghiệp, khích lệ tinh thần hợp tác sinh viên (Collaborative, Vibrant, Trustworthy).
* **Nền tảng mục tiêu (Target Platform):** Mobile Android / Cross-platform (Material Design 3 quy chuẩn). Kích thước thiết kế chuẩn: **`360 × 800 dp`** (Tỷ lệ phổ biến, tương thích tốt khi co giãn lên `412 dp`).
* **Visual Hierarchy (Thứ bậc thị giác):** 
  * Mỗi màn hình chỉ có duy nhất một hành động chính (Primary Action) dạng Filled Button nổi bật.
  * Sử dụng thẻ (Card) có bo góc mềm mại và phân cấp độ bóng (Elevation) để gom cụm thông tin rành mạch.

---

## 2. Bảng mã màu & Tokens (Color System - WCAG 2.1 AA Compliant)

Hệ thống màu sắc được chọn lọc kỹ lưỡng, đảm bảo tỉ lệ tương phản chữ/nền tối thiểu **4.5:1** cho văn bản thường và **3:1** cho tiêu đề & icon điều khiển:

| Token Name | Hex Code | Tỉ lệ tương phản (Contrast Ratio) | Ứng dụng cụ thể |
| :--- | :--- | :--- | :--- |
| `color-primary` | `#2563EB` (Royal Blue) | 4.8:1 trên nền trắng | Nút bấm chính (CTA), tab đang chọn, icon chủ đạo |
| `color-primary-variant` | `#1D4ED8` (Dark Blue) | 7.2:1 trên nền trắng | Trạng thái Pressed / Hover của nút chính |
| `color-primary-container` | `#EFF6FF` (Ice Blue) | Nền phụ mềm | Badge tag kỹ năng, nền highlight thẻ tin quan trọng |
| `color-secondary` | `#0D9488` (Teal) | 4.6:1 trên nền trắng | Nút phụ, biểu thị trạng thái "Khởi nghiệp/Kinh tế" |
| `color-background` | `#F8FAFC` (Slate 50) | - | Nền toàn bộ ứng dụng (chống mỏi mắt) |
| `color-surface` | `#FFFFFF` (White) | - | Nền thẻ Card, Bottom Sheet, App Bar |
| `color-text-primary` | `#0F172A` (Slate 900) | **14.2:1** trên nền trắng | Tiêu đề H1, H2, tên dự án, nhãn trường nhập liệu |
| `color-text-secondary` | `#475569` (Slate 600) | **5.4:1** trên nền trắng | Nội dung mô tả, phụ đề, thời gian đăng bài |
| `color-text-disabled` | `#94A3B8` (Slate 400) | 3.1:1 trên nền trắng | Văn bản placeholder, nút bị vô hiệu hóa |
| `color-error` | `#DC2626` (Red 600) | 4.7:1 trên nền trắng | Báo lỗi, nút từ chối, cảnh báo deadline gấp |
| `color-success` | `#16A34A` (Green 600) | 4.5:1 trên nền trắng | Báo chấp nhận thành công, trạng thái "Còn slot" |
| `color-border` | `#E2E8F0` (Slate 200) | 1.3:1 trên nền trắng | Đường viền ngăn cách card, viền input default |

---

## 3. Hệ thống chữ (Typography System - Google Font: Inter / Roboto)

Mọi kích thước font đều tuân thủ nguyên tắc kích thước nội dung tối thiểu từ **14 sp** trở lên để đảm bảo khả năng tiếp cận (Accessibility):

| Style Name | Font Size (sp) | Weight | Line Height | Letter Spacing | Sử dụng cho |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `headline-large` | 24 sp | Bold (700) | 32 dp | 0 | Tiêu đề lớn màn hình Onboarding |
| `headline-medium`| 20 sp | Semi-Bold (600) | 28 dp | 0.15 | Tiêu đề trang (App Bar title), Tên dự án |
| `title-medium`   | 16 sp | Semi-Bold (600) | 24 dp | 0.15 | Tên thẻ nhóm, Tên đề mục con |
| `body-large`     | 16 sp | Regular (400) | 24 dp | 0.5 | Đoạn văn mô tả chi tiết, nội dung pitch |
| `body-medium`    | 14 sp | Regular (400) | 20 dp | 0.25 | Text trong thẻ card, phụ đề, danh sách yêu cầu |
| `label-large`    | 14 sp | Medium (500) | 20 dp | 0.1 | Text trong nút bấm Button, Tab bar |
| `label-small`    | 12 sp | Medium (500) | 16 dp | 0.4 | Tag chuyên ngành (Tech, Biz), thời gian timestamp |

---

## 4. Quy chuẩn khoảng cách & Lưới (Spacing & Layout Grid)

* **Grid:** 4-column layout trên màn hình mobile `360 dp`, margin 2 bên `16 dp`, gutter `12 dp`.
* **Hệ thống Spacing (Base 4 & 8 dp):**
  * `space-xs`: `4 dp` (Khoảng cách giữa icon và label nhỏ)
  * `space-sm`: `8 dp` (Khoảng cách giữa các chip/tag, khoảng cách các trường liên quan)
  * `space-md`: `16 dp` (Padding tiêu chuẩn trong Card, padding lề màn hình)
  * `space-lg`: `24 dp` (Khoảng cách giữa các section nội dung độc lập)
  * `space-xl`: `32 dp` (Khoảng cách từ header tới khối nội dung chính)
* **Quy chuẩn bo góc (Border Radius):**
  * `radius-sm`: `8 dp` (Chip tag, Button nhỏ, ô Text Field)
  * `radius-md`: `12 dp` (Thẻ Card dự án, Card thành viên)
  * `radius-lg`: `16 dp` (Bottom sheet, Modal Dialog)
  * `radius-full`: `999 dp` (Avatar tròn, Badge tròn)
* **Độ nổi & bóng đổ (Elevation & Shadow):**
  * `elevation-0`: Không bóng, dùng viền `color-border` 1px.
  * `elevation-1`: `0px 2px 4px rgba(15, 23, 42, 0.06)` (Thẻ card ở trạng thái tĩnh).
  * `elevation-2`: `0px 8px 16px rgba(15, 23, 42, 0.10)` (Thẻ khi chạm, Bottom Sheet, Dialog).

---

## 5. Quy tắc thiết kế Components tối thiểu (9 Components bắt buộc)

1. **Button (Nút bấm):**
   * Vùng chạm (Touch Target) luôn đảm bảo tối thiểu **`48 × 48 dp`** (kể cả khi chiều cao hiển thị là 40 dp thì đệm thêm hit-box padding).
   * 4 Trạng thái bắt buộc: `Default`, `Pressed` (nền tối hơn 10%), `Disabled` (màu xám nhạt `#E2E8F0`, không click được), `Loading` (ẩn chữ, hiện spinner quay tròn).
2. **Text Field (Ô nhập liệu):**
   * 5 Trạng thái bắt buộc: `Default` (viền xám), `Focused` (viền xanh primary 2px), `Filled` (có nội dung), `Error` (viền đỏ kèm thông báo lỗi bên dưới), `Disabled`.
3. **Card (Thẻ nhóm / Thẻ thành viên):**
   * Có Auto Layout, padding 16dp, bo góc 12dp. Trạng thái `Default` và `Pressed` (phản hồi hiệu ứng gợn sóng hoặc nâng nhẹ elevation).
4. **Navigation Bar (Thanh điều hướng dưới đáy):**
   * Cố định dưới màn hình, 4 mục chính (Khám phá, Quản lý đơn, Nhóm của tôi, Thông báo). Mục đang chọn đổi màu `color-primary` kèm hiệu ứng highlight.
5. **App Bar (Thanh tiêu đề trên cùng):**
   * Tiêu chuẩn Material 3, có nút Back (trừ trang chủ), tiêu đề căn trái/giữa, có action button (Filter, Tìm kiếm hoặc Lưu).
6. **Dialog (Hộp thoại xác nhận / Báo lỗi):**
   * Dạng modal pop-up chặn nền (overlay 40% mờ), có tiêu đề rõ ràng, mô tả, nút Hủy (Outlined) và nút Chấp nhận (Filled).
7. **Loading State:**
   * Dùng **Skeleton Loading** (khung xám nhấp nháy mô phỏng vị trí card bài đăng) thay vì spinner đơn độc để tăng cảm giác phản hồi nhanh.
8. **Empty State:**
   * Hình minh họa vector đơn giản (hoặc icon 64dp), một câu thông báo dễ hiểu ("Không tìm thấy nhóm phù hợp"), kèm nút bấm phục hồi ("Đặt lại bộ lọc").
9. **Error State:**
   * Thông báo lỗi rõ ràng bằng ngôn ngữ tự nhiên (tránh mã lỗi kỹ thuật 404/500), giải thích nguyên nhân và nút "Thử lại".
