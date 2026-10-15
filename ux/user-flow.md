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

### Luồng 1: Khám phá dự án & Nộp đơn ứng tuyển (Applicant Flow)
* **Khởi đầu:** SCR-02 Discovery Feed.
* **Mục tiêu:** Tìm nhóm EdTech phù hợp để ứng tuyển trực tiếp hoặc lưu lại đối sánh sau.
* **Hoàn thành:** 
  * Hướng chính: Đơn ứng tuyển được gửi thành công, chuyển sang trạng thái chờ duyệt (SCR-07).
  * Hướng phụ: Dự án được lưu vào danh mục Saved Ventures để xem xét sau.

```mermaid
flowchart TD
    Start([Bắt đầu: SCR-02 Feed]) --> Search[Tìm kiếm từ khóa hoặc chọn Tag EdTech]
    Search --> Filter[Nhấn nút Lọc để chọn tiêu chí Developer]
    Filter --> ViewGroup[Chọn thẻ nhóm EduConnect từ danh sách]
    ViewGroup --> Detail[Xem SCR-04 Chi tiết nhóm EduConnect]
    Detail --> Decision{Nhu cầu của ứng viên?}

    %% Hướng ứng tuyển trực tiếp
    Decision -- Ứng tuyển ngay --> ClickApply[Bấm nút 'Xin gia nhập']
    ClickApply --> OpenPitch[Mở SCR-06 Bottom Sheet Pitch]
    OpenPitch --> FillForm[Chọn Role Developer & điền cam kết 12h/tuần]
    FillForm --> Submit[Bấm 'Nộp đơn ứng tuyển']
    Submit --> ShowSuccess[SCR-04 Sub: Thông báo nộp thành công #7842]
    ShowSuccess --> NavManage[Điều hướng sang SCR-07 Quản lý đơn]
    NavManage --> EndHappy([Hoàn thành: Đơn ở trạng thái Chờ duyệt])

    %% Hướng lưu trữ đối sánh sau
    Decision -- Lưu xem sau --> ClickBookmark[Chạm icon Bookmark lưu dự án]
    ClickBookmark --> ToastSaved[Hiển thị Toast: 'Đã lưu vào danh sách quan tâm']
    ToastSaved --> ContinueBrowsing[Tiếp tục lướt xem các nhóm khác]
    ContinueBrowsing --> EndAlt([Hoàn thành: Dự án lưu trong mục Saved])
```

---

### Luồng 2: Tiếp nhận hồ sơ & Phê duyệt thành viên (Leader Review Flow)
* **Khởi đầu:** SCR-09 Nhận thông báo có hồ sơ mới.
* **Mục tiêu:** Đánh giá năng lực ứng viên và đưa ra quyết định phê duyệt hoặc từ chối lịch sự.
* **Hoàn thành:** 
  * Hướng chính: Ứng viên được kết nạp, sĩ số nhóm cập nhật lên 4/5 (SCR-08).
  * Hướng phụ: Đơn bị từ chối kèm phản hồi và lưu hồ sơ vào Talent Pool dự phòng.

```mermaid
flowchart TD
    Start([Bắt đầu: SCR-09 Thông báo]) --> ClickNotif[Chạm thông báo: 'Có ứng viên apply mới']
    ClickNotif --> OpenManage[Mở SCR-07 Tab Đơn apply cần duyệt]
    OpenManage --> ViewApplicant[Xem thẻ ứng viên Lê Quốc Huy]
    ViewApplicant --> OpenProfile[Nhấn xem SCR-05 Hồ sơ năng lực]
    OpenProfile --> Evaluate{Kết quả đánh giá hồ sơ?}

    %% Hướng phê duyệt kết nạp
    Evaluate -- Hồ sơ đạt chuẩn --> ClickAccept[Bấm nút 'Chấp nhận kết nạp']
    ClickAccept --> ShowConfirmDialog[Hiển thị Dialog xác nhận kết nạp]
    ShowConfirmDialog --> Confirm[Nhấn 'Đồng ý kết nạp']
    Confirm --> LoadingState[Chuyển cảnh xử lý Loading 1.5s]
    LoadingState --> UpdateTeam[Cập nhật sĩ số nhóm lên 4/5]
    UpdateTeam --> NavDashboard[Chuyển sang SCR-08 Team Dashboard]
    NavDashboard --> EndHappy2([Hoàn thành: Thành viên chính thức gia nhập])

    %% Hướng từ chối & lưu dự phòng
    Evaluate -- Chưa phù hợp đề tài --> ClickReject[Bấm nút 'Từ chối']
    ClickReject --> PromptReason[Chọn lý do: 'Đã tuyển đủ vai trò Developer']
    PromptReason --> SendEncourage[Gửi tin nhắn động viên & lưu vào Talent Pool]
    SendEncourage --> EndAlt2([Hoàn thành: Đóng hồ sơ ứng tuyển lịch sự])
```

---

### Luồng 3: Xử lý tìm kiếm rỗng & Điều hướng phục hồi (Search Recovery Flow)
* **Khởi đầu:** SCR-02 Discovery Feed.
* **Mục tiêu:** Xử lý và điều hướng người dùng khi bộ lọc không có dữ liệu phù hợp (Empty State).
* **Hoàn thành:** 
  * Hướng phục hồi A: Làm mới bộ lọc tìm kiếm, tải lại 18 nhóm sẵn có.
  * Hướng phục hồi B: Khám phá nhóm khởi nghiệp theo danh mục hệ thống đề xuất.

```mermaid
flowchart TD
    Start([Bắt đầu: SCR-02 Feed]) --> ApplyStrictFilter[Nhập từ khóa quá hẹp: 'Quantum NLP Rust']
    ApplyStrictFilter --> CheckResult{Kiểm tra kết quả lọc?}

    %% Tình huống không tìm thấy kết quả
    CheckResult -- 0 kết quả phù hợp --> EmptyState[SCR-08 Màn hình Empty State: 'Không tìm thấy dự án']

    %% Hướng phục hồi A: Đặt lại bộ lọc
    EmptyState -- Chọn 'Đặt lại bộ lọc' --> ClickReset[Nhấn nút 'Reset Filters']
    ClickReset --> ClearFilter[Xóa toàn bộ tiêu chí lọc về mặc định]
    ClearFilter --> ShowAll[Tải lại danh sách 18 dự án sẵn có]
    ShowAll --> EndRecover1([Hoàn thành: Tiếp tục khám phá feed])

    %% Hướng phục hồi B: Khám phá theo gợi ý
    EmptyState -- Chọn danh mục gợi ý --> ClickSuggest[Chọn Track đề xuất: 'AI & LLM Tutoring']
    ClickSuggest --> LoadAlternate[Hệ thống nạp nhóm tương đương EduConnect]
    LoadAlternate --> ViewGroup[Mở chi tiết nhóm EduConnect]
    ViewGroup --> EndRecover2([Hoàn thành: Tiếp tục luồng ứng tuyển])
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
