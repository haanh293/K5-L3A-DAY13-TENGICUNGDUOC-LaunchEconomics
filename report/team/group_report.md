# Báo cáo nhóm

## 1. Thông tin nhóm

- **Tên nhóm:** TENGICUNGDUOC
- **Lớp:** L3A
- **Repo nhóm:** `K5-L3A-DAY13-TENGICUNGDUOC-LaunchEconomics`
- **Thành viên:** 4 thành viên (Nguyễn Hà Anh, Lê Xuân Hạ, Đỗ Đức Duẩn, Đỗ Đắc Duy) — xem chi tiết vai trò và đóng góp trong [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng bộ **hồ sơ launch v0 (Gate 2a)** cho trợ lý hoàn phí AI của **LogiX-VN** dựa trên dữ liệu chạy thử giả lập 2 tuần (1.200 yêu cầu, 1.624 lần chạy trong `src/logix_requests.csv` và `src/logix_runs.csv`) nhằm trả lời 4 câu hỏi cốt lõi: *(1) Chi phí thật có đáng chạy không? (2) Nhân viên có sử dụng không? (3) Xử lý lỗi ra sao? (4) Thiết kế pilot thế nào để tách được tác động và ra quyết định?*

Để triển khai song song không xung đột Git, nhóm áp dụng nguyên tắc **Single Writer** (mỗi file do một thành viên phụ trách chính), đổi người viết code giữa buổi trong `src/lab13.py` (Người 1 viết CP1–CP2, Người 3 viết CP4), và tách riêng hai người gắn nhãn độc lập ở CP3 trước khi so khớp.

## 3. Giải pháp

- **Nhiệm vụ A & B — Mô hình chi phí & Độ nhạy:** Triển khai `mo_hinh(...)` trong [src/lab13.py](../../src/lab13.py) (tử số cộng mọi lần chạy kể cả lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`), vượt qua 3/3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`), phân tách 4 loại yêu cầu, cộng chi phí cố định 40 triệu đ/tháng và chạy 9 kịch bản độ nhạy + kịch bản giới hạn chạy lại và xem lại 100%. Chi tiết: [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C — Phân loại lỗi & Khắc phục:** Hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 nhóm Google PAIR (gắn theo nguyên nhân gốc), so khớp tính tỉ lệ đồng thuận và lập bảng khắc phục 5 ca (đủ 5 loại) có cơ chế phát hiện đo được và vai trò phụ trách cụ thể. Chi tiết: [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D — Thiết kế Pilot:** Tính cỡ mẫu 5 phương án (D1) bằng code trong [src/lab13.py](../../src/lab13.py), kiểm tra 5 tiêu chí tách tác động (D2), chọn chia theo cụm 40 nhân viên CSKH (`20 + 20`, phân tầng theo depot), chấp nhận mức chênh phát hiện 6 điểm (`n = 859`/nhóm, `m ≥ 299` yêu cầu/người) và thiết lập 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`. Chi tiết: [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E — Chỉ số, Rủi ro & Hồ sơ Launch v0:** Tính thử 3 chỉ số trên 1.200 yêu cầu, đề xuất 2 chỉ số mới (adoption & kiểm tra mẫu hoàn sai tiền), chuẩn hóa 10 event mang `trace_id` kèm kiểm tra chéo, lượng hóa 3 rủi ro kinh tế từ bảng độ nhạy ([chi_so.md](chi_so.md)) và tổng hợp thành hồ sơ một trang 7 mục ([ho_so_launch_v0.md](ho_so_launch_v0.md)).
- **Duyệt chéo Gate 2a:** Bảo vệ hồ sơ và thực hiện chấm chéo nhóm bạn tại [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

- **Kinh tế & Phạm vi ([bang_chi_phi.md](bang_chi_phi.md)):**
  - Chi phí mỗi việc thành công toàn mẫu đạt **`4.472 đ` (simulated)** — gấp **16,3×** hoá đơn token + tool/yêu cầu (`274,7 đ`); giờ nhân viên chiếm **92,5%** (làm lại `51,8%`, xem lại `40,7%`, simulated). Chi phí cả hệ thống (cộng 222 ca không thành công × `12.000 đ`) là **`5.865 đ/yêu cầu` (`0,49×`, simulated)**.
  - Thu hẹp phạm vi pilot về `noi_dia` (`2.696 đ` = `0,22×`, thành công `95,0%`) và `hang_nang` (`8.221 đ` = `0,69×`, thành công `74,1%`) [simulated]; loại `quoc_te` (`22.515 đ` = `1,88×`, thành công `27,3%`) và `doi_tac` (`10.215 đ` = `0,85×`, có điều khoản riêng). Cộng chi phí cố định 40 triệu đ/tháng cho **`4.599 đ` (`0,38×`, simulated)** ở 45.000 yêu cầu/tháng và **`5.784 đ` (`0,48×`, simulated)** ở một nửa khối lượng.
  - Top 3 yếu tố nhạy nhất: **số ca làm lại (`+51,8%`), tỉ lệ xem lại (`+40,7%`), lương nhân viên (`+23,1%`)** [simulated]. Giới hạn **2 lần chạy** rẻ nhất cho cả công ty (`6.901.220 đ`, simulated), trong khi xem lại 100% đẩy CPS phạm vi lên **`11.743–12.415 đ` (`0,98×–1,03×`, simulated)**.
- **Lỗi & Chỉ số ([bang_loi.md](bang_loi.md), [chi_so.md](chi_so.md)):** Gắn nhãn độc lập 20 ca đạt đồng thuận **20/20 (100%)**. Chỉ số trong đợt chạy thử: đóng trong 24h & không mở lại trong 7 ngày **`82,83%`** (994/1.200); bỏ qua gợi ý **`27,12%`** (48/177); mở lại trong 7 ngày **`4,25%`** (51/1.200, và `3,97%` trong phạm vi pilot).
- **Đề xuất cuối ([ho_so_launch_v0.md](ho_so_launch_v0.md)):** **Go có điều kiện** cho pilot phạm vi `noi_dia` + `hang_nang` với 4 điều kiện bắt buộc trước/trong rollout: *(1)* thêm `idempotency_key` & đối soát sổ cái hàng giờ (Kỹ sư trưởng agent, 2026-12-04); *(2)* ký chấp nhận đánh đổi MDE 6 điểm / power `0,64` ở mức 5 điểm (Giám đốc vận hành, 2026-12-05); *(3)* bật đủ 10 event có `trace_id` để đo thời gian xem lại/làm lại thật (Kỹ sư trưởng agent & Trưởng nhóm CSKH, 2026-12-14); *(4)* triển khai lộ trình giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa/bỏ < 15% (Trưởng nhóm CSKH & PM, 2026-12-21).
- **Kết quả duyệt chéo từ hội đồng Gate 2a:** *(Nhóm cập nhật điểm và nhận xét nhận được ngay sau phiên duyệt chéo 17:00–17:45.)*

## 5. Khó khăn và cách xử lý

- **Rủi ro xung đột Git khi 4 người làm song song:** Xử lý bằng phân quyền 1 file – 1 chủ sở hữu, riêng `src/lab13.py` bàn giao tuần tự sau khi Người 1 hoàn thành và push CP1–CP2.
- **Đánh đổi giữa cỡ mẫu thống kê và nhiễu tràn tác động (spillover):** Với 40 nhân viên CSKH (`20 + 20`), cỡ mẫu hiệu dụng tối đa chỉ đạt `1.000 < 1.251` nên không đủ power `0,80` cho mức chênh 5 điểm. Nhóm xử lý bằng cách giữ chia theo nhân viên (đủ 20 cụm, giảm spillover bằng phân quyền tài khoản) và ghi rõ đánh đổi chấp nhận mức chênh 6 điểm (`power = 0,64` nếu tác động thật là 5 điểm) để Giám đốc vận hành ký duyệt.
- **Đọc dữ liệu CSV và tuân thủ nhãn giả lập:** Bắt buộc dùng `keep_default_na=False` khi đọc `logix_requests.csv` để tránh lỗi `NaN` ở cột `quyet_dinh_xem_lai`, và rà soát toàn bộ file báo cáo bằng script để đảm bảo đầy đủ nhãn `simulated` và không vi phạm quy tắc 5.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp và bằng chứng commit của từng thành viên nằm trong [TEAM.md](../../TEAM.md) và 4 báo cáo cá nhân trong `report/team/`:

- **Nguyễn Hà Anh (`2A202603605`):** Code giai đoạn 1 `src/lab13.py` (CP1–CP2), hoàn thiện `bang_chi_phi.md`, bàn giao số liệu kinh tế.
- **Lê Xuân Hạ (`2A202603571`):** Gắn nhãn độc lập 20 ca lỗi (Người 1), hoàn thiện `bang_loi.md`, điều phối `phieu_cham.md`.
- **Đỗ Đức Duẩn (`2A202603590`):** Code giai đoạn 2 `src/lab13.py` (CP4: D1, D3), hoàn thiện `pilot_plan.yaml`.
- **Đỗ Đắc Duy (`2A202603604`):** Gắn nhãn độc lập 20 ca lỗi (Người 2), hoàn thiện `chi_so.md` (E1, E2), `ho_so_launch_v0.md` và tổng hợp hồ sơ.

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu thời gian nhân viên còn là giả lập (`_simulated`):** Chiếm `92,5%` tổng chi phí nên sai lệch phút xem lại/làm lại sẽ ảnh hưởng mạnh đến hiệu quả kinh tế. *Hướng cải thiện:* đo đồng hồ thực tế qua event `staff_review_decision` và `staff_rework_completed` ngay từ tuần đầu rollout `0.10` để tính lại CPS thật.
- **Giới hạn sức mạnh thống kê ở mức chênh 5 điểm:** Power chỉ đạt `0,64` với 40 nhân viên. *Hướng cải thiện:* thu thập dữ liệu hiệp biến nền (baseline covariate theo từng nhân viên/depot) để áp dụng phương pháp giảm phương sai (CUPED) trong giai đoạn phân tích pilot.
- **Chưa có đối chứng trong dữ liệu chạy thử 2 tuần:** Chỉ số `82,83%` hiện tại chỉ là mô tả đợt chạy thử, chưa chứng minh được tác động nhân quả cho tới khi chạy pilot có nhóm đối chứng `20 + 20`.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook* — chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu `statsmodels` (`NormalIndPower`, `proportion_effectsize`), mục `stats.power`
- Tài liệu nội bộ Lab 13: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`
