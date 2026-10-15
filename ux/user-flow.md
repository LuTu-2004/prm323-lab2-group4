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

### Flow 1: Ứng viên tìm kiếm và xin gia nhập nhóm phù hợp
* **Điểm bắt đầu:** Ứng viên tại Màn hình Khám phá (SCR-02).
* **Mục tiêu:** Tìm được nhóm EdTech phù hợp để xin gia nhập hoặc lưu lại đối sánh.
* **Điểm kết thúc:** 
  * Nhánh chính: Đơn ứng tuyển được gửi thành công (SCR-07).
  * Nhánh thay thế: Dự án được lưu vào danh sách Bookmark để xem xét sau.

```mermaid
flowchart TD
    Start([BẮT ĐẦU: SCR-02 Discovery Feed]) --> Search[Tìm kiếm từ khóa hoặc chọn Tag EdTech]
    Search --> Filter[Nhấn nút Lọc để chọn tiêu chí Developer]
    Filter --> ViewGroup[Chọn thẻ nhóm EduConnect từ danh sách]
    ViewGroup --> Detail[Xem SCR-04 Chi tiết nhóm EduConnect]
    Detail --> Decision{Hành động của ứng viên?}

    %% Nhánh thành công (Happy Path)
    Decision -- [HAPPY PATH] Ứng tuyển ngay --> ClickApply[Bấm nút 'Xin gia nhập']
    ClickApply --> OpenPitch[Mở SCR-06 Bottom Sheet Pitch]
    OpenPitch --> FillForm[Chọn Role Developer & điền cam kết 12h/tuần]
    FillForm --> Submit[Bấm 'Nộp đơn ứng tuyển']
    Submit --> ShowSuccess[SCR-04 Sub: Thông báo nộp thành công #7842]
    ShowSuccess --> NavManage[Điều hướng sang SCR-07 Quản lý đơn]
    NavManage --> EndHappy([KẾT THÚC CHÍNH: Đơn ở trạng thái Chờ duyệt])

    %% Nhánh thay thế (Alternative Path)
    Decision -- [NHÁNH THAY THẾ] Chưa muốn nộp ngay --> ClickBookmark[Bấm icon Bookmark lưu dự án]
    ClickBookmark --> ToastSaved[Hiển thị Toast: 'Đã lưu vào danh sách quan tâm']
    ToastSaved --> ContinueBrowsing[Tiếp tục lướt xem các nhóm khác]
    ContinueBrowsing --> EndAlt([KẾT THÚC THAY THẾ: Dự án được lưu trong mục Saved])
```

---

### Flow 2: Trưởng nhóm xem xét đơn ứng tuyển và phản hồi
* **Điểm bắt đầu:** Trưởng nhóm nhận thông báo có ứng viên mới (SCR-09).
* **Mục tiêu:** Đánh giá hồ sơ ứng viên và đưa ra quyết định kết nạp hoặc từ chối.
* **Điểm kết thúc:** 
  * Nhánh chính: Ứng viên được kết nạp, sĩ số nhóm cập nhật lên 4/5 (SCR-08).
  * Nhánh thay thế: Đơn bị từ chối kèm lời nhắn và chuyển vào danh sách dự phòng.

```mermaid
flowchart TD
    Start([BẮT ĐẦU: Nhận thông báo tại SCR-09]) --> ClickNotif[Chạm thông báo: 'Có ứng viên apply mới']
    ClickNotif --> OpenManage[Mở SCR-07 Tab Đơn apply cần duyệt]
    OpenManage --> ViewApplicant[Xem thẻ ứng viên Lê Quốc Huy]
    ViewApplicant --> OpenProfile[Nhấn xem SCR-05 Hồ sơ năng lực]
    OpenProfile --> Evaluate{Đánh giá kỹ năng & mức cam kết?}

    %% Nhánh thành công (Happy Path)
    Evaluate -- [HAPPY PATH] Kỹ năng đạt chuẩn --> ClickAccept[Bấm nút 'Chấp nhận kết nạp']
    ClickAccept --> ShowConfirmDialog[Hiển thị Dialog xác nhận kết nạp]
    ShowConfirmDialog --> Confirm[Nhấn 'Đồng ý kết nạp']
    Confirm --> LoadingState[Chuyển cảnh xử lý Loading 1.5s]
    LoadingState --> UpdateTeam[Cập nhật sĩ số nhóm lên 4/5]
    UpdateTeam --> NavDashboard[Chuyển sang SCR-08 Team Dashboard]
    NavDashboard --> EndHappy2([KẾT THÚC CHÍNH: Ứng viên trở thành thành viên chính thức])

    %% Nhánh thay thế (Alternative Path)
    Evaluate -- [NHÁNH THAY THẾ] Chưa phù hợp đề tài --> ClickReject[Bấm nút 'Từ chối']
    ClickReject --> PromptReason[Chọn lý do: 'Đã tuyển đủ vai trò Developer']
    PromptReason --> SendEncourage[Gửi tin nhắn động viên & lưu vào Talent Pool]
    SendEncourage --> EndAlt2([KẾT THÚC THAY THẾ: Đơn chuyển sang trạng thái Từ chối lịch sự])
```

---

### Flow 3: Lọc không có kết quả & Phục hồi tìm kiếm (Error & Recovery Branch)
* **Điểm bắt đầu:** Ứng viên tại SCR-02 Discovery Feed.
* **Mục tiêu:** Tìm kiếm nhóm dự án phù hợp; xử lý và phục hồi khi gặp lỗi không có dữ liệu.
* **Điểm kết thúc:** 
  * Phục hồi 1: Bộ lọc được xóa, quay lại danh sách 18 nhóm ban đầu.
  * Phục hồi 2: Chọn nhóm từ danh sách gợi ý đề xuất tương đương.

```mermaid
flowchart TD
    Start([BẮT ĐẦU: SCR-02 Discovery Feed]) --> ApplyStrictFilter[Nhập từ khóa quá hẹp: 'Quantum NLP Rust']
    ApplyStrictFilter --> CheckResult{Hệ thống kiểm tra kết quả?}

    %% Nhánh lỗi (Error Branch)
    CheckResult -- [NHÁNH LỖI] 0 nhóm tìm thấy --> EmptyState[Hiển thị SCR-08 Màn hình Empty State: 'No matching projects found']

    %% Nhánh phục hồi 1 (Recovery Branch A)
    EmptyState -- [PHỤC HỒI 1: Bấm Reset] --> ClickReset[Nhấn nút 'Reset Filters']
    ClickReset --> ClearFilter[Hệ thống xóa bộ lọc về mặc định]
    ClearFilter --> ShowAll[Tải lại toàn bộ danh sách 18 nhóm]
    ShowAll --> EndRecover1([KẾT THÚC PHỤC HỒI 1: Tiếp tục khám phá feed])

    %% Nhánh phục hồi 2 (Recovery Branch B)
    EmptyState -- [PHỤC HỒI 2: Chọn Gợi ý] --> ClickSuggest[Chọn Track đề xuất: 'AI & LLM Tutoring']
    ClickSuggest --> LoadAlternate[Hệ thống nạp nhóm EduConnect]
    LoadAlternate --> ViewGroup[Mở chi tiết nhóm thay thế EduConnect]
    ViewGroup --> EndRecover2([KẾT THÚC PHỤC HỒI 2: Tiếp tục luồng Flow 1])
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
