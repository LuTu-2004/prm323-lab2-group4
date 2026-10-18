# PRM323 - Lab 2: Thiết kế UI/UX có hỗ trợ AI
## Đề tài: Hệ thống quản lý ghép nhóm Khởi nghiệp (EXE Team Matching)
### NHÓM 4

* **Chủ đề chi tiết:** Hệ thống ghép nhóm môn Khởi nghiệp (EXE101/EXE201) theo bản đồ kỹ năng (Skill Matrix) và định hướng đề tài dành cho sinh viên IT & Kinh tế chuẩn bị vào kỳ đồ án nhưng thiếu kết nối liên ngành.
* **Persona (1 dòng tóm tắt):** Lê Quốc Huy, 21 tuổi, sinh viên năm 3 Kỹ thuật phần mềm cần tìm đồng đội khối ngành Kinh tế/Marketing có cùng mức cam kết để chốt nhóm khởi nghiệp trước deadline 5 ngày.
* **Link Figma thiết kế (Public View):** https://www.figma.com/design/ZaGhw1hrYaguAZFcqruZMC/PRM323---Lab-2---EXE-Match?node-id=0-1

### Thành viên Nhóm 4:
| STT | Họ và tên | Vai trò / Đóng góp chính trong Lab 2 |
| :-: | :--- | :--- |
| 1 | Tăng Mình Trọng (Trưởng nhóm) | Phân tích UX Persona, User Flow, Viết Prompt Google Stitch |
| 2 | Phan Anh Tuấn | Xây dựng Design System, Phản biện 10 Usability Heuristics |
| 3 | Đỗ Anh Minh | Thiết kế Figma Components & Auto Layout |
| 4 | Lữ Phước Nhật Tú | Dựng Prototype tương tác & Đặc tả Flutter Handoff |

---

## 1. Danh sách công cụ AI đã sử dụng
1. **Google Stitch (hoặc công cụ AI UI tương đương):** Dùng để sinh phôi giao diện ban đầu từ văn bản mô tả (Prompt-to-UI).
2. **AI Assistant (ChatGPT / Claude / Gemini):** Đóng vai trò chuyên gia phản biện UI/UX theo 10 Heuristics của Nielsen và tiêu chuẩn tiếp cận WCAG 2.1.
3. **Figma AI Plugins (nếu có):** Hỗ trợ tạo dữ liệu mẫu (content placeholder) chân thực cho hồ sơ sinh viên.

---

## 2. Bản đồ nơi tìm từng sản phẩm (Product Deliverables Map)

| Sản phẩm bàn giao | Đường dẫn file trong Repository | Mô tả tóm tắt |
| :--- | :--- | :--- |
| **Phân tích Persona** | [`ux/persona.md`](ux/persona.md) | Chân dung người dùng, pain point, problem statement, tiêu chí thành công |
| **Kiến trúc thông tin & User Flows** | [`ux/user-flow.md`](ux/user-flow.md) | Cấu trúc 9 màn hình, 3 sơ đồ Mermaid (kèm nhánh lỗi/phục hồi), bảng ánh xạ |
| **Bản mô tả thiết kế** | [`design/DESIGN.md`](design/DESIGN.md) | Design token: bảng màu WCAG 2.1, typography, spacing, quy tắc 9 components |
| **Đặc tả màn hình** | [`design/screen-spec.md`](design/screen-spec.md) | Ý đồ thiết kế, nội dung và tương tác của từng màn hình |
| **Quyết định thiết kế & Accessibility** | [`design/design-decisions.md`](design/design-decisions.md) | 10 quyết định thiết kế quan trọng và checklist kiểm tra accessibility |
| **Nhật ký tương tác AI** | [`ai/ai-design-log.md`](ai/ai-design-log.md) | Nguyên văn prompt, kết quả, 3 vòng lặp tinh chỉnh và phản biện Heuristic |
| **Ảnh chụp kết quả Stitch** | [`assets/stitch/`](assets/stitch/) | Toàn bộ ảnh chụp màn hình UI do Google Stitch tạo ra |
| **Ảnh xuất Figma Final UI** | [`assets/figma/`](assets/figma/) | Ảnh PNG export các màn hình hoàn thiện từ Figma |
| **Đặc tả Flutter Handoff** | [`handoff/flutter-handoff.md`](handoff/flutter-handoff.md) | 6 mục đặc tả kỹ thuật từng màn hình + bảng ánh xạ Token sang Widget |
| **Kịch bản Slide Thuyết trình (12 Slides)** | [`docs/SLIDES.md`](docs/SLIDES.md) | Kịch bản 12 slide chi tiết, phân chia 4 người nói, speaker notes và Q&A |
| **Web Slide Tương tác & Xuất PDF** | [`docs/slides.html`](docs/slides.html) | Bản trình chiếu web chuẩn 16:9, điều hướng phím mũi tên, hỗ trợ xuất file PDF |
| **File Slide PowerPoint (.pptx)** | [`docs/PRM323_Lab2_Nhom4_Slides.pptx`](docs/PRM323_Lab2_Nhom4_Slides.pptx) | File PowerPoint 12 slide nhúng sẵn ảnh, kéo thả nhập trực tiếp vào Canva trong 3s |

---

## 3. Hướng dẫn Thuyết trình & Live Demo (Đánh giá Lab 2)
Tuân thủ 100% [Hướng dẫn trình bày Lab 2](https://prm393-material.web.app/lab2-presentation.html):
* **Thời lượng:** 10 phút thuyết trình (12 slide) · 5 phút live demo Figma · 5 phút hỏi đáp Q&A.
* **Cách mở Slide trình chiếu:**
  * Mở trực tiếp file [`docs/slides.html`](docs/slides.html) trong Google Chrome hoặc Microsoft Edge.
  * Phím tắt: `ArrowRight` (Tiếp), `ArrowLeft` (Lùi), `F` (Toàn màn hình), `N` (Bật/tắt lời thoại diễn giả).
  * Nhấn nút **"🖨️ Xuất PDF"** hoặc nhấn `Ctrl + P` (chọn Save as PDF) để in ra file PDF nộp thầy nếu cần.

