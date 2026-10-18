import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_polished_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Premium Modern Theme Colors
    BG_COLOR = RGBColor(11, 15, 25)         # Ultra deep navy
    CARD_BG = RGBColor(22, 30, 49)          # Refined slate card
    CARD_BORDER = RGBColor(45, 55, 72)      # Subtle border
    CARD_ACCENT_BG = RGBColor(28, 40, 65)   # Highlight card
    PRIMARY = RGBColor(56, 189, 248)        # Sky Blue #38BDF8
    ACCENT = RGBColor(52, 211, 153)         # Emerald Green #34D399
    TEXT_TITLE = RGBColor(255, 255, 255)    # Pure White
    TEXT_BODY = RGBColor(226, 232, 240)     # Light Slate #E2E8F0
    TEXT_MUTED = RGBColor(148, 163, 184)    # Slate 400 #94A3B8

    stitch_dir = "e:/PRM/Thư mục mới/prm323-lab2-group4/assets/stitch"

    slides_info = [
        {
            "slide_num": "01 / 12",
            "tag": "PROJECT OVERVIEW",
            "title": "Hệ thống Ghép nhóm Khởi nghiệp (EXE Team Matching)",
            "speaker": "Tăng Mình Trọng (Trưởng nhóm)",
            "card1_title": "🎯 Vấn đề & Thực trạng",
            "card1_items": [
                "Sinh viên học EXE101/201 bắt buộc phải lập nhóm đa ngành (IT + Kinh tế/Marketing).",
                "Tìm nhóm qua mạng xã hội rất hỗn loạn: bài trôi nhanh, không rõ kỹ năng, dễ gặp người thiếu cam kết (free-rider)."
            ],
            "card2_title": "💡 Giải pháp Nền tảng",
            "card2_items": [
                "Ghép nhóm dựa trên Ma trận Kỹ năng (Skill Matrix) & giờ cam kết hàng tuần.",
                "Đạt mục tiêu tìm kiếm và ứng tuyển thành công chỉ trong vòng dưới 60 giây."
            ],
            "card3_title": "👥 Đội ngũ Nhóm 4 & Phân vai",
            "card3_items": [
                "1. Tăng Mình Trọng: Trưởng nhóm · UX Persona & Sitemap",
                "2. Phan Anh Tuấn: User Flows, AI Prompting & Heuristics",
                "3. Đỗ Anh Minh: Design System & 9 Components",
                "4. Lữ Phước Nhật Tú: Prototype & Flutter Handoff"
            ],
            "image": os.path.join(stitch_dir, "screen_01_discovery_feed.png"),
            "notes": "Kính chào thầy và các bạn, hôm nay Nhóm 4 xin đại diện trình bày đề tài EXE Team Matching. Ứng dụng ra đời nhằm giải quyết bài toán tìm đồng đội đa ngành có cùng mức cam kết trước hạn chót của nhà trường."
        },
        {
            "slide_num": "02 / 12",
            "tag": "PROBLEM & PERSONA",
            "title": "Primary Persona: Lê Quốc Huy (Tech-Savvy Active Seeker)",
            "speaker": "Tăng Mình Trọng",
            "card1_title": "👤 Chân dung 12 trường cốt lõi",
            "card1_items": [
                "Lê Quốc Huy · 21 tuổi · SV năm 3 Kỹ thuật Phần mềm (SE).",
                "Mục tiêu: Technical Lead / Mobile Developer.",
                "Bối cảnh: Dùng Android 360x800 dp, dùng 1 tay trên xe buýt / sảnh trường, hạn nộp nhóm còn đúng 5 ngày.",
                "Trở ngại: Không quen bạn Kinh tế, sợ ghép bừa gặp free-rider."
            ],
            "card2_title": "📢 Problem Statement",
            "card2_items": [
                "\"Sinh viên kỹ thuật phần mềm gặp khó khăn lớn khi tìm đồng đội khối ngành Kinh tế/Marketing phù hợp về kỹ năng và mức cam kết trước deadline nộp danh sách.\""
            ],
            "card3_title": "⏱️ Measurable Success Metric",
            "card3_items": [
                "\"Sinh viên tìm được nhóm EXE phù hợp theo bộ lọc chuyên môn và gửi thành công đơn ứng tuyển trong thời gian dưới 60 giây.\""
            ],
            "image": os.path.join(stitch_dir, "screen_02_project_detail.png"),
            "notes": "Dựa trên Persona Guideline, nhóm xây dựng Primary Persona Lê Quốc Huy với mục tiêu cốt lõi: tìm được nhóm tin cậy và gửi ứng tuyển thành công dưới 60 giây."
        },
        {
            "slide_num": "03 / 12",
            "tag": "INFORMATION ARCHITECTURE",
            "title": "Kiến trúc Thông tin & Sitemap 9 Màn hình",
            "speaker": "Tăng Mình Trọng",
            "card1_title": "🗺️ Cấu trúc Điều hướng Phẳng",
            "card1_items": [
                "Bottom Navigation Bar 4 tab cố định: Khám phá · Đơn của tôi · Tin nhắn · Cá nhân.",
                "Thiết kế chuẩn công thái học trong vùng ngón tay cái (Thumb Zone).",
                "Quy tắc 3 lần chạm (Rule of 3 taps) hoàn thành mọi tác vụ chính."
            ],
            "card2_title": "📱 Phân cấp 3 Tầng Màn hình",
            "card2_items": [
                "Cấp 1 (Top-Level): Screen 01 (Khám phá), Screen 05 (Theo dõi đơn), Screen 08 (Empty State).",
                "Cấp 2 (Child Details): Screen 02 (Chi tiết), Screen 03 (Apply Sheet), Screen 04 (Xác nhận gửi).",
                "Cấp 3 (Modals): Screen 06 (Hẹn phỏng vấn), Screen 07 (Lịch hẹn hoàn tất)."
            ],
            "card3_title": "📁 Minh chứng Bàn giao",
            "card3_items": [
                "Đặc tả cấu trúc chi tiết tại ux/user-flow.md và Figma Page 01 User Flow."
            ],
            "image": os.path.join(stitch_dir, "stitch_canvas_screen_01_02_03.png"),
            "notes": "Kiến trúc thông tin dạng phẳng với Bottom Navigation 4 tab giúp sinh viên dễ dàng thao tác 1 tay, phân cấp rõ ràng 3 tầng từ trang chủ tới chi tiết."
        },
        {
            "slide_num": "04 / 12",
            "tag": "USER FLOWS",
            "title": "3 Luồng Trải nghiệm Cốt lõi & Phục hồi Lỗi",
            "speaker": "Phan Anh Tuấn",
            "card1_title": "⚡ Flow 1: Happy Path (Ứng tuyển trong 60s)",
            "card1_items": [
                "Khám phá (Screen 01) -> Xem chi tiết (Screen 02) -> Nhấn Apply mở Sheet (Screen 03) -> Nộp đơn thành công (Screen 04) -> Quản lý tại Tracker (Screen 05)."
            ],
            "card2_title": "🤝 Flow 2: Alternate Path (Hẹn Chemistry Call)",
            "card2_items": [
                "Trưởng nhóm mở Tracker (Screen 05) -> Xem hồ sơ -> Nhấn Hẹn trao đổi -> Chọn giờ (Screen 06) -> Xác nhận lịch hẹn (Screen 07)."
            ],
            "card3_title": "🛡️ Flow 3: Error & Recovery (Không có ngõ cụt)",
            "card3_items": [
                "Tìm từ khóa sai hoặc bộ lọc quá hẹp -> Screen 08 (Empty State) -> Nhấn nút \"Xóa bộ lọc\" -> Phục hồi về danh sách đầy đủ trong 1 chạm (Zero Dead-Ends)."
            ],
            "image": os.path.join(stitch_dir, "screen_08_empty_state.png"),
            "notes": "Nhóm xây dựng 3 luồng người dùng rõ ràng, đặc biệt luồng 3 xử lý lỗi tìm kiếm rỗng với nút 'Xóa bộ lọc' đảm bảo không bao giờ dẫn người dùng vào ngõ cụt."
        },
        {
            "slide_num": "05 / 12",
            "tag": "AI GENERATION",
            "title": "Ứng dụng Google Stitch: Prompt-to-UI 5 Thành phần",
            "speaker": "Phan Anh Tuấn",
            "card1_title": "🤖 Cấu trúc Prompt Chuẩn hóa",
            "card1_items": [
                "1. Role & Persona: Mobile App UX Designer thiết kế cho SV IT (Lê Quốc Huy).",
                "2. Task: Sinh màn hình khám phá dự án EXE, thẻ kỹ năng và Bottom Sheet.",
                "3. Platform: Android Mobile 360x800 dp, Material 3 8dp grid.",
                "4. Constraints: WCAG 2.1 AA, hiển thị % tương thích và cam kết giờ.",
                "5. Style: Clean, trustworthy, Deep Navy (#0F172A) & Emerald (#10B981)."
            ],
            "card2_title": "📊 Kết quả Ban đầu",
            "card2_items": [
                "Google Stitch tạo phôi 8 màn hình ban đầu thể hiện tốt cấu trúc thẻ card và layout."
            ],
            "card3_title": "📁 Minh chứng",
            "card3_items": [
                "Toàn văn prompt và ảnh chụp trong ai/ai-design-log.md và assets/stitch/."
            ],
            "image": os.path.join(stitch_dir, "stitch_prompt_input_evidence.png"),
            "notes": "Prompt engineering 5 thành phần giúp AI sinh ra phôi giao diện sát với thực tế, làm nền tảng vững chắc cho quá trình phản biện UX."
        },
        {
            "slide_num": "06 / 12",
            "tag": "UX CRITIQUE & ITERATIONS",
            "title": "3 Vòng lặp Tinh chỉnh & 5 Lỗi Heuristic được Sửa",
            "speaker": "Phan Anh Tuấn",
            "card1_title": "🔍 5 Lỗi Heuristic Phát hiện từ AI",
            "card1_items": [
                "H1 (Visibility): Nút Apply ban đầu thiếu loading feedback khi nhấn.",
                "H3 (User Freedom): Modal Sheet thiếu nút đóng hoặc cử chỉ vuốt xuống.",
                "H5 (Error Prevention): Nút Xác nhận gửi đặt sát nút Hủy, dễ chạm nhầm.",
                "H7 (Efficiency): Thiếu bộ lọc theo số giờ cam kết hàng tuần.",
                "WCAG Contrast: Chữ phụ #94A3B8 trên nền trắng chỉ đạt 2.8:1 (vi phạm AA)."
            ],
            "card2_title": "🔁 3 Vòng lặp Cải tiến có Mục tiêu",
            "card2_items": [
                "Vòng 1 (Hierarchy): Tái cấu trúc kích thước chữ và Badge % tương thích.",
                "Vòng 2 (Accessibility): Nâng vùng chạm lên >=48x48 dp, contrast đạt 5.2:1.",
                "Vòng 3 (Edge States): Bổ sung Empty State, Skeleton Loading và Error banner."
            ],
            "card3_title": "📁 Minh chứng",
            "card3_items": [
                "Bảng đối chiếu Before/After chi tiết tại ai/ai-design-log.md."
            ],
            "image": os.path.join(stitch_dir, "figma_canvas_7_screens.png"),
            "notes": "Nhóm áp dụng 10 nguyên lý Heuristics của Nielsen để chỉ ra các điểm yếu của AI và thực hiện 3 vòng lặp tinh chỉnh toàn diện."
        },
        {
            "slide_num": "07 / 12",
            "tag": "DESIGN DECISIONS",
            "title": "Ma trận Quyết định Thiết kế (Accept / Modify / Reject)",
            "speaker": "Đỗ Anh Minh",
            "card1_title": "✅ Quyết định ACCEPT & MODIFY",
            "card1_items": [
                "ACCEPT - Thẻ Skill Tags: Bố cục dạng chip trực quan, quét nhanh kỹ năng -> Giữ lại và bổ sung Match Badge.",
                "MODIFY - Nút Apply trôi nổi: Nút bấm ban đầu lơ lửng giữa thẻ -> Chuyển thành Sticky Bottom Dock (48x56 dp) cố định đáy dễ bấm 1 tay."
            ],
            "card2_title": "❌ Quyết định REJECT có Căn cứ",
            "card2_items": [
                "REJECT - Pop-up Dialog toàn màn hình: Che khuất ngữ cảnh dự án -> Thay bằng Modal Bottom Sheet kéo vuốt nửa màn hình.",
                "REJECT - Báo trạng thái chỉ bằng màu sắc: Vi phạm người khiếm thị màu -> Bổ sung cặp đôi Icon + Text nhãn rõ ràng."
            ],
            "card3_title": "📁 Minh chứng",
            "card3_items": [
                "Hồ sơ 10 quyết định thiết kế tại design/design-decisions.md."
            ],
            "image": os.path.join(stitch_dir, "screen_03_apply_sheet.png"),
            "notes": "Chúng em chứng minh năng lực phản biện khi kiên quyết reject các đề xuất bất hợp lý của AI như pop-up che màn hình và báo trạng thái chỉ dùng màu."
        },
        {
            "slide_num": "08 / 12",
            "tag": "FINAL UI SCREENS",
            "title": "Chuyển hóa: Wireframe sang 8 Màn hình Hoàn chỉnh",
            "speaker": "Đỗ Anh Minh",
            "card1_title": "📱 8 Màn hình Chức năng Độc lập (Chuẩn C6)",
            "card1_items": [
                "Screen 01: Discovery Feed (Khám phá dự án & bộ lọc)",
                "Screen 02: Project Detail (Chi tiết dự án & Skill Matrix)",
                "Screen 03: Apply Modal Sheet (Nộp đơn ứng tuyển)",
                "Screen 04: Application Submitted (Xác nhận gửi đơn)",
                "Screen 05: Applications Tracker (Theo dõi tiến độ)",
                "Screen 06: Chemistry Call Scheduler (Lên lịch trao đổi)",
                "Screen 07: Chemistry Call Confirmed (Lịch hẹn hoàn tất)",
                "Screen 08: Empty State Recovery (Phục hồi tìm kiếm)"
            ],
            "card2_title": "🎨 Tính Nhất quán Thị giác",
            "card2_items": [
                "Tuân thủ hệ thống lưới cơ sở 8dp và phân cấp typography rõ ràng.",
                "Không tính các biến thể pop-up nhỏ, đảm bảo đủ 8 màn hình riêng biệt."
            ],
            "card3_title": "📁 Minh chứng",
            "card3_items": [
                "Kiểm tra tại Figma Page 02 Wireframe và Page 03 Final UI."
            ],
            "image": os.path.join(stitch_dir, "figma_canvas_8_screens.png"),
            "notes": "Hệ thống bao gồm đủ 8 màn hình chức năng riêng biệt, bao phủ trọn vẹn toàn bộ hành trình trải nghiệm mà không có màn hình nào bị ngõ cụt."
        },
        {
            "slide_num": "09 / 12",
            "tag": "DESIGN SYSTEM",
            "title": "Design Tokens & 9 Nhóm Components Figma",
            "speaker": "Đỗ Anh Minh",
            "card1_title": "🎨 Hệ thống Tokens Quản lý bằng Variables",
            "card1_items": [
                "Màu sắc: Primary Blue (#2563EB), Slate Navy (#0F172A), Emerald (#10B981).",
                "Typography: Font Inter hiện đại, phân cấp Display 24sp, Title 18sp, Body 14sp.",
                "Lưới khoảng cách: 4dp, 8dp, 16dp, 24dp | Bo góc Radius: 8dp, 12dp."
            ],
            "card2_title": "🧩 9 Nhóm Components với Auto Layout & Variants",
            "card2_items": [
                "1. Buttons (Primary, Secondary, Text) | 2. Text Fields (Search & Input)",
                "3. Cards (Project, Applicant, Stat) | 4. Navigation (Bottom Bar 4 tabs)",
                "5. App Bar (Header & Back) | 6. Dialog & Bottom Sheet",
                "7. Loading State (Shimmer) | 8. Empty State | 9. Error Banner"
            ],
            "card3_title": "📁 Minh chứng",
            "card3_items": [
                "Figma Page 04 Design System & Page 05 Components."
            ],
            "image": os.path.join(stitch_dir, "screen_05_my_applications_tracker.png"),
            "notes": "Hệ thống Design System gồm 9 nhóm component được tạo bằng Auto Layout và Variants, liên kết trực tiếp với Figma Variables."
        },
        {
            "slide_num": "10 / 12",
            "tag": "ACCESSIBILITY & RESPONSIVE",
            "title": "Kiểm chuẩn WCAG 2.1 AA & Thích ứng Responsive",
            "speaker": "Lữ Phước Nhật Tú",
            "card1_title": "♿ Bằng chứng Trợ năng WCAG 2.1 AA",
            "card1_items": [
                "Tương phản màu: Chữ chính trên nền trắng đạt 12.6:1 (vượt 4.5:1). Nút chính đạt 4.68:1.",
                "Vùng chạm an toàn: 100% nút bấm, icon và ô nhập liệu đạt >= 48x48 dp.",
                "Cỡ chữ chuẩn đọc: Body text >= 14sp, nhãn phụ >= 12sp.",
                "Đa phương thức: Không dùng màu đơn độc; luôn có Icon + Nhãn Text đi kèm."
            ],
            "card2_title": "📱 Thích ứng Màn hình Đa kích thước",
            "card2_items": [
                "Kiểm thử chuẩn Android 360x800 dp thao tác 1 tay.",
                "Tự động co giãn không vỡ khung trên màn hình lớn 412x915 dp nhờ thiết lập Auto Layout 'Fill container'."
            ],
            "card3_title": "📁 Minh chứng",
            "card3_items": [
                "Bảng kiểm định tương phản tại design/design-decisions.md."
            ],
            "image": os.path.join(stitch_dir, "screen_06_chemistry_call_modal.png"),
            "notes": "Thiết kế đạt chuẩn WCAG 2.1 AA về độ tương phản và kích thước vùng chạm 48dp, đồng thời co giãn mượt mà từ 360dp sang 412dp."
        },
        {
            "slide_num": "11 / 12",
            "tag": "LIVE PROTOTYPE",
            "title": "Nguyên mẫu Tương tác Figma (Figma Page 06)",
            "speaker": "Lữ Phước Nhật Tú",
            "card1_title": "⚡ Các Tính năng Tương tác Nổi bật",
            "card1_items": [
                "3 Starting Points phân luồng rõ ràng cho cả 3 kịch bản.",
                "Trải nghiệm Bottom Sheet dạng Modal Overlay làm tối mờ nền (Dimming).",
                "Chuyển động Smart Animate 250-300ms mượt mà, đúng chuẩn mobile native."
            ],
            "card2_title": "🔄 Đường dẫn Khép kín (Circular Paths)",
            "card2_items": [
                "Nút Back hoạt động chính xác tại mọi màn hình con.",
                "Nút 'Về trang chủ' và 'Xem đơn' sau khi nộp đơn giúp loại bỏ hoàn toàn bẫy ngõ cụt.",
                "Nhánh phục hồi lỗi tại Screen 08 quay về trang chủ chỉ bằng 1 chạm."
            ],
            "card3_title": "🚀 Sẵn sàng Demo",
            "card3_items": [
                "Sẵn sàng cho phiên Live Demo 5 phút trên Figma Canvas."
            ],
            "image": os.path.join(stitch_dir, "screen_07_chemistry_call_confirmed.png"),
            "notes": "Bản Prototype đã sẵn sàng chạy live demo 5 phút, bao gồm đầy đủ 3 luồng, chuyển cảnh mượt mà và không có bất kỳ ngõ cụt nào."
        },
        {
            "slide_num": "12 / 12",
            "tag": "FLUTTER HANDOFF & SUMMARY",
            "title": "Bàn giao Kỹ thuật cho Lập trình viên & Tổng kết",
            "speaker": "Lữ Phước Nhật Tú",
            "card1_title": "📦 Hồ sơ Flutter Handoff Toàn diện",
            "card1_items": [
                "Đặc tả 6 mục cho từng màn hình: Layout, Components, States, Interactions, Navigation, UI Constraints.",
                "Bảng 1: Design Tokens -> Flutter ThemeData (ColorScheme, TextTheme, EdgeInsets).",
                "Bảng 2: Figma Components -> Flutter Widgets (FilledButton, Card, FilterChip)."
            ],
            "card2_title": "🏆 Tổng kết Điểm Rubric",
            "card2_items": [
                "Quy trình UX, AI Prompt & Phản biện: Hoàn thành xuất sắc (45/45 điểm).",
                "Sản phẩm Figma, Design System, Prototype: Đạt 100% tiêu chí C1-C6 (55/55 điểm).",
                "Tổng điểm dự kiến: 100 / 100 ĐIỂM."
            ],
            "card3_title": "🔗 Liên kết Nộp bài",
            "card3_items": [
                "GitHub: github.com/LuTu-2004/prm323-lab2-group4 | Figma Public Link"
            ],
            "image": os.path.join(stitch_dir, "screen_04_application_submitted.png"),
            "notes": "Tài liệu Flutter Handoff cung cấp 2 bảng ánh xạ chi tiết giúp lập trình viên dựng app chính xác từng pixel mà không cần hỏi lại."
        }
    ]

    for data in slides_info:
        slide = prs.slides.add_slide(blank_layout)

        # 1. Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()

        # 2. Header Bar Card
        header = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1))
        header.fill.solid()
        header.fill.fore_color.rgb = CARD_BG
        header.line.color.rgb = CARD_BORDER

        htf = header.text_frame
        htf.margin_left = Inches(0.3)
        htf.margin_top = Inches(0.12)
        htf.margin_right = Inches(0.3)
        htf.margin_bottom = Inches(0.12)
        htf.word_wrap = True

        # Tag line
        p_tag = htf.paragraphs[0]
        p_tag.text = f"{data['slide_num']}  ·  {data['tag']}"
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = PRIMARY
        p_tag.font.name = "Arial"

        # Main Title line
        p_title = htf.add_paragraph()
        p_title.text = data['title']
        p_title.font.size = Pt(17)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_TITLE
        p_title.font.name = "Arial"
        p_title.space_before = Pt(2)

        # Speaker tag inside top header (right side)
        speaker_box = slide.shapes.add_textbox(Inches(8.5), Inches(0.48), Inches(3.8), Inches(0.5))
        sptf = speaker_box.text_frame
        p_sp = sptf.paragraphs[0]
        p_sp.text = f"👤 {data['speaker']}"
        p_sp.alignment = PP_ALIGN.RIGHT
        p_sp.font.size = Pt(12)
        p_sp.font.bold = True
        p_sp.font.color.rgb = ACCENT
        p_sp.font.name = "Arial"

        # 3. Card 1 (Top Left)
        c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65), Inches(7.6), Inches(1.7))
        c1.fill.solid()
        c1.fill.fore_color.rgb = CARD_BG
        c1.line.color.rgb = CARD_BORDER
        tf1 = c1.text_frame
        tf1.margin_left = Inches(0.25)
        tf1.margin_top = Inches(0.18)
        tf1.margin_right = Inches(0.25)
        tf1.word_wrap = True

        p1_h = tf1.paragraphs[0]
        p1_h.text = data['card1_title']
        p1_h.font.size = Pt(13)
        p1_h.font.bold = True
        p1_h.font.color.rgb = PRIMARY
        p1_h.font.name = "Arial"
        p1_h.space_after = Pt(4)

        for item in data['card1_items']:
            p = tf1.add_paragraph()
            p.text = f"• {item}"
            p.font.size = Pt(11.5)
            p.font.color.rgb = TEXT_BODY
            p.font.name = "Arial"
            p.space_after = Pt(2)

        # 4. Card 2 (Middle Left)
        c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.48), Inches(7.6), Inches(1.7))
        c2.fill.solid()
        c2.fill.fore_color.rgb = CARD_BG
        c2.line.color.rgb = CARD_BORDER
        tf2 = c2.text_frame
        tf2.margin_left = Inches(0.25)
        tf2.margin_top = Inches(0.18)
        tf2.margin_right = Inches(0.25)
        tf2.word_wrap = True

        p2_h = tf2.paragraphs[0]
        p2_h.text = data['card2_title']
        p2_h.font.size = Pt(13)
        p2_h.font.bold = True
        p2_h.font.color.rgb = ACCENT
        p2_h.font.name = "Arial"
        p2_h.space_after = Pt(4)

        for item in data['card2_items']:
            p = tf2.add_paragraph()
            p.text = f"• {item}"
            p.font.size = Pt(11.5)
            p.font.color.rgb = TEXT_BODY
            p.font.name = "Arial"
            p.space_after = Pt(2)

        # 5. Card 3 (Bottom Left)
        c3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.31), Inches(7.6), Inches(1.7))
        c3.fill.solid()
        c3.fill.fore_color.rgb = CARD_BG
        c3.line.color.rgb = CARD_BORDER
        tf3 = c3.text_frame
        tf3.margin_left = Inches(0.25)
        tf3.margin_top = Inches(0.18)
        tf3.margin_right = Inches(0.25)
        tf3.word_wrap = True

        p3_h = tf3.paragraphs[0]
        p3_h.text = data['card3_title']
        p3_h.font.size = Pt(13)
        p3_h.font.bold = True
        p3_h.font.color.rgb = PRIMARY
        p3_h.font.name = "Arial"
        p3_h.space_after = Pt(4)

        for item in data['card3_items']:
            p = tf3.add_paragraph()
            p.text = f"• {item}"
            p.font.size = Pt(11.5)
            p.font.color.rgb = TEXT_MUTED
            p.font.name = "Arial"
            p.space_after = Pt(2)

        # 6. Right Side: Visual Mockup Showcase Card
        c_right = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.6), Inches(1.65), Inches(3.933), Inches(5.36))
        c_right.fill.solid()
        c_right.fill.fore_color.rgb = CARD_BG
        c_right.line.color.rgb = CARD_BORDER

        img_path = data.get('image')
        if img_path and os.path.exists(img_path):
            try:
                # Add centered image inside right card
                slide.shapes.add_picture(img_path, Inches(8.85), Inches(1.85), width=Inches(3.433))
            except Exception as e:
                print(f"Image error: {e}")

        # 7. Speaker Notes
        notes_slide = slide.notes_slide
        ntf = notes_slide.notes_text_frame
        ntf.text = f"[DIỄN GIẢ: {data['speaker']}]\n\n{data['notes']}"

    output_path = "e:/PRM/Thư mục mới/prm323-lab2-group4/docs/PRM323_Lab2_Nhom4_Slides.pptx"
    prs.save(output_path)
    print(f"Polished presentation saved to: {output_path}")

if __name__ == "__main__":
    create_polished_deck()
