# Phân tích UX: Information Architecture & User Flows

## 1. Kiến trúc thông tin (Information Architecture - IA)

Ứng dụng quản lý ghép nhóm EXE được tổ chức theo cấu trúc phân tầng rõ ràng, tối ưu cho thao tác tìm kiếm và điều hướng nhanh trên di động:

```
App Root (Bottom Navigation & Main Screens)
├── [Màn hình 01] Onboarding & Lựa chọn vai trò (Cấp cao - Khởi động)
├── Bottom Navigation (Cấp điều hướng chính):
│   ├── [Màn hình 02] Trang chủ / Khám phá nhóm EXE (Home / Discovery Feed)
│   │   ├── [Màn hình 03] Modal Bộ lọc nâng cao & Bản đồ kỹ năng (Filter Sheet)
│   │   └── [Màn hình 04] Chi tiết nhóm dự án EXE (Project/Group Detail)
│   │       └── [Màn hình 06] Bottom Sheet Gửi đơn xin gia nhập (Apply/Pitch Sheet)
│   ├── [Màn hình 07] Quản lý lời mời & Đơn xin ghép nhóm (Applications / Requests)
│   │   ├── Tab: Yêu cầu đã gửi (Sent Requests)
│   │   └── Tab: Đơn apply cần duyệt (Incoming Applications - Dành cho Leader)
│   ├── [Màn hình 08] Bảng điều khiển nhóm chính thức (Team Workspace Dashboard)
│   └── [Màn hình 09] Thông báo hoạt động & Deadline (Notifications)
└── Màn hình phụ / Liên kết ngoài:
    └── [Màn hình 05] Hồ sơ năng lực thành viên (Member Profile & Skill Matrix)
```

### Danh sách 9 màn hình chuẩn thiết kế (Kích thước 360 × 800 dp):
1. **SCR-01 (Onboarding):** Chào mừng và chọn mục tiêu: "Tìm nhóm để tham gia" hoặc "Tạo nhóm & Tuyển thành viên".
2. **SCR-02 (Discovery Feed):** Danh sách các nhóm dự án đang tuyển, thanh tìm kiếm nhanh, tag chuyên ngành (Tech, Business, Marketing, Design).
3. **SCR-03 (Filter Modal):** Lọc theo lĩnh vực đề tài, vai trò còn thiếu, số giờ cam kết/tuần, múi giờ học.
4. **SCR-04 (Group Detail):** Thông tin dự án, số slot trống (ví dụ: 3/5), mô tả đề tài, danh sách thành viên hiện tại và vai trò còn thiếu.
5. **SCR-05 (Member Profile):** Hồ sơ cá nhân của ứng viên gồm Bio, Chuyên ngành, Kỹ năng cứng/mềm, Link portfolio/GitHub và độ tin cậy.
6. **SCR-06 (Pitch/Apply Sheet):** Form gửi lời mời xin vào nhóm: chọn vai trò ứng tuyển, viết lời giới thiệu ngắn (pitch).
7. **SCR-07 (Request Management):** Quản lý tình trạng đơn (Đang chờ duyệt, Được chấp nhận, Bị từ chối) và danh sách ứng viên xin vào nhóm.
8. **SCR-08 (Team Dashboard):** Khi đã ghép đủ nhóm: hiển thị 5 thành viên, vai trò phân công, link Zalo/Trello nhóm, đồng hồ đếm ngược deadline nộp danh sách.
9. **SCR-09 (Notifications):** Danh sách thông báo lời mời mới, kết quả duyệt, nhắc nhở hạn chót.

---

## 2. Các kịch bản luồng người dùng (User Flows)

### Flow 1: Ứng viên tìm kiếm và xin gia nhập nhóm phù hợp (Core Happy Path)
* **Điểm bắt đầu:** Ứng viên ở Màn hình Khám phá (SCR-02).
* **Mục tiêu:** Tìm được nhóm EdTech đang thiếu Developer và gửi đơn xin gia nhập.
* **Điểm kết thúc:** Đơn ứng tuyển được gửi thành công, chuyển sang trạng thái chờ duyệt (Pending) ở SCR-07.

```mermaid
flowchart TD
    Start([Bắt đầu: Màn hình SCR-02 Discovery Feed]) --> Search[Sử dụng thanh tìm kiếm hoặc chọn tag EdTech]
    Search --> Filter[Nhấn nút Lọc để chọn tiêu chí Developer]
    Filter --> ViewGroup[Chọn nhóm EduConnect từ danh sách]
    ViewGroup --> Detail[Xem Màn hình SCR-04 Chi tiết nhóm]
    Detail --> CheckSlot{Nhóm còn slot trống?}
    CheckSlot -- Còn slot --> ClickApply[Bấm nút 'Xin gia nhập']
    ClickApply --> OpenPitch[Mở Màn hình SCR-06 Bottom Sheet Pitch]
    OpenPitch --> FillForm[Điền lời nhắn & xác nhận kỹ năng]
    FillForm --> Submit[Bấm 'Gửi yêu cầu']
    Submit --> ShowSuccess[Hiển thị Toast: Gửi thành công!]
    ShowSuccess --> NavManage[Điều hướng sang SCR-07 Quản lý đơn]
    NavManage --> End([Kết thúc: Đơn ở trạng thái Chờ duyệt])
```

---

### Flow 2: Trưởng nhóm xem đơn ứng tuyển và duyệt thành viên (Creator Management Flow)
* **Điểm bắt đầu:** Trưởng nhóm nhận thông báo có ứng viên mới (SCR-09).
* **Mục tiêu:** Đánh giá hồ sơ của ứng viên và quyết định duyệt vào nhóm.
* **Điểm kết thúc:** Ứng viên trở thành thành viên chính thức, slot nhóm được cập nhật trên SCR-08.

```mermaid
flowchart TD
    Start([Bắt đầu: Nhận thông báo tại SCR-09]) --> ClickNotif[Chạm vào thông báo: 'Có ứng viên apply mới']
    ClickNotif --> OpenManage[Mở SCR-07 Tab Đơn apply cần duyệt]
    OpenManage --> ViewApplicant[Xem thẻ ứng viên Lê Quốc Huy]
    ViewApplicant --> OpenProfile[Nhấn xem SCR-05 Hồ sơ năng lực]
    OpenProfile --> Evaluate{Kỹ năng & cam kết có đạt?}
    Evaluate -- Phù hợp --> ClickAccept[Bấm nút 'Chấp nhận']
    ClickAccept --> ShowConfirmDialog[Hiển thị Dialog xác nhận kết nạp]
    ShowConfirmDialog --> Confirm[Nhấn 'Đồng ý kết nạp']
    Confirm --> LoadingState[Chuyển cảnh xử lý Loading 1.5s]
    LoadingState --> UpdateTeam[Hệ thống cập nhật sĩ số nhóm lên 4/5]
    UpdateTeam --> NavDashboard[Chuyển sang SCR-08 Team Dashboard]
    NavDashboard --> End([Kết thúc: Thành viên mới xuất hiện trong nhóm])
    Evaluate -- Không phù hợp --> ClickReject[Bấm nút 'Từ chối']
    ClickReject --> PromptReason[Chọn lý do: 'Đã tuyển đủ vai trò']
    PromptReason --> EndReject([Kết thúc: Đơn chuyển sang trạng thái Từ chối])
```

---

### Flow 3: Tìm kiếm thất bại & Xử lý lỗi nhóm đã đủ slot (Error & Recovery Flow - Bắt buộc)
* **Điểm bắt đầu:** Ứng viên tìm kiếm nhóm hoặc gửi yêu cầu gia nhập (SCR-02 / SCR-04).
* **Tình huống lỗi 1:** Bộ lọc quá hẹp dẫn tới không tìm thấy kết quả (Empty State).
* **Tình huống lỗi 2:** Ứng viên bấm xin gia nhập nhóm nhưng nhóm vừa được trưởng nhóm duyệt đủ người trước đó vài giây (Race condition / Conflict Error).
* **Nhánh phục hồi:** Hệ thống báo lỗi rõ ràng, cung cấp nút hoàn tác/reset bộ lọc và gợi ý các nhóm thay thế tương tự.

```mermaid
flowchart TD
    Start([Bắt đầu: SCR-02 Discovery Feed]) --> ApplyStrictFilter[Lọc tiêu chí quá hẹp: Role Designer + Fintech + 20h/tuần]
    ApplyStrictFilter --> CheckResult{Có kết quả phù hợp?}
    
    CheckResult -- Không có kết quả --> EmptyState[Hiển thị Màn hình Empty State: 'Không tìm thấy nhóm phù hợp']
    EmptyState --> Recovery1[Nhấn nút 'Đặt lại bộ lọc']
    Recovery1 --> ResetFilter[Hệ thống xóa bộ lọc về mặc định]
    ResetFilter --> ShowAll[Hiển thị lại toàn bộ danh sách nhóm]
    ShowAll --> EndRecover1([Phục hồi thành công: Người dùng tiếp tục duyệt nhóm])

    CheckResult -- Có kết quả --> SelectGroup[Chọn nhóm PaySafe]
    SelectGroup --> ClickJoin[Bấm 'Xin gia nhập']
    ClickJoin --> ServerValidate{Kiểm tra slot trống trên Server}
    ServerValidate -- Đã đủ slot (0 slot trống) --> ErrorDialog[Hiển thị Error State Dialog: 'Rất tiếc! Nhóm này vừa tuyển đủ thành viên']
    ErrorDialog --> Recovery2[Bấm nút 'Khám phá nhóm tương tự']
    Recovery2 --> SuggestAlternative[Hệ thống tự động lọc các nhóm Fintech khác đang cần tuyển]
    SuggestAlternative --> EndRecover2([Phục hồi thành công: Chuyển hướng tới danh sách gợi ý mới])
```

---

## 3. Bảng ánh xạ Flow sang các Màn hình (Screen Mapping Table)

| Tên màn hình | Ký hiệu | Flow 1: Ứng viên xin vào nhóm | Flow 2: Leader duyệt thành viên | Flow 3: Lỗi & Phục hồi |
| :--- | :--- | :---: | :---: | :---: |
| Onboarding & Chọn vai trò | SCR-01 | | | |
| Khám phá nhóm (Discovery Feed) | SCR-02 | **X** (Bước 1) | | **X** (Bước 1, Phục hồi) |
| Bộ lọc nâng cao (Filter Modal) | SCR-03 | **X** (Bước 2) | | **X** (Nhánh lỗi lọc) |
| Chi tiết nhóm (Group Detail) | SCR-04 | **X** (Bước 3) | | **X** (Nhánh lỗi hết slot) |
| Hồ sơ năng lực (Member Profile) | SCR-05 | | **X** (Bước 3) | |
| Bottom Sheet nộp đơn (Pitch Sheet) | SCR-06 | **X** (Bước 4) | | |
| Quản lý đơn (Request Management) | SCR-07 | **X** (Bước 5) | **X** (Bước 2) | |
| Bảng điều khiển nhóm (Team Dashboard) | SCR-08 | | **X** (Bước 5) | |
| Thông báo (Notifications) | SCR-09 | | **X** (Bước 1) | |
| Màn hình Empty / Error State | STATES | | | **X** (Hiển thị lỗi & Retry) |
