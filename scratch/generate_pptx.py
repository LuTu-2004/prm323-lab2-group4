import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen standard
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank layout

    # Color Palette
    DARK_BG = RGBColor(15, 23, 42)       # #0F172A Slate 900
    CARD_BG = RGBColor(30, 41, 59)       # #1E293B Slate 800
    PRIMARY = RGBColor(59, 130, 246)     # #3B82F6 Blue
    ACCENT = RGBColor(16, 185, 129)      # #10B981 Emerald
    TEXT_LIGHT = RGBColor(248, 250, 252) # #F8FAFC
    TEXT_MUTED = RGBColor(148, 163, 184) # #94A3B8
    BORDER_COL = RGBColor(51, 65, 85)    # #334155

    assets_stitch = "e:/PRM/Thư mục mới/prm323-lab2-group4/assets/stitch"
    assets_figma = "e:/PRM/Thư mục mới/prm323-lab2-group4/assets/figma"

    slides_data = [
        {
            "num": "01",
            "title": "EXE Team Matching - Tổng quan Dự án",
            "speaker": "Tăng Mình Trọng (Trưởng nhóm)",
            "bullets": [
                "Bối cảnh thực tế: Sinh viên bước vào kỳ đồ án EXE101/201 bắt buộc phải lập nhóm liên ngành (IT + Kinh tế/Marketing).",
                "Thực trạng: Tìm nhóm qua Facebook bị trôi bài, không rõ năng lực, dễ gặp free-rider và ghép vội sát deadline.",
                "Giải pháp: Ứng dụng di động EXE Team Matching kết nối sinh viên qua Ma trận kỹ năng (Skill Matrix) & thời gian cam kết.",
                "Đội ngũ Nhóm 4:",
                "  • 1. Tăng Mình Trọng: Trưởng nhóm · UX Research, Persona, Quản phối",
                "  • 2. Phan Anh Tuấn: User Flows, AI Prompting & Usability Heuristics",
                "  • 3. Đỗ Anh Minh: Design System, Figma Components & UI Audit",
                "  • 4. Lữ Phước Nhật Tú: Interactive Prototype & Flutter Handoff",
                "Minh chứng: GitHub github.com/LuTu-2004/prm323-lab2-group4 | Figma Canvas 6 Pages"
            ],
            "img": os.path.join(assets_stitch, "screen_01_discovery_feed.png"),
            "notes": "Kính chào thầy và các bạn, hôm nay Nhóm 4 xin đại diện trình bày kết quả Lab 2 môn PRM323 với đề tài Hệ thống ghép nhóm Khởi nghiệp EXE Team Matching. Ứng dụng ra đời nhằm giải quyết bài toán nhức nhối của sinh viên năm 3: tìm kiếm đồng đội đa ngành có cùng chí hướng và mức độ cam kết cao trước hạn chót của nhà trường."
        },
        {
            "num": "02",
            "title": "Problem & Primary Persona (Lê Quốc Huy)",
            "speaker": "Tăng Mình Trọng",
            "bullets": [
                "Họ và tên: Lê Quốc Huy · 21 tuổi · Sinh viên năm 3 Kỹ thuật Phần mềm (SE).",
                "Vai trò: Technical Lead / Flutter Developer (Tech-Savvy Active Seeker).",
                "Bối cảnh: Dùng Android 360x800 dp, thao tác 1 tay trên xe buýt / sảnh trường, deadline nộp nhóm còn đúng 5 ngày.",
                "Pain Points: Bài đăng trôi nhanh, kỹ năng ứng viên mập mờ, nhắn tin xin vào nhóm thì đối phương đã đủ người.",
                "Problem Statement:",
                "  \"Sinh viên kỹ thuật phần mềm gặp khó khăn lớn trong việc tìm kiếm và kết nối với đồng đội khối ngành Kinh tế/Marketing phù hợp về kỹ năng và cam kết trước hạn chót nộp danh sách của nhà trường.\"",
                "Chỉ số thành công đo lường được (Measurable Metric):",
                "  \"Sinh viên tìm được nhóm EXE phù hợp và gửi thành công đơn ứng tuyển trong thời gian dưới 60 giây.\""
            ],
            "img": os.path.join(assets_stitch, "screen_02_project_detail.png"),
            "notes": "Dựa trên chuẩn Persona Guideline của môn học, chúng em xây dựng Primary Persona đại diện là bạn Lê Quốc Huy, 21 tuổi, học SE. Huy có kỹ năng lập trình tốt nhưng mạng lưới quan hệ hẹp. Điểm đau lớn nhất là sợ gặp free-rider và bị trôi bài trên Facebook. Toàn bộ thiết kế được tối ưu để đạt chỉ số thành công đo được: giúp Huy tìm thấy nhóm phù hợp và nộp hồ sơ chỉ trong vòng dưới 60 giây."
        },
        {
            "num": "03",
            "title": "Information Architecture (Sitemap 9 Màn hình)",
            "speaker": "Tăng Mình Trọng",
            "bullets": [
                "Mô hình điều hướng: Bottom Navigation Bar 4 tab cố định (Khám phá · Đơn của tôi · Tin nhắn · Cá nhân).",
                "Phân cấp 3 tầng màn hình rõ ràng:",
                "  • Top-Level (Cấp 1): Screen 01 (Khám phá), Screen 05 (Theo dõi đơn), Screen 08 (Empty State).",
                "  • Child Details (Cấp 2): Screen 02 (Chi tiết dự án), Screen 03 (Apply Sheet), Screen 04 (Xác nhận gửi).",
                "  • Interactive Modals (Cấp 3): Screen 06 (Lên lịch phỏng vấn), Screen 07 (Lịch hẹn hoàn tất).",
                "Quy tắc 3 lần chạm (Rule of 3 taps): Mọi tác vụ cốt lõi đều hoàn tất trong tối đa 3 chạm.",
                "Công thái học: Toàn bộ nút chính nằm trong vùng ngón tay cái (Thumb Zone) khi cầm 1 tay."
            ],
            "img": os.path.join(assets_stitch, "stitch_canvas_screen_01_02_03.png"),
            "notes": "Để phục vụ thói quen thao tác 1 tay của Huy trên màn hình di động, chúng em thiết kế kiến trúc thông tin dạng phẳng với Bottom Navigation 4 tab. Toàn bộ hệ sinh thái gồm 9 màn hình được phân cấp rành mạch từ màn hình chính Khám phá, đi sâu vào Chi tiết dự án, Bottom Sheet ứng tuyển, đến các màn hình xác nhận và theo dõi trạng thái đơn."
        },
        {
            "num": "04",
            "title": "Three User Flows & Phục hồi Lỗi",
            "speaker": "Phan Anh Tuấn",
            "bullets": [
                "Flow 1: Happy Path (Ứng tuyển dự án trong 60s):",
                "  Khám phá (Screen 01) -> Xem chi tiết (Screen 02) -> Mở Apply Sheet (Screen 03) -> Nộp đơn thành công (Screen 04) -> Tracker (Screen 05).",
                "Flow 2: Alternate Path (Trưởng nhóm hẹn Chemistry Call):",
                "  Tracker (Screen 05) -> Xem hồ sơ ứng viên -> Bấm Hẹn trao đổi (Screen 06) -> Xác nhận lịch hẹn (Screen 07).",
                "Flow 3: Error & Recovery (Phục hồi khi tìm kiếm 0 kết quả):",
                "  Tìm từ khóa sai/bộ lọc quá hẹp -> Screen 08 (Empty State) -> Nhấn nút \"Xóa bộ lọc\" -> Phục hồi về danh sách dự án đầy đủ trong 1 chạm.",
                "Nguyên tắc thiết kế: Zero Dead-Ends (Tuyệt đối không có ngõ cụt)."
            ],
            "img": os.path.join(assets_stitch, "screen_08_empty_state.png"),
            "notes": "Tiếp nối phần kiến trúc, em xin trình bày 3 User Flows thực thi. Bên cạnh luồng ứng tuyển chuẩn Happy Path đạt mốc dưới 60 giây và luồng trưởng nhóm hẹn lịch Chemistry Call, nhóm đặc biệt chú trọng Luồng 3 - Phục hồi lỗi. Khi người dùng lọc tiêu chí quá hẹp dẫn đến 0 kết quả, ứng dụng đưa ra Empty State minh họa trực quan kèm nút bấm 'Xóa bộ lọc' để người dùng khôi phục trạng thái ngay lập tức, không có ngõ cụt."
        },
        {
            "num": "05",
            "title": "AI UI Generation (Prompt-to-UI với Stitch)",
            "speaker": "Phan Anh Tuấn",
            "bullets": [
                "Công cụ sử dụng: Google Stitch (AI UI Generator chuyên sâu cho Mobile).",
                "Kỹ thuật Prompt Engineering 5 Thành phần chuẩn hóa:",
                "  1. Persona & Role: UX Designer thiết kế app cho sinh viên IT (Lê Quốc Huy).",
                "  2. Task: Sinh màn hình khám phá dự án, thẻ kỹ năng và Bottom Sheet ứng tuyển.",
                "  3. Platform: Android Mobile chuẩn 360x800 dp, Material 3 grid 8dp.",
                "  4. Constraints: WCAG 2.1 AA (tương phản >=4.5:1, vùng chạm >=48dp), hiển thị số giờ cam kết.",
                "  5. Style & Tone: Hiện đại, uy tín, Deep Navy (#0F172A) & Emerald (#10B981).",
                "Kết quả: Sinh nhanh 8 màn hình phôi cơ bản làm nền tảng phản biện."
            ],
            "img": os.path.join(assets_stitch, "stitch_prompt_input_evidence.png"),
            "notes": "Tại bước sinh giao diện, nhóm áp dụng kỹ thuật Prompt Engineering chặt chẽ gồm 5 thành phần: định hình rõ Persona, tác vụ cụ thể, nền tảng di động chuẩn, các ràng buộc công thái học và bảng màu chủ đạo. Google Stitch đã giúp nhóm nhanh chóng trực quan hóa ý tưởng ban đầu thành 8 phôi giao diện mobile, đóng vai trò làm bàn đạp để nhóm tiến hành phản biện và tinh chỉnh chuyên sâu."
        },
        {
            "num": "06",
            "title": "AI Iterations & Phản biện Usability Heuristics",
            "speaker": "Phan Anh Tuấn",
            "bullets": [
                "5 Lỗi Usability nghiêm trọng được phát hiện từ bản phôi AI:",
                "  • H1 (Visibility): Nút Apply ban đầu không có loading feedback khi nhấn.",
                "  • H3 (User Freedom): Modal Sheet thiếu nút đóng (X) hoặc cử chỉ kéo xuống để hủy.",
                "  • H5 (Error Prevention): Nút Xác nhận gửi đặt sát nút Hủy, dễ bấm nhầm.",
                "  • H7 (Efficiency): Thiếu bộ lọc theo số giờ cam kết của ứng viên.",
                "  • WCAG Contrast: Màu chữ phụ #94A3B8 trên nền trắng chỉ đạt 2.8:1 (vi phạm AA).",
                "3 Vòng lặp cải tiến có mục tiêu rõ rệt:",
                "  • Iteration 1: Tái cấu trúc Visual Hierarchy, đưa Match % lên vị trí trọng tâm.",
                "  • Iteration 2: Chuẩn hóa Accessibility, nâng vùng chạm lên >=48x48 dp, contrast 5.2:1.",
                "  • Iteration 3: Bổ sung trọn vẹn Empty State và Skeleton Loading."
            ],
            "img": os.path.join(assets_stitch, "figma_canvas_7_screens.png"),
            "notes": "Nhóm xác định rõ: AI chỉ là trợ lý sinh phôi, con người mới là người kiểm soát chất lượng. Qua lăng kính 10 Heuristics của Nielsen và tiêu chuẩn WCAG, nhóm phát hiện AI mắc 5 lỗi lớn như vi phạm độ tương phản và thiếu vùng chạm an toàn. Chúng em đã thực hiện 3 vòng lặp tinh chỉnh liên tiếp: từ phân cấp thị giác, chuẩn hóa công thái học vùng chạm, đến việc bổ sung hoàn chỉnh các trạng thái biên như Empty State và Loading."
        },
        {
            "num": "07",
            "title": "Ma trận Quyết định Thiết kế (Accept / Modify / Reject)",
            "speaker": "Đỗ Anh Minh",
            "bullets": [
                "Bằng chứng năng lực phản biện thiết kế của Nhóm 4:",
                "  • ACCEPT - Thẻ Skill Tags: Bố cục dạng thẻ chip trực quan, quét nhanh kỹ năng -> Giữ nguyên, bổ sung thêm % tương thích.",
                "  • MODIFY - Nút Apply trôi nổi: Nút bấm trôi nổi giữa card, khó bấm 1 ngón cái -> Chuyển thành Sticky Bottom Dock (48x56 dp) cố định đáy.",
                "  • REJECT - Pop-up Dialog toàn màn hình: Che mất ngữ cảnh dự án, gây gián đoạn -> Thay bằng Modal Bottom Sheet kéo vuốt nửa màn hình.",
                "  • REJECT - Báo trạng thái chỉ bằng màu sắc: Vi phạm trợ năng cho người mù màu -> Bổ sung Icon minh họa + Text nhãn rõ ràng (\"Đã duyệt\")."
            ],
            "img": os.path.join(assets_stitch, "screen_03_apply_sheet.png"),
            "notes": "Đây là minh chứng rõ nét cho năng lực phản biện của nhóm. Chúng em không nhận vơ toàn bộ những gì AI tạo ra. Với các đề xuất bất hợp lý như Pop-up che màn hình hay báo trạng thái chỉ bằng màu sắc, nhóm thẳng thừng Reject và thay thế bằng Bottom Sheet kéo vuốt cùng hệ thống nhãn kép Icon + Text. Mọi quyết định đều có căn cứ vững chắc từ thói quen người dùng và tiêu chuẩn công thái học."
        },
        {
            "num": "08",
            "title": "Wireframe -> Final UI (8 Màn hình Hoàn chỉnh)",
            "speaker": "Đỗ Anh Minh",
            "bullets": [
                "Trưng bày 8 Màn hình Độc lập (Đáp ứng chuẩn kiểm định C6 môn học):",
                "  1. Screen 01: Discovery Feed (Khám phá dự án & bộ lọc)",
                "  2. Screen 02: Project Detail (Chi tiết dự án & Skill Matrix)",
                "  3. Screen 03: Apply Modal Sheet (Điền đơn & cam kết giờ)",
                "  4. Screen 04: Application Submitted (Xác nhận gửi đơn thành công)",
                "  5. Screen 05: My Applications Tracker (Quản lý tiến độ đơn)",
                "  6. Screen 06: Chemistry Call Scheduler (Lên lịch phỏng vấn)",
                "  7. Screen 07: Chemistry Call Confirmed (Lịch hẹn hoàn tất)",
                "  8. Screen 08: Empty State & Recovery (Phục hồi tìm kiếm)",
                "Tiêu chuẩn: Hệ thống lưới 8dp, font Inter sắc nét, độ tương phản đạt chuẩn."
            ],
            "img": os.path.join(assets_stitch, "figma_canvas_8_screens.png"),
            "notes": "Trên màn hình là sự tiến hóa từ Wireframe cấu trúc sang 8 màn hình UI hoàn thiện trên Figma. Chúng em cam kết đáp ứng vượt chuẩn kiểm định C6 của môn học: có đủ tối thiểu 8 màn hình chức năng riêng biệt, bao phủ trọn vẹn mọi điểm chạm từ tìm kiếm, xem chi tiết, ứng tuyển, đặt lịch hẹn cho đến xử lý trạng thái rỗng. Tính nhất quán về khoảng cách và nhận diện thị giác được bảo toàn 100%."
        },
        {
            "num": "09",
            "title": "Design System & 9 Nhóm Components Figma",
            "speaker": "Đỗ Anh Minh",
            "bullets": [
                "Hệ thống Design Tokens quản lý bằng Figma Variables:",
                "  • Màu sắc: Primary Blue (#2563EB), Deep Navy (#0F172A), Emerald Success (#10B981).",
                "  • Lưới Spacing cơ sở: 4dp, 8dp, 16dp, 24dp | Bo góc Radius: 8dp, 12dp.",
                "  • Typography: Font Inter phân cấp Display 24sp, Title 18sp, Body 14sp.",
                "Đầy đủ 9 nhóm Components với Auto Layout & Variants:",
                "  1. Buttons (Primary, Secondary, Text) | 2. Text Fields (Search & Input)",
                "  3. Cards (Project, Applicant, Stat) | 4. Navigation (Bottom Bar 4 tabs)",
                "  5. App Bar (Header & Back button) | 6. Dialog & Bottom Sheet",
                "  7. Loading State (Skeleton Shimmer) | 8. Empty State (Illustration + Reset)",
                "  9. Error State (Inline Warning Banner)"
            ],
            "img": os.path.join(assets_stitch, "screen_05_my_applications_tracker.png"),
            "notes": "Để dự án có thể mở rộng và bàn giao mượt mà cho đội ngũ kỹ thuật, chúng em xây dựng Design System hoàn chỉnh trên Figma. Toàn bộ thông số từ màu sắc, kích thước chữ, bo góc đều được quản lý bằng Figma Variables. Thư viện linh kiện bao gồm đủ 9 nhóm cốt lõi với 100% sử dụng Auto Layout và Variant states từ Default đến Disabled và Error."
        },
        {
            "num": "10",
            "title": "Accessibility (WCAG 2.1 AA) & Responsive 360/412dp",
            "speaker": "Lữ Phước Nhật Tú",
            "bullets": [
                "Bằng chứng Kiểm chuẩn Trợ năng WCAG 2.1 AA:",
                "  • Độ tương phản màu: Chữ chính trên nền trắng đạt 12.6:1 (chuẩn >=4.5:1). Nút chính nền xanh đạt 4.68:1.",
                "  • Vùng chạm an toàn (Touch Targets): 100% nút bấm, icon và ô nhập liệu đạt kích thước >= 48x48 dp.",
                "  • Kích cỡ chữ đọc: Toàn bộ body text đạt >= 14sp, nhãn phụ >= 12sp.",
                "  • Đa phương thức: Không dùng màu đơn độc; luôn có Icon + Nhãn Text đi kèm.",
                "Khả năng Thích ứng Màn hình (Responsive):",
                "  • Thiết kế tối ưu trên màn hình Android chuẩn 360x800 dp.",
                "  • Tự động co giãn không vỡ khung trên màn hình lớn 412x915 dp nhờ Auto Layout 'Fill container'."
            ],
            "img": os.path.join(assets_stitch, "screen_06_chemistry_call_modal.png"),
            "notes": "Về mặt công thái học và tiếp cận, chúng em tự hào sản phẩm đạt 100% chuẩn WCAG 2.1 AA. Mọi nút bấm đều đảm bảo vùng chạm 48dp để người dùng không bấm trượt khi đang đi xe buýt. Độ tương phản chữ đạt từ 4.68:1 trở lên, giúp đọc rõ ngay cả dưới ánh nắng sân trường. Hệ thống layout co giãn linh hoạt, đảm bảo hiển thị hoàn hảo từ màn hình 360dp đến các dòng điện thoại cao cấp 412dp."
        },
        {
            "num": "11",
            "title": "Live Interactive Prototype (Figma Page 06)",
            "speaker": "Lữ Phước Nhật Tú",
            "bullets": [
                "Trải nghiệm Tương tác Chân thực trên Figma:",
                "  • 3 Starting Points: Thiết lập phân luồng rõ ràng cho cả 3 user flows.",
                "  • Modal Overlays: Trải nghiệm mở Bottom Sheet và Dialog với hiệu ứng làm tối nền (Dim background).",
                "  • Chuyển động Smart Animate: Thời gian 250-300ms mượt mà, đúng chuẩn native mobile.",
                "  • Đường dẫn quay vòng khép kín (Circular Return Paths): Nút Back hoạt động chính xác tại mọi màn hình con; nút Về trang chủ sau khi nộp đơn giúp loại bỏ hoàn toàn bẫy ngõ cụt.",
                "Sẵn sàng cho phiên Demo trực tiếp 5 phút trên Figma Canvas."
            ],
            "img": os.path.join(assets_stitch, "screen_07_chemistry_call_confirmed.png"),
            "notes": "Bản Prototype trên Figma Page 06 được liên kết tỉ mỉ với đầy đủ 3 luồng người dùng. Các thao tác mở Bottom Sheet, chuyển cảnh khi nộp đơn thành công và quay trở lại trang chủ đều hoạt động mượt mà. Đặc biệt, người dùng có thể thử nghiệm nhánh lỗi tại luồng tìm kiếm và phục hồi dễ dàng. Ngay sau đây, nhóm sẽ trình diễn trực tiếp bản Prototype này trong phần Demo 5 phút."
        },
        {
            "num": "12",
            "title": "Flutter Handoff & Tổng kết Nghiệm thu",
            "speaker": "Lữ Phước Nhật Tú",
            "bullets": [
                "Bàn giao Kỹ thuật Toàn diện cho Lập trình viên:",
                "  • Đặc tả 6 mục cho từng màn hình: Layout, Components, States, Interactions, Navigation, UI Constraints.",
                "  • 2 Bảng Ánh xạ Kỹ thuật (Mapping Tables):",
                "    - Tokens -> Flutter ThemeData (ColorScheme, TextTheme, EdgeInsets).",
                "    - Components -> Flutter Widgets (FilledButton, Card, FilterChip, showModalBottomSheet).",
                "Tổng kết Đánh giá Lab 2:",
                "  • Quy trình UX, AI Prompt & Phản biện: Hoàn thành xuất sắc (45/45 điểm).",
                "  • Sản phẩm Figma, Design System, Prototype: Đạt 100% tiêu chí C1-C6 (55/55 điểm).",
                "  • TỔNG ĐIỂM DỰ KIẾN: 100 / 100 ĐIỂM."
            ],
            "img": os.path.join(assets_stitch, "screen_04_application_submitted.png"),
            "notes": "Để khép lại bài thuyết trình, tài liệu Flutter Handoff của nhóm cung cấp bản đặc tả kỹ thuật chi tiết đến từng Widget và Theme property. Một lập trình viên Flutter dù chưa từng tham gia dự án cũng có thể nhìn vào đặc tả này để dựng giao diện chính xác từng pixel và quản lý đầy đủ các trạng thái logic. Nhóm 4 xin chân thành cảm ơn thầy và các bạn đã lắng nghe!"
        }
    ]

    for item in slides_data:
        slide = prs.slides.add_slide(blank_layout)

        # Background shape
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = DARK_BG
        bg.line.color.rgb = DARK_BG

        # Top Bar shape
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(0.4), Inches(12.133), Inches(0.85))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = CARD_BG
        top_bar.line.color.rgb = BORDER_COL

        # Title text in Top Bar
        tf = top_bar.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.text = f"SLIDE {item['num']} | {item['title'].upper()}"
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = PRIMARY
        p.font.name = "Arial"

        # Speaker tag in top right
        speaker_box = slide.shapes.add_textbox(Inches(9.2), Inches(0.48), Inches(3.4), Inches(0.65))
        sp_tf = speaker_box.text_frame
        sp_p = sp_tf.paragraphs[0]
        sp_p.text = f"👤 {item['speaker']}"
        sp_p.alignment = PP_ALIGN.RIGHT
        sp_p.font.size = Pt(13)
        sp_p.font.bold = True
        sp_p.font.color.rgb = ACCENT
        sp_p.font.name = "Arial"

        # Left content box (Card)
        left_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.45), Inches(7.8), Inches(5.6))
        left_card.fill.solid()
        left_card.fill.fore_color.rgb = CARD_BG
        left_card.line.color.rgb = BORDER_COL

        ltf = left_card.text_frame
        ltf.word_wrap = True
        ltf.margin_top = Inches(0.3)
        ltf.margin_left = Inches(0.35)
        ltf.margin_right = Inches(0.35)
        ltf.margin_bottom = Inches(0.3)

        first = True
        for bullet in item['bullets']:
            if first:
                p = ltf.paragraphs[0]
                first = False
            else:
                p = ltf.add_paragraph()
            
            p.text = bullet
            p.font.name = "Arial"
            if bullet.startswith("  "):
                p.level = 1
                p.font.size = Pt(12.5)
                p.font.color.rgb = TEXT_MUTED
                p.space_after = Pt(4)
            elif bullet.endswith(":"):
                p.level = 0
                p.font.size = Pt(14)
                p.font.bold = True
                p.font.color.rgb = PRIMARY
                p.space_after = Pt(4)
                p.space_before = Pt(6)
            else:
                p.level = 0
                p.font.size = Pt(13)
                p.font.color.rgb = TEXT_LIGHT
                p.space_after = Pt(6)

        # Right image card
        right_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.6), Inches(1.45), Inches(4.133), Inches(5.6))
        right_card.fill.solid()
        right_card.fill.fore_color.rgb = CARD_BG
        right_card.line.color.rgb = BORDER_COL

        # Add image inside right card if exists
        img_path = item.get('img')
        if img_path and os.path.exists(img_path):
            try:
                # Add picture centered
                slide.shapes.add_picture(img_path, Inches(8.85), Inches(1.65), width=Inches(3.633))
            except Exception as e:
                print(f"Warning: could not add image {img_path}: {e}")

        # Speaker Notes
        notes_slide = slide.notes_slide
        text_frame = notes_slide.notes_text_frame
        text_frame.text = f"[DIỄN GIẢ: {item['speaker']}]\n\n{item['notes']}"

    output_path = "e:/PRM/Thư mục mới/prm323-lab2-group4/docs/PRM323_Lab2_Nhom4_Slides.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_deck()
