# BẢNG NỘI DUNG VÀ KỊCH BẢN THUYẾT TRÌNH SLIDE (LAB 2)
## Đề tài: Hệ thống Ghép nhóm Khởi nghiệp (EXE Team Matching) - NHÓM 4
> **Tuân thủ:** Chuẩn đánh giá [Lab 2 Presentation & Demo Guideline](https://prm393-material.web.app/lab2-presentation.html) và [Persona Guideline v1.0](https://prm393-material.web.app/persona-guideline).
> **Thời lượng đề xuất:** 10 phút thuyết trình (12 slides) · 5 phút Live Demo · 5 phút Q&A.

---

### Bảng phân công vai trò thuyết trình Nhóm 4

| STT | Thành viên | Vai trò phụ trách | Phụ trách Slide | Thời gian nói |
| :-: | :--- | :--- | :---: | :---: |
| 1 | **Tăng Mình Trọng** | Trưởng nhóm · UX Research & IA | Slide 01, 02, 03 | ~ 2.5 phút |
| 2 | **Phan Anh Tuấn** | User Flow & AI Generation Specialist | Slide 04, 05, 06 | ~ 2.5 phút |
| 3 | **Đỗ Anh Minh** | Design System & UI Specialist | Slide 07, 08, 09 | ~ 2.5 phút |
| 4 | **Lữ Phước Nhật Tú** | Interaction, Prototype & Flutter Handoff | Slide 10, 11, 12 | ~ 2.5 phút |

---

## SLIDE 01: Project Overview (Tổng quan Dự án)
* **Người trình bày:** Tăng Mình Trọng (Trưởng nhóm)
* **Tiêu đề Slide:** EXE Team Matching - Hệ thống Quản lý Ghép nhóm Khởi nghiệp
* **Nội dung chính:**
  * **Vấn đề thực tế:** Sinh viên Kỹ thuật (IT) và Kinh tế/Marketing khi bước vào kỳ đồ án khởi nghiệp (EXE101/201) gặp khó khăn lớn trong việc tìm đồng đội đa ngành, dẫn đến tình trạng trôi bài trên Facebook, ghép vội vàng sát deadline và gặp "free-rider".
  * **Giải pháp sản phẩm:** Ứng dụng di động EXE Team Matching kết nối sinh viên dựa trên Ma trận kỹ năng (Skill Matrix), định hướng đề tài và mức độ cam kết thời gian.
  * **Đội ngũ Nhóm 4:**
    1. Tăng Mình Trọng (Trưởng nhóm): UX Research, Persona, Quản phối dự án.
    2. Phan Anh Tuấn: User Flows, AI Prompt Engineering, Heuristics Critique.
    3. Đỗ Anh Minh: Design System, Figma Components, Layout Audit.
    4. Lữ Phước Nhật Tú: Interactive Prototype, Accessibility & Flutter Handoff.
  * **Kênh truy cập minh chứng:**
    * GitHub: `https://github.com/LuTu-2004/prm323-lab2-group4`
    * Figma Public View: `https://www.figma.com/design/ZaGhw1hrYaguAZFcqruZMC/PRM323---Lab-2---EXE-Match?node-id=0-1`
* **Minh chứng gắn kèm:** Logo/Bìa sản phẩm, Link Repo GitHub, Link Figma Canvas.
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Kính chào thầy và các bạn, hôm nay Nhóm 4 xin đại diện trình bày kết quả Lab 2 môn PRM323 với đề tài Hệ thống ghép nhóm Khởi nghiệp EXE Team Matching. Ứng dụng ra đời nhằm giải quyết bài toán nhức nhối nhất của sinh viên năm 3: tìm kiếm đồng đội đa ngành có cùng chí hướng và mức độ cam kết cao trước hạn chót của nhà trường. Sản phẩm của nhóm đã được hoàn thiện từ khâu nghiên cứu Persona, User Flow, sinh phôi AI bằng Google Stitch, tinh chỉnh Design System chuẩn WCAG và bàn giao kỹ thuật cho lập trình viên Flutter."*

---

## SLIDE 02: Problem & Persona (Bài toán & Chân dung Người dùng)
* **Người trình bày:** Tăng Mình Trọng
* **Tiêu đề Slide:** Primary Persona - Lê Quốc Huy (Tech-Savvy Active Seeker)
* **Nội dung chính:**
  * **Chân dung cốt lõi (12 trường theo Persona Guideline):**
    * *Độ tuổi & Chuyên ngành:* 21 tuổi, Sinh viên năm 3 Kỹ thuật Phần mềm (SE).
    * *Bối cảnh sử dụng:* Dùng Android (360×800 dp), thao tác 1 tay trên xe buýt/sảnh trường, deadline nộp nhóm chỉ còn 5 ngày.
    * *Mục tiêu:* Tìm nhóm có đề tài hợp thế mạnh công nghệ, kết nối được bạn Kinh tế/Marketing uy tín, cam kết ≥10-15h/tuần.
    * *Job to Be Done:* "Khi chuẩn bị vào kỳ học EXE, tôi muốn nhanh chóng tìm và nộp hồ sơ vào nhóm phù hợp năng lực để chốt danh sách trước deadline mà không lo gặp free-rider."
    * *Pain points:* Bài đăng Facebook trôi nhanh, không minh bạch kỹ năng, nhắn tin xin vào nhóm thì đối phương đã đủ người hoặc không phản hồi.
  * **Câu phát biểu vấn đề (Problem Statement):**
    * *"Sinh viên kỹ thuật phần mềm gặp khó khăn lớn trong việc tìm kiếm và kết nối với đồng đội khối ngành Kinh tế/Marketing phù hợp về kỹ năng và cam kết trước hạn chót của nhà trường."*
  * **Chỉ số thành công đo lường được (Measurable Success Metric):**
    * *"Sinh viên tìm được nhóm EXE phù hợp và gửi thành công đơn ứng tuyển (kèm ghi chú kỹ năng) trong thời gian dưới 60 giây."*
* **Minh chứng gắn kèm:** Trích dẫn file [`ux/persona.md`](file:///e:/PRM/Thư%20mục%20mới/prm323-lab2-group4/ux/persona.md), ảnh thẻ Persona Lê Quốc Huy.
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Dựa trên chuẩn Persona Guideline của môn học, chúng em xây dựng Primary Persona đại diện là bạn Lê Quốc Huy. Huy có chuyên môn lập trình tốt nhưng mạng lưới quan hệ chỉ gói gọn trong khoa CNTT. Điểm đau lớn nhất của Huy không phải là thiếu kỹ năng, mà là thiếu kênh kết nối minh bạch và sự bất an khi gặp thành viên thiếu cam kết. Mọi quyết định thiết kế của chúng em đều hướng tới mục tiêu tối thượng: giúp Huy tìm thấy nhóm phù hợp và gửi đơn ứng tuyển thành công chỉ trong vòng dưới 60 giây."*

---

## SLIDE 03: Information Architecture (Kiến trúc Thông tin & Sitemap)
* **Người trình bày:** Tăng Mình Trọng
* **Tiêu đề Slide:** Cấu trúc Điều hướng & Kiến trúc 9 Màn hình
* **Nội dung chính:**
  * **Mô hình điều hướng (Navigation Model):** Bottom Navigation Bar gồm 4 tab phân cấp rõ ràng (Khám phá, Đơn của tôi, Tin nhắn, Cá nhân).
  * **Hệ thống 9 màn hình chia theo cấp bậc:**
    * *Cấp 1 - Màn hình chính (Top-level):*
      * Screen 01: Khám phá dự án (Discovery Feed)
      * Screen 05: Theo dõi đơn ứng tuyển (Applications Tracker)
      * Screen 08: Trạng thái không có dữ liệu (Empty State Recovery)
    * *Cấp 2 - Màn hình chi tiết & Thao tác (Child-level):*
      * Screen 02: Chi tiết dự án khởi nghiệp (Project Detail)
      * Screen 03: Bottom Sheet điền ghi chú ứng tuyển (Apply Sheet)
      * Screen 04: Xác nhận nộp đơn thành công (Application Submitted)
    * *Cấp 3 - Tương tác nâng cao (Interactive Modals):*
      * Screen 06: Lên lịch phỏng vấn Chemistry Call (Call Modal)
      * Screen 07: Xác nhận cuộc hẹn kết nối (Call Confirmed)
  * **Tối ưu hóa hành trình:** Mọi tác vụ cốt lõi đều đạt được trong tối đa 3 lần chạm (Rule of 3 taps).
* **Minh chứng gắn kèm:** Sơ đồ Sitemap dạng cây trích từ [`ux/user-flow.md`](file:///e:/PRM/Thư%20mục%20mới/prm323-lab2-group4/ux/user-flow.md) và Figma Page `01 User Flow`.
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Để phục vụ thói quen thao tác 1 tay của Huy trên màn hình di động, chúng em thiết kế kiến trúc thông tin dạng phẳng với Bottom Navigation 4 tab. Toàn bộ hệ sinh thái gồm 9 màn hình được phân cấp rành mạch từ màn hình chính Khám phá, đi sâu vào Chi tiết dự án, Bottom Sheet ứng tuyển, đến các màn hình xác nhận và theo dõi trạng thái đơn. Không có bất kỳ màn hình nào bị cô lập, đảm bảo mạch trải nghiệm liền mạch."*

---

## SLIDE 04: Three User Flows (Ba Luồng Người dùng & Phục hồi Lỗi)
* **Người trình bày:** Phan Anh Tuấn
* **Tiêu đề Slide:** 3 User Flows Cốt lõi & Kịch bản Xử lý Lỗi
* **Nội dung chính:**
  * **Flow 1: Ứng viên tìm nhóm & nộp đơn (Happy Path):**
    * Bắt đầu tại Discovery Feed -> Lọc thẻ "Flutter/Tech Lead" -> Chọn dự án EdTech -> Nhấn Apply -> Điền ghi chú cam kết 12h/tuần -> Nộp đơn -> Nhận màn hình thành công -> Chuyển về Tracker.
  * **Flow 2: Trưởng nhóm duyệt đơn & Hẹn Chemistry Call (Alternate Path):**
    * Mở Tracker -> Xem hồ sơ ứng viên -> Duyệt mức độ cam kết -> Bấm "Hẹn trao đổi" -> Chọn khung giờ 19:30 Thứ 5 -> Gửi lời mời -> Nhận màn hình Confirmed.
  * **Flow 3: Phục hồi khi tìm kiếm thất bại (Error / Recovery Path):**
    * Người dùng tìm từ khóa không tồn tại -> Hệ thống hiển thị Screen 08 (Empty State) kèm thông báo rõ ràng -> Cung cấp 2 lựa chọn phục hồi: "Xóa bộ lọc" (Reset filter) hoặc "Duyệt danh sách gợi ý" -> Người dùng nhấn nút và lập tức quay về Discovery Feed đầy đủ trong 1 chạm (Zero Dead-Ends).
* **Minh chứng gắn kèm:** Sơ đồ Mermaid từ [`ux/user-flow.md`](file:///e:/PRM/Thư%20mục%20mới/prm323-lab2-group4/ux/user-flow.md) và Board SVG Vector tại Figma Page `01 User Flow`.
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Tiếp nối phần kiến trúc, em xin trình bày 3 User Flows thực thi. Bên cạnh luồng ứng tuyển chuẩn Happy Path đạt mốc dưới 60 giây và luồng trưởng nhóm hẹn lịch Chemistry Call, nhóm đặc biệt chú trọng Luồng 3 - Phục hồi lỗi. Khi người dùng lọc tiêu chí quá hẹp dẫn đến 0 kết quả, ứng dụng tuyệt đối không để màn hình trắng hay ngõ cụt, mà đưa ra Empty State minh họa trực quan kèm nút bấm 'Xóa bộ lọc' để người dùng khôi phục trạng thái ngay lập tức."*

---

## SLIDE 05: AI UI Generation (Tạo phôi Giao diện bằng AI)
* **Người trình bày:** Phan Anh Tuấn
* **Tiêu đề Slide:** Ứng dụng Google Stitch - Kỹ thuật Prompt-to-UI
* **Nội dung chính:**
  * **Công cụ sử dụng:** Google Stitch (AI UI Generator chuyên sâu cho Mobile App).
  * **Cấu trúc Prompt nguyên văn 5 thành phần chuẩn hóa:**
    1. *Persona & Role:* Mobile App UX Designer thiết kế app cho sinh viên IT (Lê Quốc Huy).
    2. *Task:* Thiết kế màn hình khám phá dự án và chi tiết đơn ứng tuyển.
    3. *Platform:* Android Mobile tiêu chuẩn, kích thước `360 × 800 dp`, chuẩn Material 3.
    4. *Constraints:* Tuân thủ WCAG 2.1 AA (tương phản ≥4.5:1, touch target ≥48dp), hiển thị thẻ Skill Matrix.
    5. *Style & Tone:* Clean, trustworthy, hiện đại, phối màu Deep Navy (`#0F172A`) & Emerald (`#10B981`).
  * **Kết quả đầu ra ban đầu từ Stitch:** Sinh ra 8 màn hình phôi cơ bản, thể hiện được cấu trúc card và thẻ kỹ năng.
* **Minh chứng gắn kèm:** Ảnh chụp màn hình Prompt và kết quả Canvas từ [`assets/stitch/stitch_prompt_input_evidence.png`](file:///e:/PRM/Thư%20mục%20mới/prm323-lab2-group4/assets/stitch/stitch_prompt_input_evidence.png) và [`ai/ai-design-log.md`](file:///e:/PRM/Thư%20mục%20mới/prm323-lab2-group4/ai/ai-design-log.md).
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Tại bước sinh giao diện, nhóm áp dụng kỹ thuật Prompt Engineering chặt chẽ gồm 5 thành phần: định hình rõ Persona, tác vụ cụ thể, nền tảng di động chuẩn, các ràng buộc công thái học và bảng màu chủ đạo. Google Stitch đã giúp nhóm nhanh chóng trực quan hóa ý tưởng ban đầu thành 8 phôi giao diện mobile, đóng vai trò làm bàn đạp để nhóm tiến hành phản biện và tinh chỉnh chuyên sâu."*

---

## SLIDE 06: AI Iterations & Critique (Vòng lặp Tinh chỉnh & Phản biện Heuristic)
* **Người trình bày:** Phan Anh Tuấn
* **Tiêu đề Slide:** 3 Vòng lặp Cải tiến & 5 Phát hiện Usability Heuristic
* **Nội dung chính:**
  * **5 lỗi Usability nghiêm trọng được phát hiện từ bản AI ban đầu:**
    1. *H1 - Visibility of system status:* Nút Apply không hiển thị trạng thái "Đang gửi" (thiếu Loading feedback).
    2. *H3 - User control and freedom:* Bottom Sheet không có nút đóng (X) hoặc vuốt xuống để hủy.
    3. *H5 - Error prevention:* Nút "Xác nhận gửi đơn" nằm quá sát nút "Hủy", dễ gây bấm nhầm.
    4. *H7 - Flexibility and efficiency of use:* Thiếu bộ lọc nhanh theo số giờ cam kết hàng tuần.
    5. *WCAG 2.1 Contrast:* Màu chữ phụ xám nhạt `#94A3B8` trên nền trắng có tỷ lệ tương phản chỉ 2.8:1 (vi phạm chuẩn AA).
  * **3 Vòng lặp cải tiến có mục tiêu rõ rệt:**
    * *Iteration 1 (Visual Hierarchy):* Tái cấu trúc lại kích thước Font chữ, đưa tiêu đề dự án và Match % lên vị trí trọng tâm.
    * *Iteration 2 (Accessibility & Touch Targets):* Nâng toàn bộ vùng chạm nút bấm lên tối thiểu 48×48 dp; sửa màu chữ đạt tương phản 5.2:1.
    * *Iteration 3 (Edge States & Resilience):* Bổ sung đầy đủ màn hình Empty State, Loading Shimmer và Error Banner.
* **Minh chứng gắn kèm:** Bảng đối chiếu Before / After trong [`ai/ai-design-log.md`](file:///e:/PRM/Thư%20mục%20mới/prm323-lab2-group4/ai/ai-design-log.md).
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Nhóm xác định rõ: AI chỉ là trợ lý sinh phôi, con người mới là người kiểm soát chất lượng. Qua lăng kính 10 Heuristics của Nielsen và tiêu chuẩn WCAG, nhóm phát hiện AI mắc nhiều lỗi sơ đẳng như vi phạm độ tương phản và thiếu vùng chạm an toàn. Chúng em đã thực hiện 3 vòng lặp tinh chỉnh liên tiếp: từ phân cấp thị giác, chuẩn hóa công thái học vùng chạm, đến việc bổ sung hoàn chỉnh các trạng thái biên như Empty State và Loading."*

---

## SLIDE 07: Design Decisions (Ma trận Quyết định Thiết kế)
* **Người trình bày:** Đỗ Anh Minh
* **Tiêu đề Slide:** Đánh giá AI - Accept / Modify / Reject
* **Nội dung chính:**
  * **Ví dụ 1 (ACCEPT):** Chấp nhận bố cục dạng Card hiển thị thẻ kỹ năng (Skill Tags) của Stitch vì trực quan, dễ quét thông tin nhanh khi lướt danh sách.
  * **Ví dụ 2 (MODIFY):** Điều chỉnh nút "Apply" từ vị trí trôi nổi tự do (free float) thành thanh neo đáy cố định (Sticky Bottom Dock 48×56 dp) kèm giá trị cam kết thời gian, giúp ngón tay cái chạm cực dễ khi dùng 1 tay.
  * **Ví dụ 3 (REJECT):** Bác bỏ hoàn toàn đề xuất dùng Dialog pop-up toàn màn hình của AI khi điền ghi chú nộp đơn. Lý do: Pop-up che khuất toàn bộ thông tin dự án, gây mất ngữ cảnh; thay thế bằng Modal Bottom Sheet có thể kéo thả nửa màn hình.
  * **Ví dụ 4 (REJECT):** Bác bỏ việc AI chỉ dùng màu sắc (xanh lá / đỏ) để báo trạng thái duyệt đơn. Bắt buộc bổ sung icon và nhãn chữ đi kèm ("Đã duyệt", "Đang chờ") để chống nhầm lẫn cho người khiếm thị màu.
* **Minh chứng gắn kèm:** Trích từ [`design/design-decisions.md`](file:///e:/PRM/Thư%20mục%20mới/prm323-lab2-group4/design/design-decisions.md).
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Đây là minh chứng rõ nét cho năng lực phản biện của nhóm. Chúng em không nhận vơ toàn bộ những gì AI tạo ra. Với các đề xuất bất hợp lý như Pop-up che màn hình hay báo trạng thái chỉ bằng màu sắc, nhóm thẳng thừng Reject và thay thế bằng Bottom Sheet kéo vuốt cùng hệ thống nhãn kép Icon + Text. Mọi quyết định đều có căn cứ vững chắc từ thói quen người dùng và tiêu chuẩn công thái học."*

---

## SLIDE 08: Wireframe → Final UI (Từ Bản phác thảo đến 8 Màn hình Hoàn chỉnh)
* **Người trình bày:** Đỗ Anh Minh
* **Tiêu đề Slide:** Chuyển hóa Thiết kế: Low-Fi Wireframe sang 8 Final Screens
* **Nội dung chính:**
  * **Đối chiếu Low-fi vs Final UI:**
    * Thể hiện sự nhất quán về cấu trúc lưới (8dp grid system) từ Wireframe đến UI hoàn thiện.
    * Tinh chỉnh Typography và nhịp điệu thị giác (Visual Rhythm) sắc nét.
  * **Trưng bày trọn vẹn 8 màn hình chức năng độc lập (Không tính pop-up):**
    1. Screen 01: Discovery Feed (Khám phá dự án)
    2. Screen 02: Project Detail (Chi tiết dự án & Team Matrix)
    3. Screen 03: Apply Modal Sheet (Nộp đơn ứng tuyển)
    4. Screen 04: Application Submitted (Xác nhận gửi đơn)
    5. Screen 05: My Applications Tracker (Theo dõi tiến độ đơn)
    6. Screen 06: Chemistry Call Scheduler (Lên lịch phỏng vấn)
    7. Screen 07: Chemistry Call Confirmed (Xác nhận lịch hẹn)
    8. Screen 08: Empty State & Search Recovery (Màn hình phục hồi tìm kiếm)
* **Minh chứng gắn kèm:** Hình ảnh Canvas 8 màn hình từ [`assets/stitch/figma_canvas_8_screens.png`](file:///e:/PRM/Thư%20mục%20mới/prm323-lab2-group4/assets/stitch/figma_canvas_8_screens.png) và Figma Page `02 Wireframe` + `03 Final UI`.
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Trên màn hình là sự tiến hóa từ Wireframe cấu trúc sang 8 màn hình UI hoàn thiện trên Figma. Chúng em cam kết đáp ứng vượt chuẩn kiểm định C6 của môn học: có đủ tối thiểu 8 màn hình chức năng riêng biệt, bao phủ trọn vẹn mọi điểm chạm từ tìm kiếm, xem chi tiết, ứng tuyển, đặt lịch hẹn cho đến xử lý trạng thái rỗng. Tính nhất quán về khoảng cách và nhận diện thị giác được bảo toàn 100%."*

---

## SLIDE 09: Design System & Components Library (Hệ thống Thiết kế & Thư viện Linh kiện)
* **Người trình bày:** Đỗ Anh Minh
* **Tiêu đề Slide:** Design Tokens Chuẩn mực & 9 Nhóm Components Figma
* **Nội dung chính:**
  * **Hệ thống Design Tokens:**
    * *Màu sắc (Colors):* Primary Blue (`#2563EB`), Navy (`#0F172A`), Emerald Success (`#10B981`), Danger (`#EF4444`).
    * *Typography:* Phông chữ Inter hiện đại; phân cấp Type Scale từ Display 24sp, Title 18sp đến Body 14sp chuẩn tiếp cận.
    * *Spacing & Radius:* Hệ thống lưới cơ sở 4/8dp (`4dp`, `8dp`, `16dp`, `24dp`); Bo góc đồng bộ `12dp` (Card) và `8dp` (Button).
  * **Đầy đủ 9 nhóm Components trên Figma (Auto Layout + Variants):**
    1. Buttons (Primary, Secondary, Text · Default, Hover, Pressed, Disabled)
    2. Text Fields (Default, Focused, Error, With Icon)
    3. Cards (Project Card, Applicant Card, Stat Card)
    4. Navigation Bar (4 Tab Bar có trạng thái Active/Inactive)
    5. App Bar (Standard App Bar kèm Back button và Action icons)
    6. Dialog & Bottom Sheet (Overlay tương tác nửa màn hình)
    7. Loading State (Shimmer Skeleton Cards)
    8. Empty State (Illustration + Description + CTA Button)
    9. Error State (Inline Warning Banner + Error Toast)
* **Minh chứng gắn kèm:** Board SVG Figma Page `04 Design System` và `05 Components` ([`assets/figma/05_components_library.svg`](file:///e:/PRM/Thư%20mục%20mới/prm323-lab2-group4/assets/figma/05_components_library.svg)).
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Để dự án có thể mở rộng và bàn giao mượt mà cho đội ngũ kỹ thuật, chúng em xây dựng Design System hoàn chỉnh trên Figma. Toàn bộ thông số từ màu sắc, kích thước chữ, bo góc đều được quản lý bằng Figma Variables. Thư viện linh kiện bao gồm đủ 9 nhóm cốt lõi với 100% sử dụng Auto Layout và Variant states (từ Default, Hover đến Disabled và Error)."*

---

## SLIDE 10: Accessibility & Responsive Adaptation (Khả năng Tiếp cận & Thích ứng Màn hình)
* **Người trình bày:** Lữ Phước Nhật Tú
* **Tiêu đề Slide:** Kiểm chuẩn WCAG 2.1 AA & Khả năng Đáp ứng Đa thiết bị
* **Nội dung chính:**
  * **Tuân thủ tiêu chuẩn tiếp cận WCAG 2.1 AA:**
    * *Độ tương phản (Contrast Ratio):* Text trên nền đạt tỷ lệ từ `4.68:1` đến `12.6:1` (vượt ngưỡng yêu cầu 4.5:1).
    * *Vùng chạm tối thiểu (Touch Target):* 100% nút bấm, icon và ô nhập liệu có kích thước ≥ `48 × 48 dp` (hoặc chiều cao 48dp/56dp với padding bao quanh).
    * *Cỡ chữ nội dung (Readability):* Toàn bộ chữ nội dung đạt ≥ `14 sp`, nhãn phụ tối thiểu `12 sp`.
    * *Đa phương thức truyền tải:* Không chỉ dùng màu đơn thuần; luôn đi kèm Icon cảnh báo và Nhãn trạng thái dạng Text.
  * **Kiểm tra thích ứng Responsive:**
    * Thiết kế được kiểm thử trên kích thước phổ thông Android `360 × 800 dp` và mở rộng sang màn hình lớn `412 × 915 dp` mà không hề bị vỡ layout nhờ quy tắc Auto Layout và Responsive constraints.
* **Minh chứng gắn kèm:** Bảng kiểm thử tương phản Contrast Checker và kích thước vùng chạm trong [`design/design-decisions.md`](file:///e:/PRM/Thư%20mục%20mới/prm323-lab2-group4/design/design-decisions.md).
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Về mặt công thái học và tiếp cận, chúng em tự hào sản phẩm đạt 100% chuẩn WCAG 2.1 AA. Mọi nút bấm đều đảm bảo vùng chạm 48dp để người dùng không bấm trượt khi đang đi xe buýt. Độ tương phản chữ đạt từ 4.68:1 trở lên, giúp đọc rõ ngay cả dưới ánh nắng sân trường. Hệ thống layout co giãn linh hoạt, đảm bảo hiển thị hoàn hảo từ màn hình 360dp đến các dòng điện thoại cao cấp 412dp."*

---

## SLIDE 11: Live Prototype Interaction (Trình diễn Prototype Tương tác)
* **Người trình bày:** Lữ Phước Nhật Tú
* **Tiêu đề Slide:** Nguyên mẫu Tương tác Figma (Flows, Overlays & Circular Paths)
* **Nội dung chính:**
  * **Các tính năng nổi bật của bản Prototype:**
    * 3 Flow Starting Points được thiết lập chuẩn mực trên Figma Prototype.
    * Trải nghiệm Bottom Sheet dạng Modal Overlay làm tối mờ nền sau lưng (Dim background).
    * Chuyển động Smart Animate mượt mà thời gian 250–300ms.
    * Nút Back hoạt động chính xác tại mọi màn hình cấp con.
    * **Đường dẫn khép kín (Circular Return Paths):** Từ màn hình hoàn tất nộp đơn hay hủy bỏ đều có thể quay ngược về trang chủ hoặc trang quản lý đơn, loại bỏ hoàn toàn bẫy ngõ cụt (Zero Dead-Ends).
* **Minh chứng gắn kèm:** Sơ đồ liên kết Prototype tại Figma Page `06 Prototype` và kịch bản chuẩn bị demo trực tiếp 5 phút.
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Bản Prototype trên Figma Page 06 được liên kết tỉ mỉ với đầy đủ 3 luồng người dùng. Các thao tác mở Bottom Sheet, chuyển cảnh khi nộp đơn thành công và quay trở lại trang chủ đều hoạt động mượt mà. Đặc biệt, người dùng có thể thử nghiệm nhánh lỗi tại luồng tìm kiếm và phục hồi dễ dàng. Ngay sau đây, nhóm sẽ trình diễn trực tiếp bản Prototype này trong phần Demo 5 phút."*

---

## SLIDE 12: Flutter Handoff & Summary (Bàn giao Kỹ thuật & Tổng kết)
* **Người trình bày:** Lữ Phước Nhật Tú
* **Tiêu đề Slide:** Bàn giao Kỹ thuật cho Lập trình viên Flutter & Tổng kết
* **Nội dung chính:**
  * **Hồ sơ Flutter Handoff toàn diện:**
    * *Đặc tả 6 mục cho từng màn hình:* (1) Layout Architecture, (2) Reusable Components, (3) States, (4) Interactions, (5) Navigation, (6) UI Constraints.
    * *2 Bảng ánh xạ kỹ thuật:*
      * Design Tokens -> Flutter `ThemeData` (`ColorScheme.fromSeed`, `TextTheme`, `EdgeInsets`).
      * Figma Components -> Flutter Widgets (`FilledButton`, `Card`, `FilterChip`, `showModalBottomSheet`).
  * **Tổng kết thành quả Lab 2:**
    * 100% hoàn thành chuỗi quy trình: Analyze -> Generate -> Critique -> Refine -> Prototype -> Handoff.
    * Đáp ứng trọn vẹn rubric 100 điểm của môn học.
  * **Liên kết nộp bài chính thức:**
    * GitHub: `https://github.com/LuTu-2004/prm323-lab2-group4`
    * Figma Link: `https://www.figma.com/design/ZaGhw1hrYaguAZFcqruZMC/PRM323---Lab-2---EXE-Match?node-id=0-1`
* **Minh chứng gắn kèm:** Trích từ tài liệu [`handoff/flutter-handoff.md`](file:///e:/PRM/Thư%20mục%20mới/prm323-lab2-group4/handoff/flutter-handoff.md) và README repository.
* **Lời thoại gợi ý (Speaker Notes):**
  > *"Để khép lại bài thuyết trình, tài liệu Flutter Handoff của nhóm cung cấp bản đặc tả kỹ thuật chi tiết đến từng Widget và Theme property. Một lập trình viên Flutter dù chưa từng tham gia dự án cũng có thể nhìn vào đặc tả này để dựng giao diện chính xác từng pixel và quản lý đầy đủ các trạng thái logic. Nhóm 4 xin chân thành cảm ơn thầy và các bạn đã lắng nghe!"*

---

## KỊCH BẢN DEMO TRỰC TIẾP 5 PHÚT (LIVE DEMO SCRIPT)

| Phút | Hành động thực hiện trên màn hình máy tính | Điểm cần nhấn mạnh bằng lời nói |
| :-: | :--- | :--- |
| **00:00 - 01:00** | **Mở Figma Canvas**: Trình chiếu đủ đúng **6 Pages**: `01 User Flow`, `02 Wireframe`, `03 Final UI`, `04 Design System`, `05 Components`, `06 Prototype`. | "File Figma của nhóm tuân thủ cấu trúc chuẩn 6 pages được yêu cầu, thể hiện rõ chuỗi tiến hóa từ flow tới linh kiện." |
| **01:00 - 02:00** | **Vào Page 03 Final UI**: Lướt qua đủ **8 màn hình độc lập** (không tính popup nhỏ). Phóng to Screen 01 và Screen 02. | "Nhóm có đủ 8 màn hình riêng biệt, tuân thủ chặt chẽ lưới 8dp và chuẩn tương phản màu sắc." |
| **02:00 - 03:30** | **Chạy Prototype (Page 06)**:<br>1. *Chạy Flow 1*: Click Card -> Bấm Apply -> Kéo mở Bottom Sheet -> Bấm Submit -> Chuyển sang Screen 04.<br>2. *Chạy Flow 3*: Bấm tìm kiếm ra Empty State Screen 08 -> Bấm nút 'Xóa bộ lọc' quay về danh sách. | "Prototype hỗ trợ chuyển động Smart Animate, Modal Bottom Sheet mượt mà và đặc biệt có nhánh phục hồi lỗi không ngõ cụt." |
| **03:30 - 04:15** | **Vào Page 05 Components & Variables**: Click chọn Button/Card để cho xem Auto Layout và bảng Tokens. | "Toàn bộ component đều xây dựng từ Auto Layout và liên kết với hệ thống Figma Variables chuẩn." |
| **04:15 - 05:00** | **Mở GitHub Repository**: Cho xem file `ai/ai-design-log.md` và `handoff/flutter-handoff.md` (2 bảng ánh xạ Token sang Widget). | "Mọi bằng chứng prompt, phản biện Heuristic và đặc tả ánh xạ sang Flutter Widget đều được lưu trữ minh bạch trên GitHub." |

---

## BỘ CÂU HỎI VẤN ĐÁP (Q&A CHEAT SHEET) - GIẢNG VIÊN THƯỜNG HỎI

### Câu 1: Persona có nhu cầu gì khiến bạn chọn cấu trúc điều hướng này?
* **Trả lời chuẩn:**
  > *"Dạ thưa thầy, Persona Lê Quốc Huy là sinh viên kỹ thuật thường dùng điện thoại bằng 1 tay khi đang di chuyển trên xe buýt hoặc sảnh trường, đồng thời chịu áp lực deadline 5 ngày. Do đó nhóm chọn cấu trúc phẳng với Bottom Navigation Bar 4 tab để ngón cái chạm tới dễ dàng trong 'Thumb Zone', và áp dụng nguyên tắc tối đa 3 chạm để hoàn thành tác vụ ứng tuyển, không dùng thanh menu ẩn Drawer phức tạp."*

### Câu 2: Flow nào dễ thất bại nhất? Khi xảy ra lỗi, người dùng phục hồi ra sao?
* **Trả lời chuẩn:**
  > *"Dạ thưa thầy, Flow dễ thất bại nhất là Flow tìm kiếm và lọc dự án, vì sinh viên thường gõ các từ khóa quá chi tiết hoặc chọn cùng lúc nhiều bộ lọc dẫn đến kết quả trả về bằng 0 (Empty State). Để phục hồi, nhóm thiết kế Screen 08 với thông báo thân thiện và nút hành động chính 'Xóa bộ lọc' nổi bật giúp người dùng chỉ cần 1 chạm là đưa hệ thống về lại danh sách đầy đủ, tuyệt đối không để người dùng bị bẫy trong ngõ cụt."*

### Câu 3: Một đề xuất AI nào đã bị từ chối? Vì sao?
* **Trả lời chuẩn:**
  > *"Dạ thưa thầy, khi thiết kế luồng nộp đơn ứng tuyển, Google Stitch đã đề xuất một Dialog Pop-up toàn màn hình chiếm toàn bộ giao diện. Nhóm đã REJECT đề xuất này vì nó che mất thông tin dự án bên dưới khiến sinh viên mất ngữ cảnh (context loss) và khó thao tác 1 tay. Nhóm đã thay thế bằng Modal Bottom Sheet che nửa màn hình, cho phép người dùng vừa nhìn thấy tóm tắt dự án vừa dễ dàng điền ghi chú."*

### Câu 4: Ba vòng lặp đã giải quyết ba vấn đề UX khác nhau như thế nào?
* **Trả lời chuẩn:**
  > *"Dạ thưa thầy, 3 vòng lặp có mục tiêu hoàn toàn phân biệt: Vòng 1 giải quyết Hierarchy thị giác (làm nổi bật tiêu đề và tỷ lệ match %); Vòng 2 giải quyết Accessibility & Công thái học (nâng vùng chạm từ 32dp lên ≥48dp và sửa độ tương phản màu chữ đạt chuẩn WCAG AA); Vòng 3 giải quyết Trạng thái biên và Tính bền vững (bổ sung đầy đủ Empty State, Loading Shimmer và màn hình xác nhận)."*

### Câu 5: Nếu đổi primary color hoặc spacing token, những màn hình nào tự cập nhật?
* **Trả lời chuẩn:**
  > *"Dạ thưa thầy, toàn bộ 8 màn hình và tất cả các component đều sẽ tự động cập nhật ngay lập tức. Lý do là nhóm đã gắn triệt để hệ thống Figma Variables cho cả màu sắc (Fill, Stroke) và khoảng cách Spacing/Padding trong Auto Layout. Khi đổi biến gốc `primary-blue` hay `spacing-16`, toàn bộ dự án sẽ đồng bộ tự động."*

### Câu 6: Làm thế nào chứng minh màn hình rộng 412 dp không vỡ layout?
* **Trả lời chuẩn:**
  > *"Dạ thưa thầy, nhóm thiết kế 100% màn hình bằng Auto Layout với các thiết lập 'Fill container' cho nội dung văn bản và thẻ Card, kết hợp 'Fixed size' cho các icon/avatar và neo giữ khoảng cách padding hai bên 16dp. Khi chuyển khung nhìn từ 360dp sang 412dp, bề ngang các thẻ card tự động giãn đều theo trục ngang mà không làm tràn chữ hay méo tỷ lệ linh kiện."*

### Câu 7: Một lập trình viên Flutter chưa biết dự án sẽ dựa vào đâu để dựng màn hình và states?
* **Trả lời chuẩn:**
  > *"Dạ thưa thầy, lập trình viên sẽ dựa vào file `handoff/flutter-handoff.md`. Trong đó nhóm đã xây dựng sẵn 2 bảng mapping tổng thể từ Design Token sang Flutter `ThemeData` và từ Component sang Flutter Widget cụ thể. Đồng thời mỗi màn hình đều có đủ 6 mục đặc tả chi tiết về bố cục, các component tái sử dụng, danh sách states (Normal, Loading, Empty, Error) và các sự kiện tương tác."*
