# Team

## Thông tin nhóm

- Tên nhóm: TENGICUNGDUOC
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-TENGICUNGDUOC-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/haanh293/K5-L3A-DAY13-TENGICUNGDUOC-LaunchEconomics · nhánh `main` · cập nhật commit chốt cuối cùng trước deadline

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Hà Anh | 2A202603605 | 26ai.anhnh7@vinuni.edu.vn | haanh293 | Người viết code giai đoạn 1 & kiểm số (CP1–CP2: mô hình chi phí, bảng độ nhạy) |
|   2 | Lê Xuân Hạ | 2A202603571 | hlee93698@gmail.com | hlee93698-stack | Người gắn nhãn 1 (CP3: bảng lỗi & khắc phục) & điều phối phiếu chấm duyệt chéo |
|   3 | Đỗ Đức Duẩn | 2A202603590 | duandd1101@gmail.com | Do-Duan | Người viết code giai đoạn 2 (CP4: cỡ mẫu D1 & thiết kế `pilot_plan.yaml`) |
|   4 | Đỗ Đắc Duy | 2A202603604 | ddduy7890@gmail.com | DuyDo1007 | Người gắn nhãn 2 kiêm giữ hồ sơ (CP3, CP5: chỉ số, rủi ro, `ho_so_launch_v0.md`, báo cáo nhóm) |

Phân công theo nguyên tắc **mỗi file một người phụ trách (0% xung đột Git)**, đổi người viết code giữa buổi (Nguyễn Hà Anh viết CP1–CP2, Đỗ Đức Duẩn tiếp quản viết CP4 trong `src/lab13.py`) để có hai thành viên trực tiếp chạy mô hình và kiểm chứng số liệu. Ở CP3, Lê Xuân Hạ và Đỗ Đắc Duy gắn nhãn độc lập 20 ca lỗi trong 8 phút không trao đổi trước khi so khớp.

## Cá nhân

Mỗi thành viên tạo một báo cáo riêng trong `report/team/` theo dạng `report/team/MSSV_HoTen.md`.

## NguyenHaAnh-2A202603605

### Phần việc phụ trách

- Cài đặt môi trường `src/.venv` và triển khai giai đoạn 1 của `src/lab13.py` (CP1: A1–A4; CP2: B1–B4).
- Hoàn thiện bảng chi phí và phân tích độ nhạy trong `report/team/bang_chi_phi.md`.
- Bàn giao `src/lab13.py` và số liệu kinh tế cho thiết kế `pilot_plan.yaml` và `ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Viết ba hàm A1 vượt qua 3/3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`).
- Viết hàm `mo_hinh(runs, reqs, ...)` tính chi phí mỗi việc thành công `4.472 đ` (simulated), gấp `16,3×` hoá đơn token + tool/yêu cầu (`274,7 đ`); chỉ ra làm lại chiếm `51,8%` và xem lại chiếm `40,7%` (simulated).
- Tách 4 loại yêu cầu (A3) đề xuất thu hẹp phạm vi pilot về `noi_dia` (`2.696 đ`, `0,22×`) + `hang_nang` (`8.221 đ`, `0,69×`), loại `quoc_te` (`22.515 đ`, `1,88×`) và `doi_tac` (`10.215 đ`, `0,85×`, simulated); cộng chi phí cố định 40 triệu đ/tháng (A4) cho `4.599 đ` (`0,38×`, simulated).
- Chạy đủ 9 kịch bản độ nhạy B1, đổi cặp B2 (`6.543 đ`, `+46,3%`), so sánh giới hạn chạy lại cả hệ thống B3 (2 lần rẻ nhất `6.901.220 đ`), và kịch bản xem lại 100% B4 (`11.743 đ` / `12.415 đ`, simulated).

### Bằng chứng

- Commit `5c78f6d` (`src/lab13.py`, `report/team/bang_chi_phi.md`).
- Commit `c91c6eb` (`report/team/2A202603605_NguyenHaAnh.md`).

## LeXuanHa-2A202603571

### Phần việc phụ trách

- Nhiệm vụ C (CP3): đọc 20 ca lỗi trong đề bài, gắn nhãn độc lập (Người gắn nhãn 1) theo 5 loại Google PAIR, tổng hợp so khớp với Người gắn nhãn 2 và hoàn thiện `report/team/bang_loi.md`.
- Phụ trách ghi nhận và tổng hợp `report/team/phieu_cham.md` trong phiên duyệt chéo Gate 2a.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc (không trao đổi trong 8 phút) và so khớp với Đỗ Đắc Duy đạt đồng thuận `20/20 = 100%`.
- Viết rõ quy tắc phân biệt nguyên nhân gốc cho các ca dễ nhầm lẫn (ca 6, 9, 13, 8, 15, 18, 12, 17).
- Xây dựng bảng khắc phục đủ 5 loại lỗi (ca 9, 7, 18, 4, 17) với cách phát hiện đo được (event, ngưỡng, tần suất) và vai trò phụ trách cụ thể.

### Bằng chứng

- Commit `88299a1` (`report/team/bang_loi.md`).
- `report/team/phieu_cham.md`, `report/team/2A202603571_LeXuanHa.md`.

## DoDucDuan-2A202603590

### Phần việc phụ trách

- Nhiệm vụ D (CP4): tính cỡ mẫu D1, trả lời 5 câu kiểm tra "tách được tác động" D2, đặt 3 luật dừng và hoàn thiện `report/team/pilot_plan.yaml`.
- Giai đoạn 2 của `src/lab13.py`: bổ sung hàm tính cỡ mẫu, hệ số thiết kế, power và tỉ lệ mở lại 7 ngày (`in_ket_qua_cp4`).

### Đóng góp cụ thể

- Tính đủ 5 câu D1: chia theo yêu cầu `1.251`/nhóm; theo nhân viên `m = 75` (`DE = 2,48`, cần 84 > 40 người); 20 nhân viên/nhóm tối đa `1.000 < 1.251`; 6 depot/nhóm tối đa `300` (< 20 cụm); mức chênh 6 điểm (`859`/nhóm) cần `m ≥ 299`, `DE = 6,96`, power còn `0,64` nếu tác động thật là 5 điểm.
- Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn mẫu, `3,97%` trong phạm vi) làm cơ sở đặt luật dừng an toàn (chênh `+2` điểm so với đối chứng, trần `6%`).
- Hoàn thiện `report/team/pilot_plan.yaml` hợp lệ với `yaml.safe_load`, không còn dấu `?`, đủ 3 luật dừng theo mẫu `NẾU – TRONG – THÌ – KHÔNG THÌ` và tích hợp `in_ket_qua_cp4` vào `src/lab13.py`.

### Bằng chứng

- Commit `56e8825` (`report/team/pilot_plan.yaml`), commit `224bc99` (`src/lab13.py` và `report/team/2A202603590_DoDucDuan.md`).

## DoDacDuy-2A202603604

### Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi ở CP3 (Người gắn nhãn 2).
- Nhiệm vụ E (CP5): đặc tả chỉ số & danh sách event (E1), phân tích rủi ro kinh tế (E2) trong `report/team/chi_so.md`, tổng hợp `report/team/ho_so_launch_v0.md` và `report/team/group_report.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi theo Google PAIR, trùng khớp `20/20 = 100%` với Lê Xuân Hạ.
- Tính thử 3 chỉ số E1 trên 1.200 yêu cầu (`82,83%`, `27,12%`, `4,25%`), đề xuất 2 chỉ số mới (adoption & kiểm tra mẫu hoàn sai tiền), chuẩn hóa 10 event có `trace_id` kèm kiểm tra chéo đầy đủ.
- Lượng hóa 3 rủi ro kinh tế E2 từ bảng độ nhạy (làm lại ×2 lên `6.787 đ`, xem lại 100% lên `11.743–12.415 đ`, khối lượng giảm 50% cố định `2.370 đ/việc`, simulated).
- Hoàn thiện trang hồ sơ 7 mục `report/team/ho_so_launch_v0.md` với đề xuất **Go có điều kiện** và tổng hợp `report/team/group_report.md`.

### Bằng chứng

- Commit `cce03c0` & `7131f07` (`report/team/chi_so.md`), commit `60d49b7` (`report/team/ho_so_launch_v0.md`), commit `a8b0b9e` (`report/team/2A202603604_DoDacDuy.md`), và `report/team/group_report.md`.
