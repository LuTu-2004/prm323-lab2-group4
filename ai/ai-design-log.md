# Nhật ký tương tác & Phản biện UI với AI (AI Design Log)

## 1. Thông tin tổng quan
* **Dự án:** EXE Match - Hệ thống quản lý ghép nhóm Khởi nghiệp sinh viên
* **Công cụ AI chính sử dụng:** Google Stitch (Prompt-to-UI), AI Assistant (Nielsen Heuristics UX Critique)
* **Kích thước thiết kế:** 360 × 800 dp (Mobile Android)

---

## 2. UI Ban đầu từ Google Stitch (Initial Generation)

### 2.1. Nguyên văn Prompt đưa vào Google Stitch
```text
Design a modern mobile app screen for 'EXE Match', a cross-disciplinary team matching app for university entrepreneurship students. Screen dimensions: 360x800 dp, Clean Material 3 style. Target user: 3rd-year Software Engineering student looking for Business and Marketing teammates. Screen 1 (Discovery Feed): Top app bar with search 'Search projects, skills...'; horizontal category chips: 'All', 'EdTech', 'FinTech', 'E-commerce'; a prominent filter button. Feed shows project cards. Each card displays: Project title (e.g. 'EduConnect - AI Tutor'), required roles badges ('Needs: Marketing Lead, Business Plan'), current vacancy status ('3/5 members filled'), time commitment ('12 hrs/week'), and a primary button 'View Details'. Clean color palette: Primary Royal Blue (#2563EB), surface white, background slate-50 (#F8FAFC), high contrast typography. Bottom navigation bar with 4 tabs: Explore, Applications, My Team, Notifications.
```

### 2.2. Kết quả nhận được từ Stitch
* **Ảnh minh chứng nhập Prompt:** [`assets/stitch/stitch_prompt_input_evidence.png`](../assets/stitch/stitch_prompt_input_evidence.png)
* **Ảnh Màn hình 1 (Discovery Feed):** [`assets/stitch/screen_01_discovery_feed.png`](../assets/stitch/screen_01_discovery_feed.png)
* **Ảnh Màn hình 2 (Group Detail - EduConnect):** [`assets/stitch/screen_02_project_detail.png`](../assets/stitch/screen_02_project_detail.png)
* **Ảnh Màn hình 3 (Apply as Co-Founder Form):** [`assets/stitch/screen_03_apply_sheet.png`](../assets/stitch/screen_03_apply_sheet.png)
* **Ảnh Màn hình 4 (Application Submitted):** [`assets/stitch/screen_04_application_submitted.png`](../assets/stitch/screen_04_application_submitted.png)
* **Ảnh Màn hình 5 (My Applications Tracker):** [`assets/stitch/screen_05_my_applications_tracker.png`](../assets/stitch/screen_05_my_applications_tracker.png)
* **Ảnh Màn hình 6 (Chemistry Call Modal):** [`assets/stitch/screen_06_chemistry_call_modal.png`](../assets/stitch/screen_06_chemistry_call_modal.png)
* **Ảnh Màn hình 7 (Chemistry Call Confirmed):** [`assets/stitch/screen_07_chemistry_call_confirmed.png`](../assets/stitch/screen_07_chemistry_call_confirmed.png)
* **Ảnh Màn hình 8 (Empty State & Recovery):** [`assets/stitch/screen_08_empty_state.png`](../assets/stitch/screen_08_empty_state.png)
* **Ảnh Canvas 8 màn hình hoàn chỉnh:** [`assets/stitch/figma_canvas_8_screens.png`](../assets/stitch/figma_canvas_8_screens.png)
* **Đánh giá ban đầu:** 
  * Đạt đủ trọn vẹn **8 màn hình độc lập** theo yêu cầu của đề tài.
  * Màn hình 8 (Empty State) cung cấp đầy đủ thông báo lỗi tìm kiếm, minh họa vector thân thiện, và nút CTA phục hồi nổi bật `Reset Filters` theo đúng Heuristic #9 và tiêu chuẩn Flow 3.

---

## 3. Phản biện UX bằng AI theo 10 Usability Heuristics của Nielsen

Hệ thống được đưa qua chuyên gia phản biện AI để rà soát theo bộ tiêu chuẩn **10 Heuristics của Nielsen Norman Group** và tiêu chuẩn tiếp cận **WCAG 2.1**:

### Phát hiện 1 (Heuristic #1: Visibility of System Status - Hiển thị trạng thái hệ thống)
* **Vấn đề trên UI Stitch:** Thanh đo lường thành viên `3/5 members filled` dùng thanh màu xanh nhưng không có nhãn số rõ ràng khi co nhỏ, và chưa thể hiện rõ *còn trống bao nhiêu vị trí và hạn nộp danh sách còn bao nhiêu ngày*.
* **Đề xuất từ AI:** Bổ sung badge nổi bật: `"Còn trống 2 vị trí"` và đồng hồ đếm ngược mini `"Hạn chót: 5 ngày"` ngay trên góc thẻ card.
* **Quyết định của sinh viên:** **CHẤP NHẬN**. Bổ sung vào bản Figma vì persona Lê Quốc Huy đang chịu áp lực thời gian (còn 5 ngày nộp danh sách), hiển thị ngày hạn chót sẽ giúp tạo tính cấp bách (urgency).

### Phát hiện 2 (Heuristic #7: Flexibility and Efficiency of Use - Linh hoạt và hiệu quả)
* **Vấn đề trên UI Stitch:** Nút chính trên mỗi card chỉ có `"View Venture ->"`. Nếu người dùng đã biết rõ nhóm và chỉ muốn lưu lại để so sánh sau thì phải click vào trang chi tiết, tốn thao tác.
* **Đề xuất từ AI:** Thêm icon Bookmark (Lưu tin) ngay góc phải trên của mỗi card và cho phép chạm giữ hoặc mở menu rút gọn để gửi pitch nhanh.
* **Quyết định của sinh viên:** **CHẤP NHẬN**. Thêm nút Bookmark/Lưu trữ vào component Card trong Figma để sinh viên có thể lưu 3–4 nhóm tiềm năng trước khi quyết định nộp đơn.

### Phát hiện 3 (Heuristic #8: Aesthetic and Minimalist Design - Thiết kế tối giản)
* **Vấn đề trên UI Stitch:** Phần header hiển thị quá nhiều khối thông tin liên tiếp (Avatar + Lời chào `Hi Priya` + Tiêu đề lớn `Co-Founders & Teams` + Ô tìm kiếm + Chip lọc) làm chiếm gần 40% chiều cao màn hình trước khi người dùng nhìn thấy thẻ dự án đầu tiên.
* **Đề xuất từ AI:** Tinh gọn phần Header: Gộp lời chào và avatar vào cùng một hàng trên App Bar; chuyển khẩu hiệu dài thành phụ đề ngắn hoặc chỉ hiển thị khi cuộn lên trên cùng (Collapsible App Bar).
* **Quyết định của sinh viên:** **CHẤP NHẬN**. Thiết kế lại App Bar trong Figma dạng thu gọn để chừa không gian hiển thị ít nhất 1.5 thẻ dự án trong tầm mắt đầu tiên (Above the fold).

### Phát hiện 4 (Tiêu chuẩn Accessibility WCAG 2.1 - Vùng chạm Touch Target)
* **Vấn đề trên UI Stitch:** Icon Bookmark và nút mũi tên chuyển trang có kích thước hiển thị khoảng `24 × 24 dp`, nhỏ hơn quy chuẩn tối thiểu `48 × 48 dp` của Android Material Design, dễ bấm trượt khi dùng một tay trên màn hình `360 dp`.
* **Đề xuất từ AI:** Mở rộng vùng padding ẩn xung quanh các icon để đảm bảo hit-box đạt tối thiểu `48 × 48 dp`.
* **Quyết định của sinh viên:** **CHẤP NHẬN**. Cài đặt Auto Layout với kích thước bounding box `48 × 48 dp` cho tất cả interactive icons trong Figma component library.

### Phát hiện 5 (Heuristic #9: Help Users Recognize, Diagnose, and Recover from Errors - Phòng ngừa và phục hồi lỗi)
* **Vấn đề trên UI Stitch:** Stitch chỉ sinh ra giao diện ở trạng thái lý tưởng (Happy State với nhiều dữ liệu). Hoàn toàn chưa có kịch bản khi người dùng tìm kiếm một từ khóa không tồn tại hoặc áp dụng bộ lọc quá ngặt nghèo.
* **Đề xuất từ AI:** Bổ sung màn hình **Empty State** có hình minh họa, thông báo `"Không tìm thấy nhóm phù hợp với bộ lọc hiện tại"` và một nút CTA nổi bật `"Đặt lại bộ lọc"` hoặc `"Tự tạo nhóm mới"`.
* **Quyết định của sinh viên:** **CHẤP NHẬN**. Thiết kế riêng một màn hình Empty State và Error State trong trang `03 Final UI` của Figma để phục vụ Flow 3 (Error & Recovery).

---

## 4. Ba vòng lặp tinh chỉnh có ý nghĩa (3 Meaningful Iterations)

### Vòng lặp 1: Tối ưu thứ bậc thị giác App Bar & Header (Visual Hierarchy Optimization)
* **Vấn đề cụ thể:** Phần đầu trang chiếm diện tích quá lớn (hơn 300dp), đẩy nội dung quan trọng xuống dưới nếp gấp màn hình (below the fold).
* **Hành động tinh chỉnh:** 
  * Thu gọn App Bar thành 1 hàng chuẩn 56dp (Avatar bên trái, Icon thông báo bên phải).
  * Đặt thanh tìm kiếm ngay dưới App Bar, tích hợp nút Filter trực tiếp vào bên phải ô tìm kiếm.
* **Kết quả:** Thẻ dự án đầu tiên hiển thị trọn vẹn 100% ngay khi vừa mở ứng dụng.

### Vòng lặp 2: Chuẩn hóa Design System & Accessibility Touch Targets (WCAG 2.1 Compliance)
* **Vấn đề cụ thể:** Các nút bấm phụ và icon bookmark có vùng chạm quá nhỏ (28dp), độ tương phản của chữ phụ màu xám nhạt chưa đạt 4.5:1.
* **Hành động tinh chỉnh:** 
  * Tăng toàn bộ touch target lên chuẩn `48 × 48 dp`.
  * Điều chỉnh màu chữ phụ (`color-text-secondary`) từ `#64748B` thành `#475569` (đạt tỷ lệ tương phản 5.4:1 trên nền trắng).
  * Định nghĩa biến Figma Variables cho toàn bộ bảng màu và spacing.
* **Kết quả:** Đạt chuẩn tiếp cận WCAG 2.1 AA cho toàn bộ thành phần giao diện.

### Vòng lặp 3: Thiết kế các trạng thái biên (Empty State, Loading Skeleton & Error Recovery)
* **Vấn đề cụ thể:** Thiếu phản hồi hệ thống khi không có dữ liệu hoặc khi mạng chập chờn.
* **Hành động tinh chỉnh:** 
  * Xây dựng Component **Skeleton Loading Card** mô phỏng hình khối của card dự án với hiệu ứng nhấp nháy 1.5s.
  * Xây dựng **Empty State** với nút phục hồi "Xóa bộ lọc".
  * Xây dựng **Error Dialog** thông báo khi nhóm vừa bị người khác nộp đơn lấp đầy slot cuối cùng.
* **Kết quả:** Trải nghiệm người dùng liền mạch, không còn tình trạng "ngõ cụt" (dead-end).

---

## 5. Bảng ghi nhận quyết định thiết kế (Decision Matrix)

| Đề xuất cải tiến | Nguồn gốc | Quyết định | Lý do lập luận chuyên môn | Phản ánh trên Figma |
| :--- | :--- | :---: | :--- | :--- |
| Thu gọn header từ 3 tầng xuống 1 tầng | AI Critique (Heuristic #8) | **Chấp nhận** | Tiết kiệm không gian hiển thị thẻ dự án trên màn hình `360 × 800 dp` của sinh viên | Thể hiện tại Page 03 Final UI (SCR-02) |
| Thêm bộ đếm ngược deadline còn 5 ngày | AI Critique (Heuristic #1) | **Chấp nhận** | Đánh trúng nỗi đau (pain point) của Persona Huy đang gấp rút chốt nhóm trước hạn | Thể hiện trên Badge đầu mỗi Card dự án |
| Đổi màu nền từ trắng tuyền sang xám nhạt `#F8FAFC` | Bản mô tả DESIGN.md | **Chấp nhận** | Giúp các thẻ Card màu trắng nổi bật rõ ràng theo chiều sâu (elevation) mà không cần viền đen dày | Áp dụng qua Variable `color-background` |
| Sử dụng Dark Mode mặc định | AI Gợi ý thêm | **Từ chối** | Sinh viên thường xem app ngoài trời hoặc sảnh trường; Light Theme có độ tương phản tự nhiên tốt hơn dưới ánh sáng mạnh | Giữ nguyên Light Theme theo chuẩn Lab |
| Tăng touch target lên 48x48dp | Accessibility Checklist | **Chấp nhận** | Tuân thủ nghiêm ngặt chuẩn WCAG 2.1 và Material Design 3 | Component Button & Icon trong Page 05 |
| Bổ sung Skeleton Loading | Heuristic #1 & Lab Rule | **Chấp nhận** | Tạo cảm giác hệ thống phản hồi tức thì, tránh người dùng bấm liên tục gây lỗi gửi trùng đơn | Thể hiện trong Prototype chuyển cảnh |
