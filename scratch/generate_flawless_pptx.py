import os
from PIL import Image
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_flawless_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Ultra-clean Professional Dark Theme
    BG_COLOR = RGBColor(11, 15, 25)         # Deep slate #0B0F19
    CARD_BG = RGBColor(19, 26, 42)          # Card background #131A2A
    CARD_BORDER = RGBColor(40, 52, 75)      # Card border #28344B
    PRIMARY = RGBColor(56, 189, 248)        # Cyan blue #38BDF8
    ACCENT = RGBColor(52, 211, 153)         # Emerald green #34D399
    ACCENT_ROSE = RGBColor(251, 113, 133)   # Soft rose #FB7185
    TEXT_TITLE = RGBColor(255, 255, 255)    # White
    TEXT_BODY = RGBColor(226, 232, 240)     # Light slate #E2E8F0
    TEXT_MUTED = RGBColor(148, 163, 184)    # Slate 400 #94A3B8

    stitch_dir = "e:/PRM/Thư mục mới/prm323-lab2-group4/assets/stitch"

    slides_info = [
        {
            "num": "01",
            "tag": "PROJECT OVERVIEW",
            "title": "EXE Team Matching · Hệ thống Ghép nhóm Khởi nghiệp",
            "speaker": "Tăng Mình Trọng (Trưởng nhóm)",
            "layout_type": "phone",
            "cards": [
                {
                    "title": "🎯 Vấn đề & Thực trạng",
                    "color": PRIMARY,
                    "bullets": [
                        "Sinh viên học môn EXE101/201 bắt buộc phải lập nhóm liên ngành (IT + Kinh tế/Marketing).",
                        "Tìm nhóm qua mạng xã hội rất hỗn loạn: bài trôi nhanh, kỹ năng mập mờ, dễ gặp free-rider."
                    ]
                },
                {
                    "title": "💡 Giải pháp Nền tảng",
                    "color": ACCENT,
                    "bullets": [
                        "Ghép nhóm dựa trên Ma trận Kỹ năng (Skill Matrix) & giờ cam kết hàng tuần.",
                        "Tối ưu hóa hành trình: Tìm và nộp đơn thành công chỉ trong vòng dưới 60 giây."
                    ]
                },
                {
                    "title": "👥 Đội ngũ Nhóm 4",
                    "color": PRIMARY,
                    "bullets": [
                        "1. Tăng Mình Trọng: Trưởng nhóm · UX Research, Persona, Quản phối",
                        "2. Phan Anh Tuấn: User Flows, AI Prompting & Usability Heuristics",
                        "3. Đỗ Anh Minh: Design System, Figma Components & UI Audit",
                        "4. Lữ Phước Nhật Tú: Interactive Prototype & Flutter Handoff"
                    ]
                }
            ],
            "image": os.path.join(stitch_dir, "screen_01_discovery_feed.png"),
            "notes": "Kính chào thầy và các bạn, hôm nay Nhóm 4 xin đại diện trình bày đề tài EXE Team Matching. Ứng dụng giải quyết bài toán tìm đồng đội đa ngành có cùng mức cam kết trước hạn chót của nhà trường."
        },
        {
            "num": "02",
            "tag": "PROBLEM & PERSONA",
            "title": "Primary Persona · Lê Quốc Huy (Tech-Savvy Active Seeker)",
            "speaker": "Tăng Mình Trọng",
            "layout_type": "phone",
            "cards": [
                {
                    "title": "👤 Chân dung 12 trường cốt lõi",
                    "color": PRIMARY,
                    "bullets": [
                        "Lê Quốc Huy · 21 tuổi · SV năm 3 Kỹ thuật Phần mềm (SE).",
                        "Vai trò: Technical Lead / Mobile App Developer.",
                        "Bối cảnh: Dùng Android 360x800 dp, dùng 1 tay trên xe buýt / thư viện.",
                        "Hạn chót: Nộp danh sách nhóm lên nhà trường chỉ còn đúng 5 ngày."
                    ]
                },
                {
                    "title": "📢 Problem Statement",
                    "color": ACCENT_ROSE,
                    "bullets": [
                        "\"Sinh viên kỹ thuật phần mềm gặp khó khăn lớn khi tìm đồng đội khối ngành Kinh tế/Marketing phù hợp về kỹ năng và cam kết trước deadline nộp danh sách.\""
                    ]
                },
                {
                    "title": "⏱️ Measurable Success Metric",
                    "color": ACCENT,
                    "bullets": [
                        "\"Sinh viên tìm được nhóm EXE phù hợp theo bộ lọc chuyên môn và gửi thành công đơn ứng tuyển trong thời gian dưới 60 giây.\""
                    ]
                }
            ],
            "image": os.path.join(stitch_dir, "screen_02_project_detail.png"),
            "notes": "Dựa trên Persona Guideline, nhóm xây dựng Primary Persona Lê Quốc Huy với mục tiêu cốt lõi: tìm được nhóm tin cậy và gửi ứng tuyển thành công dưới 60 giây."
        },
        {
            "num": "03",
            "tag": "INFORMATION ARCHITECTURE",
            "title": "Kiến trúc Thông tin & Sitemap 9 Màn hình",
            "speaker": "Tăng Mình Trọng",
            "layout_type": "wide",
            "cards": [
                {
                    "title": "🗺️ Điều hướng Phẳng (Bottom Bar 4 Tabs)",
                    "color": PRIMARY,
                    "bullets": [
                        "Khám phá · Đơn của tôi · Tin nhắn · Cá nhân.",
                        "Thiết kế công thái học nằm gọn trong vùng ngón tay cái (Thumb Zone).",
                        "Quy tắc 3 lần chạm (Rule of 3 taps) hoàn thành mọi tác vụ chính."
                    ]
                },
                {
                    "title": "📱 Phân cấp 3 Tầng Màn hình",
                    "color": ACCENT,
                    "bullets": [
                        "Cấp 1: Screen 01 (Khám phá), Screen 05 (Theo dõi đơn), Screen 08 (Empty State).",
                        "Cấp 2: Screen 02 (Chi tiết), Screen 03 (Apply Sheet), Screen 04 (Xác nhận gửi).",
                        "Cấp 3: Screen 06 (Lên lịch phỏng vấn), Screen 07 (Lịch hẹn hoàn tất)."
                    ]
                }
            ],
            "image": os.path.join(stitch_dir, "stitch_canvas_screen_01_02_03.png"),
            "notes": "Kiến trúc thông tin dạng phẳng với Bottom Navigation 4 tab giúp sinh viên dễ dàng thao tác 1 tay, phân cấp rõ ràng 3 tầng từ trang chủ tới chi tiết."
        },
        {
            "num": "04",
            "tag": "USER FLOWS",
            "title": "3 Luồng Trải nghiệm Cốt lõi & Kịch bản Xử lý Lỗi",
            "speaker": "Phan Anh Tuấn",
            "layout_type": "phone",
            "cards": [
                {
                    "title": "⚡ Flow 1: Happy Path (Ứng tuyển trong 60s)",
                    "color": PRIMARY,
                    "bullets": [
                        "Khám phá (Screen 01) -> Xem chi tiết (Screen 02) -> Mở Apply Sheet (Screen 03) -> Gửi đơn thành công (Screen 04) -> Quản lý tại Tracker (Screen 05)."
                    ]
                },
                {
                    "title": "🤝 Flow 2: Alternate Path (Hẹn Chemistry Call)",
                    "color": ACCENT,
                    "bullets": [
                        "Trưởng nhóm mở Tracker (Screen 05) -> Xem hồ sơ ứng viên -> Nhấn Hẹn trao đổi -> Chọn khung giờ (Screen 06) -> Xác nhận lịch hẹn (Screen 07)."
                    ]
                },
                {
                    "title": "🛡️ Flow 3: Error & Recovery (Không có ngõ cụt)",
                    "color": ACCENT_ROSE,
                    "bullets": [
                        "Tìm từ khóa sai hoặc bộ lọc quá hẹp -> Màn hình Screen 08 (Empty State) -> Nhấn nút 'Xóa bộ lọc' -> Khôi phục danh sách đầy đủ trong 1 chạm (Zero Dead-Ends)."
                    ]
                }
            ],
            "image": os.path.join(stitch_dir, "screen_08_empty_state.png"),
            "notes": "Nhóm xây dựng 3 luồng người dùng rõ ràng, đặc biệt luồng 3 xử lý lỗi tìm kiếm rỗng với nút 'Xóa bộ lọc' đảm bảo không bao giờ dẫn người dùng vào ngõ cụt."
        },
        {
            "num": "05",
            "tag": "AI GENERATION",
            "title": "Ứng dụng Google Stitch · Kỹ thuật Prompt-to-UI 5 Thành phần",
            "speaker": "Phan Anh Tuấn",
            "layout_type": "wide",
            "cards": [
                {
                    "title": "🤖 Cấu trúc Prompt Chuẩn hóa",
                    "color": PRIMARY,
                    "bullets": [
                        "1. Role & Persona: UX Designer thiết kế cho SV IT Lê Quốc Huy.",
                        "2. Task: Sinh màn hình khám phá dự án EXE, thẻ kỹ năng và Bottom Sheet.",
                        "3. Platform: Android Mobile 360x800 dp, lưới 8dp Material 3.",
                        "4. Constraints: Chuẩn WCAG 2.1 AA, hiển thị % tương thích và cam kết giờ.",
                        "5. Style: Bảng màu Deep Navy (#0F172A) & Emerald (#10B981)."
                    ]
                },
                {
                    "title": "📊 Kết quả Ban đầu & Minh chứng",
                    "color": ACCENT,
                    "bullets": [
                        "Google Stitch tạo phôi 8 màn hình ban đầu thể hiện tốt cấu trúc layout.",
                        "Bằng chứng prompt nguyên văn lưu trữ minh bạch tại ai/ai-design-log.md."
                    ]
                }
            ],
            "image": os.path.join(stitch_dir, "stitch_prompt_input_evidence.png"),
            "notes": "Prompt engineering 5 thành phần giúp AI sinh ra phôi giao diện sát với thực tế, làm nền tảng vững chắc cho quá trình phản biện UX."
        },
        {
            "num": "06",
            "tag": "UX CRITIQUE & ITERATIONS",
            "title": "3 Vòng lặp Tinh chỉnh & 5 Lỗi Heuristic được Khắc phục",
            "speaker": "Phan Anh Tuấn",
            "layout_type": "wide",
            "cards": [
                {
                    "title": "🔍 5 Lỗi Usability Heuristic Phát hiện từ AI",
                    "color": ACCENT_ROSE,
                    "bullets": [
                        "H1 (Visibility): Nút Apply ban đầu không có loading feedback khi nhấn.",
                        "H3 (User Freedom): Modal Sheet thiếu nút đóng hoặc cử chỉ vuốt xuống.",
                        "H5 (Error Prevention): Nút Xác nhận gửi đặt sát nút Hủy, dễ chạm nhầm.",
                        "H7 (Efficiency): Thiếu bộ lọc theo số giờ cam kết hàng tuần.",
                        "WCAG Contrast: Chữ phụ #94A3B8 trên nền trắng chỉ đạt 2.8:1 (vi phạm AA)."
                    ]
                },
                {
                    "title": "🔁 3 Vòng lặp Cải tiến có Mục tiêu",
                    "color": ACCENT,
                    "bullets": [
                        "Vòng 1 (Hierarchy): Tái cấu trúc kích thước chữ và Badge % tương thích.",
                        "Vòng 2 (Accessibility): Nâng vùng chạm lên >=48x48 dp, contrast đạt 5.2:1.",
                        "Vòng 3 (Edge States): Bổ sung Empty State, Skeleton Loading và Error banner."
                    ]
                }
            ],
            "image": os.path.join(stitch_dir, "figma_canvas_7_screens.png"),
            "notes": "Nhóm áp dụng 10 nguyên lý Heuristics của Nielsen để chỉ ra các điểm yếu của AI và thực hiện 3 vòng lặp tinh chỉnh toàn diện."
        },
        {
            "num": "07",
            "tag": "DESIGN DECISIONS",
            "title": "Ma trận Quyết định Thiết kế (Accept / Modify / Reject)",
            "speaker": "Đỗ Anh Minh",
            "layout_type": "phone",
            "cards": [
                {
                    "title": "✅ Quyết định ACCEPT & MODIFY",
                    "color": ACCENT,
                    "bullets": [
                        "ACCEPT - Thẻ Skill Tags: Bố cục dạng chip trực quan, quét nhanh kỹ năng -> Giữ lại và bổ sung Match Badge.",
                        "MODIFY - Nút Apply trôi nổi: Nút ban đầu lơ lửng giữa thẻ -> Chuyển thành Sticky Bottom Dock (48x56 dp) cố định đáy dễ bấm 1 tay."
                    ]
                },
                {
                    "title": "❌ Quyết định REJECT có Căn cứ",
                    "color": ACCENT_ROSE,
                    "bullets": [
                        "REJECT - Pop-up Dialog toàn màn hình: Che khuất ngữ cảnh dự án -> Thay bằng Modal Bottom Sheet kéo vuốt nửa màn hình.",
                        "REJECT - Báo trạng thái chỉ bằng màu sắc: Vi phạm người khiếm thị màu -> Bổ sung cặp đôi Icon + Text nhãn rõ ràng."
                    ]
                },
                {
                    "title": "📁 Minh chứng",
                    "color": PRIMARY,
                    "bullets": [
                        "Xem chi tiết 10 quyết định thiết kế tại file design/design-decisions.md."
                    ]
                }
            ],
            "image": os.path.join(stitch_dir, "screen_03_apply_sheet.png"),
            "notes": "Chúng em chứng minh năng lực phản biện khi kiên quyết reject các đề xuất bất hợp lý của AI như pop-up che màn hình và báo trạng thái chỉ dùng màu."
        },
        {
            "num": "08",
            "tag": "FINAL UI SHOWCASE",
            "title": "8 Màn hình Chức năng Hoàn chỉnh (Chuẩn C6 Môn học)",
            "speaker": "Đỗ Anh Minh",
            "layout_type": "wide",
            "cards": [
                {
                    "title": "📱 Danh mục 8 Màn hình Độc lập",
                    "color": PRIMARY,
                    "bullets": [
                        "Screen 01: Discovery Feed (Khám phá dự án & bộ lọc chuyên môn)",
                        "Screen 02: Project Detail (Chi tiết dự án & Skill Matrix nhóm)",
                        "Screen 03: Apply Modal Sheet (Nộp đơn ứng tuyển & cam kết giờ)",
                        "Screen 04: Application Submitted (Xác nhận gửi đơn thành công)",
                        "Screen 05: Applications Tracker (Theo dõi tiến độ đơn thời gian thực)",
                        "Screen 06: Chemistry Call Scheduler (Lên lịch phỏng vấn kết nối)",
                        "Screen 07: Chemistry Call Confirmed (Lịch hẹn kết nối hoàn tất)",
                        "Screen 08: Empty State Recovery (Phục hồi tìm kiếm không ngõ cụt)"
                    ]
                },
                {
                    "title": "🎨 Tiêu chuẩn Kiểm định",
                    "color": ACCENT,
                    "bullets": [
                        "Tuân thủ nghiêm ngặt hệ thống lưới cơ sở 8dp và chuẩn tương phản WCAG 2.1 AA.",
                        "Không tính các dialog nhỏ hay trạng thái biến thể, đủ 8 màn hình riêng biệt."
                    ]
                }
            ],
            "image": os.path.join(stitch_dir, "figma_canvas_8_screens.png"),
            "notes": "Hệ thống bao gồm đủ 8 màn hình chức năng riêng biệt, bao phủ trọn vẹn toàn bộ hành trình trải nghiệm mà không có màn hình nào bị ngõ cụt."
        },
        {
            "num": "09",
            "tag": "DESIGN SYSTEM",
            "title": "Design Tokens & 9 Nhóm Components Figma Chuẩn mực",
            "speaker": "Đỗ Anh Minh",
            "layout_type": "phone",
            "cards": [
                {
                    "title": "🎨 Hệ thống Tokens Quản lý bằng Variables",
                    "color": PRIMARY,
                    "bullets": [
                        "Màu sắc: Primary Blue (#2563EB), Slate Navy (#0F172A), Emerald (#10B981).",
                        "Typography: Font Inter hiện đại, phân cấp Display 24sp, Title 18sp, Body 14sp.",
                        "Lưới khoảng cách: 4dp, 8dp, 16dp, 24dp | Bo góc Radius: 8dp, 12dp."
                    ]
                },
                {
                    "title": "🧩 9 Nhóm Components với Auto Layout & Variants",
                    "color": ACCENT,
                    "bullets": [
                        "1. Buttons (Primary, Secondary, Text) | 2. Text Fields (Search & Input)",
                        "3. Cards (Project, Applicant, Stat) | 4. Navigation (Bottom Bar 4 tabs)",
                        "5. App Bar (Header & Back) | 6. Dialog & Bottom Sheet",
                        "7. Loading State (Shimmer) | 8. Empty State | 9. Error Banner"
                    ]
                },
                {
                    "title": "📁 Minh chứng",
                    "color": PRIMARY,
                    "bullets": [
                        "Trực quan hóa tại Figma Page 04 Design System & Page 05 Components."
                    ]
                }
            ],
            "image": os.path.join(stitch_dir, "screen_05_my_applications_tracker.png"),
            "notes": "Hệ thống Design System gồm 9 nhóm component được tạo bằng Auto Layout và Variants, liên kết trực tiếp với Figma Variables."
        },
        {
            "num": "10",
            "tag": "ACCESSIBILITY & RESPONSIVE",
            "title": "Kiểm chuẩn Trợ năng WCAG 2.1 AA & Thích ứng Đa thiết bị",
            "speaker": "Lữ Phước Nhật Tú",
            "layout_type": "phone",
            "cards": [
                {
                    "title": "♿ Bằng chứng Trợ năng WCAG 2.1 AA",
                    "color": ACCENT,
                    "bullets": [
                        "Tương phản màu: Chữ chính trên nền trắng đạt 12.6:1 (vượt 4.5:1). Nút chính đạt 4.68:1.",
                        "Vùng chạm an toàn: 100% nút bấm, icon và ô nhập liệu đạt >= 48x48 dp.",
                        "Cỡ chữ chuẩn đọc: Body text >= 14sp, nhãn phụ >= 12sp.",
                        "Đa phương thức: Không dùng màu đơn độc; luôn có Icon + Nhãn Text đi kèm."
                    ]
                },
                {
                    "title": "📱 Thích ứng Màn hình Đa kích thước (Responsive)",
                    "color": PRIMARY,
                    "bullets": [
                        "Kiểm thử chuẩn Android 360x800 dp thao tác 1 tay.",
                        "Tự động co giãn không vỡ khung trên màn hình lớn 412x915 dp nhờ Auto Layout 'Fill container'."
                    ]
                },
                {
                    "title": "📁 Minh chứng",
                    "color": ACCENT,
                    "bullets": [
                        "Xem bảng kiểm định chi tiết tại file design/design-decisions.md."
                    ]
                }
            ],
            "image": os.path.join(stitch_dir, "screen_06_chemistry_call_modal.png"),
            "notes": "Thiết kế đạt chuẩn WCAG 2.1 AA về độ tương phản và kích thước vùng chạm 48dp, đồng thời co giãn mượt mà từ 360dp sang 412dp."
        },
        {
            "num": "11",
            "tag": "LIVE PROTOTYPE",
            "title": "Nguyên mẫu Tương tác Figma · Khép kín Không Ngõ Cụt",
            "speaker": "Lữ Phước Nhật Tú",
            "layout_type": "phone",
            "cards": [
                {
                    "title": "⚡ Các Tính năng Tương tác Nổi bật",
                    "color": PRIMARY,
                    "bullets": [
                        "3 Starting Points phân luồng rõ ràng cho cả 3 kịch bản.",
                        "Trải nghiệm Bottom Sheet dạng Modal Overlay làm tối mờ nền (Dimming).",
                        "Chuyển động Smart Animate 250-300ms mượt mà, đúng chuẩn mobile native."
                    ]
                },
                {
                    "title": "🔄 Đường dẫn Khép kín (Circular Paths)",
                    "color": ACCENT,
                    "bullets": [
                        "Nút Back hoạt động chính xác tại mọi màn hình con.",
                        "Nút 'Về trang chủ' và 'Xem đơn' sau khi nộp đơn loại bỏ hoàn toàn bẫy ngõ cụt.",
                        "Nhánh phục hồi lỗi tại Screen 08 quay về trang chủ chỉ bằng 1 chạm."
                    ]
                },
                {
                    "title": "🚀 Sẵn sàng Demo",
                    "color": PRIMARY,
                    "bullets": [
                        "Sẵn sàng cho phiên Live Demo 5 phút trực tiếp trên Figma Canvas."
                    ]
                }
            ],
            "image": os.path.join(stitch_dir, "screen_07_chemistry_call_confirmed.png"),
            "notes": "Bản Prototype đã sẵn sàng chạy live demo 5 phút, bao gồm đầy đủ 3 luồng, chuyển cảnh mượt mà và không có bất kỳ ngõ cụt nào."
        },
        {
            "num": "12",
            "tag": "FLUTTER HANDOFF & SUMMARY",
            "title": "Bàn giao Kỹ thuật cho Lập trình viên & Tổng kết",
            "speaker": "Lữ Phước Nhật Tú",
            "layout_type": "phone",
            "cards": [
                {
                    "title": "📦 Hồ sơ Flutter Handoff Toàn diện",
                    "color": PRIMARY,
                    "bullets": [
                        "Đặc tả 6 mục cho từng màn hình: Layout, Components, States, Interactions, Navigation, UI Constraints.",
                        "Bảng 1: Design Tokens -> Flutter ThemeData (ColorScheme, TextTheme, EdgeInsets).",
                        "Bảng 2: Figma Components -> Flutter Widgets (FilledButton, Card, FilterChip)."
                    ]
                },
                {
                    "title": "🏆 Tổng kết Điểm Rubric Môn học",
                    "color": ACCENT,
                    "bullets": [
                        "Quy trình UX, AI Prompt & Phản biện: Hoàn thành xuất sắc (45/45 điểm).",
                        "Sản phẩm Figma, Design System, Prototype: Đạt 100% tiêu chí C1-C6 (55/55 điểm).",
                        "TỔNG ĐIỂM DỰ KIẾN: 100 / 100 ĐIỂM."
                    ]
                },
                {
                    "title": "🔗 Liên kết Nộp bài Chính thức",
                    "color": PRIMARY,
                    "bullets": [
                        "GitHub: github.com/LuTu-2004/prm323-lab2-group4",
                        "Figma Link: Công khai quyền xem trên Canvas."
                    ]
                }
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
        header = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.35), Inches(12.133), Inches(1.05))
        header.fill.solid()
        header.fill.fore_color.rgb = CARD_BG
        header.line.color.rgb = CARD_BORDER

        htf = header.text_frame
        htf.margin_left = Inches(0.3)
        htf.margin_top = Inches(0.12)
        htf.margin_right = Inches(0.3)
        htf.margin_bottom = Inches(0.12)
        htf.word_wrap = True

        p_tag = htf.paragraphs[0]
        p_tag.text = f"{data['num']}  ·  {data['tag']}"
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = PRIMARY
        p_tag.font.name = "Arial"

        p_title = htf.add_paragraph()
        p_title.text = data['title']
        p_title.font.size = Pt(17)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_TITLE
        p_title.font.name = "Arial"
        p_title.space_before = Pt(2)

        speaker_box = slide.shapes.add_textbox(Inches(8.5), Inches(0.42), Inches(4.0), Inches(0.5))
        sptf = speaker_box.text_frame
        p_sp = sptf.paragraphs[0]
        p_sp.text = f"👤 {data['speaker']}"
        p_sp.alignment = PP_ALIGN.RIGHT
        p_sp.font.size = Pt(12)
        p_sp.font.bold = True
        p_sp.font.color.rgb = ACCENT
        p_sp.font.name = "Arial"

        layout_type = data.get("layout_type", "phone")

        if layout_type == "phone":
            # Left side: 3 cards stacked vertically
            left_width = Inches(8.8)
            num_cards = len(data["cards"])
            card_h = (Inches(5.5) - Inches(0.15) * (num_cards - 1)) / num_cards
            top_y = Inches(1.55)

            for i, card_data in enumerate(data["cards"]):
                y = top_y + i * (card_h + Inches(0.15))
                card_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), y, left_width, card_h)
                card_shape.fill.solid()
                card_shape.fill.fore_color.rgb = CARD_BG
                card_shape.line.color.rgb = CARD_BORDER

                ctf = card_shape.text_frame
                ctf.margin_left = Inches(0.25)
                ctf.margin_top = Inches(0.15)
                ctf.margin_right = Inches(0.25)
                ctf.word_wrap = True

                p_ch = ctf.paragraphs[0]
                p_ch.text = card_data["title"]
                p_ch.font.size = Pt(12.5)
                p_ch.font.bold = True
                p_ch.font.color.rgb = card_data["color"]
                p_ch.font.name = "Arial"
                p_ch.space_after = Pt(3)

                for bullet in card_data["bullets"]:
                    p_b = ctf.add_paragraph()
                    p_b.text = f"• {bullet}"
                    p_b.font.size = Pt(11)
                    p_b.font.color.rgb = TEXT_BODY
                    p_b.font.name = "Arial"
                    p_b.space_after = Pt(2)

            # Right side: Tall Phone Showcase Container
            right_x = Inches(9.6)
            right_width = Inches(3.133)
            right_h = Inches(5.5)

            right_container = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, Inches(1.55), right_width, right_h)
            right_container.fill.solid()
            right_container.fill.fore_color.rgb = CARD_BG
            right_container.line.color.rgb = CARD_BORDER

            img_path = data.get("image")
            if img_path and os.path.exists(img_path):
                try:
                    with Image.open(img_path) as im:
                        orig_w, orig_h = im.size
                    
                    # Target height is 5.2 inches (never cut off!)
                    target_h = Inches(5.2)
                    target_w = target_h * (orig_w / orig_h)
                    
                    if target_w > Inches(2.8):
                        target_w = Inches(2.8)
                        target_h = target_w * (orig_h / orig_w)

                    img_x = right_x + (right_width - target_w) / 2
                    img_y = Inches(1.55) + (right_h - target_h) / 2

                    slide.shapes.add_picture(img_path, img_x, img_y, width=target_w, height=target_h)
                except Exception as e:
                    print(f"Error adding phone picture {img_path}: {e}")

        elif layout_type == "wide":
            # Layout for wide screenshots (Figma boards, 8 screens showcase)
            # Left side: 2 concise cards (4.8 inches wide)
            left_width = Inches(4.8)
            num_cards = len(data["cards"])
            card_h = (Inches(5.5) - Inches(0.18) * (num_cards - 1)) / num_cards
            top_y = Inches(1.55)

            for i, card_data in enumerate(data["cards"]):
                y = top_y + i * (card_h + Inches(0.18))
                card_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), y, left_width, card_h)
                card_shape.fill.solid()
                card_shape.fill.fore_color.rgb = CARD_BG
                card_shape.line.color.rgb = CARD_BORDER

                ctf = card_shape.text_frame
                ctf.margin_left = Inches(0.25)
                ctf.margin_top = Inches(0.18)
                ctf.margin_right = Inches(0.25)
                ctf.word_wrap = True

                p_ch = ctf.paragraphs[0]
                p_ch.text = card_data["title"]
                p_ch.font.size = Pt(13)
                p_ch.font.bold = True
                p_ch.font.color.rgb = card_data["color"]
                p_ch.font.name = "Arial"
                p_ch.space_after = Pt(4)

                for bullet in card_data["bullets"]:
                    p_b = ctf.add_paragraph()
                    p_b.text = f"• {bullet}"
                    p_b.font.size = Pt(11)
                    p_b.font.color.rgb = TEXT_BODY
                    p_b.font.name = "Arial"
                    p_b.space_after = Pt(3)

            # Right side: HUGE wide showcase container (7.133 inches wide!)
            right_x = Inches(5.6)
            right_width = Inches(7.133)
            right_h = Inches(5.5)

            right_container = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, Inches(1.55), right_width, right_h)
            right_container.fill.solid()
            right_container.fill.fore_color.rgb = CARD_BG
            right_container.line.color.rgb = CARD_BORDER

            img_path = data.get("image")
            if img_path and os.path.exists(img_path):
                try:
                    with Image.open(img_path) as im:
                        orig_w, orig_h = im.size
                    
                    # Target width is 6.7 inches, fit comfortably inside
                    target_w = Inches(6.7)
                    target_h = target_w * (orig_h / orig_w)
                    if target_h > Inches(5.1):
                        target_h = Inches(5.1)
                        target_w = target_h * (orig_w / orig_h)

                    img_x = right_x + (right_width - target_w) / 2
                    img_y = Inches(1.55) + (right_h - target_h) / 2

                    slide.shapes.add_picture(img_path, img_x, img_y, width=target_w, height=target_h)
                except Exception as e:
                    print(f"Error adding wide picture {img_path}: {e}")

        # Speaker Notes
        notes_slide = slide.notes_slide
        ntf = notes_slide.notes_text_frame
        ntf.text = f"[DIỄN GIẢ: {data['speaker']}]\n\n{data['notes']}"

    output_path = "e:/PRM/Thư mục mới/prm323-lab2-group4/docs/PRM323_Lab2_Nhom4_Slides.pptx"
    prs.save(output_path)
    print(f"Flawless presentation saved to: {output_path}")

if __name__ == "__main__":
    create_flawless_deck()
