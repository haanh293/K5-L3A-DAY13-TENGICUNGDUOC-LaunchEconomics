# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: TENGICUNGDUOC · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Chi phí trung bình toàn bộ: 4.472 đ [simulated]; trong phạm vi pilot (`noi_dia` + `hang_nang`): 3.414 đ, cộng chi phí cố định (40 tr/tháng ở 45.000 yc/tháng) là **4.599 đ** [simulated] | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8% khi x2); 2. Tỉ lệ xem lại (+40,7% khi x2); 3. Lương nhân viên (+23,1% khi tăng 25%). Giá token chỉ ảnh hưởng +5,6% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí mỗi việc thành công trong phạm vi pilot đạt **0,38×** so với 12.000 đ của nhân viên (tiết kiệm 62% chi phí) [simulated] | Giả lập | Kỹ sư trưởng agent |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính: **82,83%** (đóng trong 24h và không mở lại trong 7 ngày); Dùng: **27,12%** (tỉ lệ bỏ qua/sửa gợi ý); An toàn: **4,25%** (tỉ lệ lỗi lọt đến khách) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi chuẩn Google PAIR, đồng thuận 100%: 4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm. Có 5 giải pháp khắc phục có thước đo | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | 40 nhân viên (20 đối chứng vs 20 can thiệp), MDE 6 điểm ($n=859$/nhóm, $m \ge 299$ đơn/người); rollout 0.10 $\rightarrow$ 0.25 $\rightarrow$ 0.50; 3 luật dừng 4 vế có ngưỡng và rollback | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại x2 tăng lên **6.787 đ** (+51,8%) [simulated]; Xem lại 100% tăng lên **11.743 đ – 12.415 đ** (0,98× – 1,03×) [simulated]; Khối lượng giảm 50% cố định gánh **2.370 đ/việc** [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** cho pilot trong phạm vi `noi_dia` (0,22×) và `hang_nang` (0,69×), loại bỏ hoàn toàn `quoc_te` (1,88×) và `doi_tac` (0,85×) [simulated]. Bốn điều kiện bắt buộc trước và trong khi pilot:

1. **Khắc phục lỗi hệ thống đối soát sổ cái (ca 7, 20):** Cài đặt khoá chống trùng (`idempotency_key`) trên dịch vụ sổ cái hoàn tiền và đối soát tự động hàng giờ; chỉ báo "đã hoàn" khi sổ cái trả kết quả thành công.
   - *Người phụ trách:* Kỹ sư trưởng agent.
   - *Ngày kiểm tra:* 2026-12-04 (trước ngày bắt đầu pilot).
2. **Ký duyệt văn bản chấp nhận đánh đổi cỡ mẫu thống kê:** Giám đốc vận hành ký duyệt chấp nhận MDE = 6 điểm phần trăm (power khoảng 0,64 nếu mức chênh thực tế là 5 điểm) do giới hạn 40 nhân viên CSKH.
   - *Người phụ trách:* Giám đốc vận hành LogiX-VN.
   - *Ngày kiểm tra:* 2026-12-05.
3. **Kích hoạt đủ 10 event telemetry có `trace_id`:** Bắt buộc mọi service ghi đủ `trace_id` trên từng request; bắt đầu đo lường thời gian xem lại (`phut_xem_lai`) và làm lại (`phut_lam_lai`) bằng đồng hồ thực tế trên UI thay cho số giả lập sau tuần 1.
   - *Người phụ trách:* Kỹ sư trưởng agent & Trưởng nhóm CSKH.
   - *Ngày kiểm tra:* 2026-12-14 (cuối bước rollout 0.10).
4. **Kế hoạch giảm xem lại theo bậc (Tiered Review):** Xây dựng lộ trình giảm dần tỉ lệ xem lại khi tỉ lệ sửa/bỏ của nhân viên ổn định dưới 15%, tránh rủi ro xem lại 100% làm triệt tiêu hiệu quả kinh tế (B4).
   - *Người phụ trách:* Trưởng nhóm CSKH & PM trợ lý hoàn phí.
   - *Ngày kiểm tra:* 2026-12-21 (trước khi chuyển từ bước 0.25 sang 0.50).
