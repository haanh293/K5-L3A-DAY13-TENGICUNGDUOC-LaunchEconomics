# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51 / 1.200) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu trong phạm vi được mở bằng trợ lý | Số yêu cầu được mở qua giao diện trợ lý chia tổng yêu cầu trong phạm vi (noi_dia + hang_nang) của nhóm can thiệp | *Không cần tính (đo trong pilot)* |
| An toàn | Nhóm tự đề xuất: Tỉ lệ hoàn sai tiền phát hiện qua kiểm tra mẫu ngẫu nhiên | Số đơn kiểm tra mẫu có số tiền hoàn thực tế lệch số tiền theo chính sách chia tổng số đơn kiểm tra mẫu (100 đơn/tuần) | *Không cần tính (đo trong pilot)* |

*Ghi chú quy tắc:* Chỉ số trong đợt chạy thử đạt 82,83% (không viết "trợ lý đã nâng chỉ số" vì đợt chạy thử 2 tuần chưa có nhóm đối chứng).

## Danh sách event

Hệ thống thiết kế 10 event telemetry chuẩn hóa, mọi event đều bắt buộc mang `trace_id` để liên kết thông suốt với trace của agent:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng / Cổng tiếp nhận | `request_id`, `loai`, `so_tien`, `arm`, `depot_id`, `trace_id` | Khi khách hàng gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent Core Engine | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Ngay khi một lần chạy của agent kết thúc (kể cả lỗi) |
| `agent_suggestion_shown` | Giao diện CSKH (UI) | `staff_id`, `so_tien_de_xuat`, `phuong_an`, `trace_id` | Khi màn hình hiển thị gợi ý của agent cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm xác nhận/chỉnh sửa/bác bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id`, `phut_lam_lai` (đo thật), `ly_do_lam_lai`, `trace_id` | Khi nhân viên hoàn thành xử lý lại ca hỏng |
| `refund_ledger_write` | Dịch vụ Sổ cái Hoàn tiền | `idempotency_key`, `so_tien`, `status` (`ok`/`fail`), `trace_id` | Khi thực hiện ghi giao dịch chuyển tiền |
| `handoff_to_staff` | Agent Core Engine | `reason` (`thieu_du_lieu`, `vuot_nguong`, `loi_tool`), `tom_tat`, `trace_id` | Khi agent chủ động chuyển ca cho nhân viên |
| `ticket_closed` | Hệ thống Helpdesk / Ticket | `closed_at`, `duration_hours`, `closed_by`, `trace_id` | Khi yêu cầu được đánh dấu giải quyết hoàn tất |
| `ticket_reopened` | Cổng khách hàng / Ticket | `reopened_at`, `reason`, `trace_id` | Khi khách khiếu nại mở lại trong vòng 7 ngày |
| `audit_sample_checked` | Kế toán nội bộ / QA | `sample_id`, `so_tien_da_hoan`, `so_tien_chuan`, `ket_qua_audit`, `trace_id` | Hằng tuần khi kiểm toán mẫu ngẫu nhiên 100 đơn |

**Kiểm tra chéo (Cross-check):**
- **Chỉ số chính (% đóng trong 24h & không mở lại trong 7 ngày):** Tính từ `ticket_closed` (`closed_at - created_at <= 24h`) đối chiếu với sự vắng mặt của `ticket_reopened` (`reopened_at - closed_at <= 7 days`) theo cùng `trace_id`.
- **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** Tính từ `staff_review_decision` (`quyet_dinh IN ('sua', 'bo')`) chia cho tổng số event `staff_review_decision` phát sinh theo `trace_id`.
- **Chỉ số an toàn (Tỉ lệ lỗi lọt đến khách):** Tính từ số event `ticket_reopened` phát sinh trong 7 ngày chia cho tổng số event `refund_request_created`.
- **Chỉ số dùng tự đề xuất (% mở bằng trợ lý):** Tính từ số event `agent_suggestion_shown` chia cho số event `refund_request_created` phát sinh ở nhóm can thiệp (`arm == 'treatment'`).
- **Chỉ số an toàn tự đề xuất (% sai tiền audit):** Tính từ số event `audit_sample_checked` có `ket_qua_audit == 'sai_lech'` chia cho tổng số event `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
