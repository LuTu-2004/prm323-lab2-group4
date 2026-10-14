# Đặc tả chuyển giao lập trình Flutter (Flutter Handoff Specification)

Tài liệu này cung cấp toàn bộ thông số kỹ thuật, cấu trúc Widget, ánh xạ token và ràng buộc tương tác để lập trình viên Flutter có thể hiện thực hóa 100% ứng dụng **EXE Match** mà không cần trao đổi thêm.

---

## PHẦN 1: BẢNG ÁNH XẠ CHUNG (GLOBAL MAPPING TABLES)

### 1.1. Bảng ánh xạ Design Token sang Flutter ThemeData

| Token Name trong Figma | Giá trị CSS/Hex | Tên thuộc tính trong Flutter (ThemeData) | Kiểu dữ liệu / Code mẫu |
| :--- | :--- | :--- | :--- |
| `color-primary` | `#2563EB` | `Theme.of(context).colorScheme.primary` | `Color(0xFF2563EB)` |
| `color-primary-variant` | `#1D4ED8` | `Theme.of(context).colorScheme.primaryContainer`| `Color(0xFF1D4ED8)` |
| `color-surface` | `#FFFFFF` | `Theme.of(context).colorScheme.surface` | `Color(0xFFFFFFFF)` |
| `color-background` | `#F8FAFC` | `Theme.of(context).scaffoldBackgroundColor` | `Color(0xFFF8FAFC)` |
| `color-text-primary` | `#0F172A` | `Theme.of(context).colorScheme.onSurface` | `Color(0xFF0F172A)` |
| `color-text-secondary`| `#475569` | `Theme.of(context).colorScheme.onSurfaceVariant`| `Color(0xFF475569)` |
| `color-error` | `#DC2626` | `Theme.of(context).colorScheme.error` | `Color(0xFFDC2626)` |
| `color-success` | `#16A34A` | `AppColors.success` (Custom Extension) | `Color(0xFF16A34A)` |
| `space-xs` (4dp) | `4.0` | `AppSpacing.xs` | `const double = 4.0;` |
| `space-sm` (8dp) | `8.0` | `AppSpacing.sm` | `const double = 8.0;` |
| `space-md` (16dp) | `16.0` | `AppSpacing.md` | `const double = 16.0;` |
| `space-lg` (24dp) | `24.0` | `AppSpacing.lg` | `const double = 24.0;` |
| `headline-medium` | 20sp, 600 | `Theme.of(context).textTheme.headlineMedium` | `TextStyle(fontSize: 20, fontWeight: FontWeight.w600)` |
| `title-medium` | 16sp, 600 | `Theme.of(context).textTheme.titleMedium` | `TextStyle(fontSize: 16, fontWeight: FontWeight.w600)` |
| `body-medium` | 14sp, 400 | `Theme.of(context).textTheme.bodyMedium` | `TextStyle(fontSize: 14, fontWeight: FontWeight.w400)` |
| `radius-md` | 12.0 | `AppRadius.md` | `BorderRadius.circular(12.0)` |

### 1.2. Bảng ánh xạ Components sang Flutter Widgets

| Component trong Figma | Widget tương ứng trong Flutter | Thuộc tính cấu hình chính |
| :--- | :--- | :--- |
| **Primary Button** | `FilledButton` | `style: FilledButton.styleFrom(...)`, có icon hoặc text |
| **Secondary Button** | `OutlinedButton` | `BorderSide(color: colorScheme.outline)` |
| **Text Field** | `TextFormField` | `decoration: InputDecoration(border: OutlineInputBorder(...))` |
| **Project Card** | `Card` lồng `InkWell` | `elevation: 1`, `shape: RoundedRectangleBorder(...)` |
| **Chip / Tag** | `FilterChip` / `RawChip` | `backgroundColor: colorScheme.primaryContainer` |
| **Bottom Navigation** | `NavigationBar` (M3) | `destinations: [NavigationDestination(...)]` |
| **Top App Bar** | `AppBar` | `scrolledUnderElevation: 2.0`, `centerTitle: false` |
| **Modal Pitch Sheet** | `showModalBottomSheet` | `isScrollControlled: true`, `shape: RoundedRectangleBorder(...)`|
| **Confirm Dialog** | `AlertDialog` | `title`, `content`, `actions: [TextButton, FilledButton]` |
| **Loading Skeleton** | `Shimmer.fromColors` (pkg) | Tạo `Container` bo góc nhấp nháy mô phỏng layout |

---

## PHẦN 2: ĐẶC TẢ CHI TIẾT 6 MỤC CHO TỪNG MÀN HÌNH

### MÀN HÌNH 1: SCR-02 - Khám phá nhóm EXE (Discovery Feed)

1. **Layout Hierarchy:**
   * `Scaffold`
     * `AppBar`: cố định trên cùng (`height: 56.0`).
     * `body`: `CustomScrollView` (phần có thể cuộn toàn trang).
       * `SliverToBoxAdapter`: chứa Thanh tìm kiếm `SearchBar` (`margin: space-md`) và Danh sách cuộn ngang `ListView.horizontal` của các category chip (`height: 40.0`).
       * `SliverPadding`: padding 2 bên `space-md`.
       * `SliverList`: danh sách cuộn các thẻ dự án `ProjectCard`, khoảng cách giữa các card là `space-md` (`16.0`).
     * `bottomNavigationBar`: `NavigationBar` cố định 4 tab (`height: 80.0`).
2. **Components & Variants:**
   * `SearchBar` (Default).
   * `FilterChip` (Variant: `Selected` cho "Tất cả", `Unselected` cho các ngành còn lại).
   * `ProjectCard` (Variant: `Default`, `Hovered`).
   * `FilledButton` (Variant: `Default` có icon `Icons.arrow_forward`).
   * `IconButton` (Variant: `Default` Bookmark).
3. **States:**
   * `Loading`: Hiển thị 3 `SkeletonCard` nhấp nháy xám trong khi fetch API.
   * `Populated`: Hiển thị danh sách card khi tải dữ liệu thành công.
   * `Empty`: Hiển thị `EmptyStateWidget` khi tìm kiếm/lọc không có nhóm nào phù hợp.
   * `Error`: Hiển thị banner lỗi mạng kèm nút "Tải lại trang".
4. **User Interactions:**
   * Chạm vào `SearchBar`: Kích hoạt bàn phím, điều hướng sang chế độ gợi ý từ khóa.
   * Chạm vào `FilterChip`: Lọc danh sách theo chuyên ngành tức thì.
   * Chạm vào `ProjectCard` hoặc nút `"Xem chi tiết"`: Chuyển sang màn hình `SCR-04 Group Detail`.
   * Chạm icon Bookmark: Toggle trạng thái lưu tin (đổi màu icon và hiện SnackBar).
   * Vuốt từ trên xuống: Kích hoạt `RefreshIndicator` để làm mới danh sách.
5. **Navigation:**
   * Nguồn đến: Khởi động app hoặc chuyển từ các tab khác.
   * Đích đến: Sang `SCR-04` (chạm card), sang `SCR-03` (chạm nút lọc), sang `SCR-09` (chạm chuông).
   * Nút Back: Vì là màn hình Home cấp cao, nhấn Back trên Android sẽ minimize/thoát ứng dụng.
6. **Important UI Constraints:**
   * Mọi vùng chạm icon (filter, bookmark, avatar) bọc trong `SizedBox(width: 48, height: 48)`.
   * Tên dự án giới hạn tối đa 2 dòng (`maxLines: 2, overflow: TextOverflow.ellipsis`).
   * Mô tả dự án giới hạn tối đa 3 dòng.
   * Responsive: Màn hình >= 600dp chuyển sang `GridView` 2 cột.

---

### MÀN HÌNH 2: SCR-04 - Chi tiết nhóm dự án (Group Detail)

1. **Layout Hierarchy:**
   * `Scaffold`
     * `AppBar`: có nút Back (`leading: BackButton`), tiêu đề căn trái, action: `Bookmark` và `Share`.
     * `body`: `SingleChildScrollView` (cuộn dọc)
       * `Column`:
         * `ProjectBannerCard`: chứa tag đề tài, tên dự án, giảng viên hướng dẫn (`padding: space-md`).
         * `VacancyProgressBox`: box nền `color-primary-container`, hiển thị `3/5 thành viên` và thanh tiến độ.
         * `SectionHeader`: Tiêu đề "Về dự án", text mô tả `bodyMedium`.
         * `SectionHeader`: Tiêu đề "Thành viên hiện tại", danh sách ngang các `MemberAvatarItem`.
         * `SectionHeader`: Tiêu đề "Vị trí đang tìm kiếm", danh sách card tuyển dụng con.
     * `bottomNavigationBar`: `Container` cố định có nút `FilledButton` "Xin gia nhập nhóm" (`height: 56.0`, `padding: 16.0`).
2. **Components & Variants:**
   * `FilledButton` (Variant: `Default`, `Disabled` khi nhóm đã đầy).
   * `Avatar` (Tròn, radius 24dp).
   * `LinearProgressIndicator` (Màu primary, track color xám nhạt).
   * `BadgeChip` (Màu cam nhạt báo "Cần: Marketing").
3. **States:**
   * `Default`: Hiển thị đầy đủ thông tin nhóm, nút "Xin gia nhập" khả dụng.
   * `Full Slot`: Nhóm đã đủ 5/5 người, nút CTA chuyển thành `Disabled` hiển thị text "Nhóm đã đủ thành viên".
   * `Already Applied`: Người dùng đã gửi đơn trước đó, nút CTA đổi thành `OutlinedButton` text "Xem tình trạng đơn".
4. **User Interactions:**
   * Chạm nút "Xin gia nhập nhóm": Kích hoạt `showModalBottomSheet` mở `SCR-06 Pitch Sheet`.
   * Chạm vào Avatar của thành viên trong nhóm: Mở Bottom Sheet xem tóm tắt thông tin thành viên đó.
5. **Navigation:**
   * Nguồn đến: Từ `SCR-02 Discovery Feed`.
   * Đích đến: Mở overlay `SCR-06 Pitch Sheet`.
   * Nút Back: Quay lại vị trí cuộn trước đó của `SCR-02`.
6. **Important UI Constraints:**
   * Nút CTA dưới cùng phải nằm cố định ngoài vùng cuộn để người dùng luôn nhìn thấy bất kể đang cuộn ở đâu.
   * Text mô tả dự án hỗ trợ tính năng "Xem thêm / Thu gọn" nếu dài hơn 4 dòng.

---

### MÀN HÌNH 3: SCR-06 - Form gửi đơn xin gia nhập (Pitch Bottom Sheet)

1. **Layout Hierarchy:**
   * `ModalBottomSheet` (Bán phần, tự động đẩy lên khi bàn phím xuất hiện)
     * `Padding` đệm bàn phím: `EdgeInsets.only(bottom: MediaQuery.of(context).viewInsets.bottom)`.
     * `Column` cuộn được (`mainAxisSize: MainAxisSize.min`):
       * `DragHandle`: thanh ngang xám trên đầu sheet (`width: 32, height: 4, radius: 2`).
       * `Header`: Tiêu đề "Ứng tuyển vào nhóm", nút đóng (X).
       * `DropdownButtonFormField`: Chọn vai trò ứng tuyển (`Developer`, `Marketing`, `Business`).
       * `TextFormField`: Ô nhập lời tự giới thiệu (Multiline: 4 dòng).
       * `SwitchListTile`: Toggle "Đính kèm Skill Matrix từ Profile của tôi".
       * `FilledButton`: Nút "Gửi đơn ứng tuyển" (`height: 48.0`).
2. **Components & Variants:**
   * `DropdownButtonFormField` (Variant: Default).
   * `TextFormField` (Variant: Multiline, có character counter "0/300 ký tự").
   * `Switch` (M3 Style).
   * `FilledButton` (Variant: Default, Loading).
3. **States:**
   * `Default`: Form trống, nút Gửi bị disable cho đến khi chọn vai trò và nhập tối thiểu 10 ký tự.
   * `Loading`: Khi người dùng bấm Gửi, nút chuyển sang trạng thái Loading (ẩn chữ, hiện `CircularProgressIndicator` 20dp).
   * `Success`: Đóng Bottom Sheet và hiển thị `SnackBar` xanh thành công.
   * `Error`: Hiển thị thông báo lỗi nếu mất kết nối hoặc nhóm vừa bị đầy slot.
4. **User Interactions:**
   * Chạm chọn dropdown: Mở danh sách các vai trò còn thiếu.
   * Gõ văn bản: Đếm số lượng ký tự theo thời gian thực.
   * Chạm nút Gửi: Kiểm tra validation, gọi API nộp đơn.
5. **Navigation:**
   * Nguồn đến: Bấm từ `SCR-04`.
   * Đích đến: Đóng sheet, điều hướng sang `SCR-07 Request Management` (Tab Đơn đã gửi).
   * Nút Back / Vuốt xuống: Đóng sheet và giữ nguyên màn hình `SCR-04`.
6. **Important UI Constraints:**
   * Bắt buộc có `SingleChildScrollView` tránh lỗi tràn pixel (A RenderFlex overflowed) khi mở bàn phím ảo.
   * Validation: Lời giới thiệu không được để trống, độ dài từ 10 - 300 ký tự.

---

## PHẦN 3: ĐẶC TẢ TỔNG HỢP CÁC MÀN HÌNH CÒN LẠI (SCR-01, 03, 05, 07, 08, 09)

* **SCR-01 Onboarding:** Scaffold đơn giản, `PageView` hiển thị 2 slide, nút `FilledButton` "Bắt đầu ngay" điều hướng thẳng vào `SCR-02`.
* **SCR-03 Filter Modal:** Dạng `showModalBottomSheet`, chứa cụm `Wrap` các `FilterChip` cho 4 chuyên ngành; nút "Áp dụng" trả về filter object cho `SCR-02`.
* **SCR-05 Member Profile:** Scaffold cuộn, hiển thị `CircleAvatar(radius: 48)`, `Wrap` các chip kỹ năng, danh sách `ListTile` mở link ngoài (dùng package `url_launcher` mở GitHub/CV).
* **SCR-07 Request Management:** `DefaultTabController` với 2 tabs: "Đã gửi" và "Cần duyệt"; mỗi tab dùng `ListView.builder` hiển thị `RequestItemCard` kèm `PopupMenuButton` cho thao tác rút đơn.
* **SCR-08 Team Dashboard:** Màn hình đích sau khi ghép đủ 5 người; hiển thị thẻ đếm ngược `CountdownTimerWidget`, danh sách 5 thành viên dạng `ListTile` có nút gọi điện thoại (`tel:`) và link Zalo (`https://zalo.me/...`).
* **SCR-09 Notifications:** `ListView.separated` hiển thị danh sách thông báo; khi chạm vào thông báo điều hướng chính xác tới `SCR-05` (nếu là đơn xin vào nhóm) hoặc `SCR-07` (nếu là đơn được duyệt).
