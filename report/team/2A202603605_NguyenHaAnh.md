# Báo cáo cá nhân — NguyenHaAnh-2A202603605

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hà Anh
- MSSV: 2A202603605
- Email: 26ai.anhnh7@vinuni.edu.vn
- Vai trong nhóm: Người viết code (giai đoạn 1: CP1–CP2, kinh tế & bảng độ nhạy)

## 2. Phần việc phụ trách

- Cài đặt, kiểm tra môi trường Python (`src/.venv`) và đảm bảo chạy sạch các thư viện `pandas`, `numpy`, `scipy`, `statsmodels`, `pyyaml`.
- Triển khai code cho Nhiệm vụ A (A1–A4: ba phép thử đáp án biết trước, mô hình chi phí từ trace, phân tách theo loại yêu cầu, cộng chi phí cố định) và Nhiệm vụ B (B1–B4: phân tích độ nhạy 9 kịch bản, đổi cặp, chi phí cả hệ thống theo giới hạn chạy lại, kịch bản xem lại 100%) trong `src/lab13.py`.
- Hoàn thiện đầy đủ bảng số liệu, gắn nhãn `simulated` và viết kết luận ngắn (tối đa 3 dòng, có số) trong `report/team/bang_chi_phi.md`.
- Bàn giao `src/lab13.py` (còn phần `# TODO CP4`) và số liệu kinh tế cho thành viên phụ trách `pilot_plan.yaml` và `ho_so_launch_v0.md`.

## 3. Đóng góp cụ thể

- **Nhiệm vụ A1:** Viết ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`, đạt 3/3 phép thử kiểm chứng (`1,20 · 1,25 · 1,25`).
- **Nhiệm vụ A2:** Viết hàm `mo_hinh(runs, reqs, ...)` tái sử dụng được cho A3 và B; tính ra tổng chi phí `4.373.585 đ` (simulated), `978` việc thành công, chi phí mỗi việc thành công `4.472 đ` (simulated) — gấp `16,3×` hoá đơn token + tool chia số yêu cầu (`274,7 đ`), trong đó làm lại chiếm `51,8%` và xem lại chiếm `40,7%` (simulated).
- **Nhiệm vụ A3 & A4:** Phân tách 4 loại yêu cầu, chỉ ra `quoc_te` (`22.515 đ` = `1,88×`, thành công `27,3%`, simulated) và `doi_tac` (`10.215 đ` = `0,85×`, simulated) cần loại khỏi phạm vi pilot, đồng thời chứng minh chạy lại 3 lần không cải thiện `quoc_te` (tỉ lệ `ok` giảm từ `30,0%` xuống `11,4%` và `2,2%`). Cộng chi phí cố định `40 triệu đ/tháng` cho phạm vi `noi_dia` + `hang_nang` cho `4.599 đ` (`0,38×`, simulated) ở 45.000 yêu cầu/tháng và `5.784 đ` (`0,48×`, simulated) ở một nửa khối lượng.
- **Nhiệm vụ B1–B4:** Chạy đủ 9 kịch bản đơn lẻ, 1 kịch bản đổi cặp (`6.543 đ`, `+46,3%`, simulated), xếp hạng top 3 yếu tố nhạy nhất (số ca làm lại, tỉ lệ xem lại, lương nhân viên). Chứng minh giới hạn `2 lần` rẻ nhất cho cả hệ thống (`6.901.220 đ`, simulated) khác với giới hạn `1 lần` cho CPS thấp nhất (`4.111 đ`, simulated), và chỉ ra xem lại 100% nâng CPS phạm vi lên `11.743 đ` (`0,98×`, mức 9 phút làm lại) hoặc `12.415 đ` (`1,03×`, mức trung bình thực tế 15,3 phút, simulated).

## 4. Bằng chứng

- Commit chốt CP1–CP2: `5c78f6d` (`feat(cp1-cp2): implement cost model, sensitivity analysis and bang_chi_phi`).
- File code đã triển khai và chạy kiểm chứng: `src/lab13.py` (in `Ba phép thử đáp án biết trước: ĐẠT` và toàn bộ bảng A1–A4, B1–B4).
- File hồ sơ đã hoàn thiện: `report/team/bang_chi_phi.md` (đủ bảng A1–A4, B1–B4, đầy đủ nhãn `simulated`, không chứa từ cấm).

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI trong IDE (Antigravity / Gemini).
- **Mục đích sử dụng:** Hỗ trợ rà soát yêu cầu trong `README.md`, `CHECKPOINTS.md`, `RUBRIC.md`; phân chia công việc nhóm tránh xung đột Git; gợi ý cấu trúc code cho `src/lab13.py` và rà soát định dạng, nhãn `simulated` trong `report/team/bang_chi_phi.md`.
- **Cách tự kiểm tra kết quả:**
  - Chạy trực tiếp `.\.venv\Scripts\python.exe lab13.py` trong `src/` trên hai file dữ liệu gốc `logix_runs.csv` và `logix_requests.csv` (đọc với `keep_default_na=False`).
  - Xác nhận qua 3/3 assert ở `kiem_tra_dap_an_biet_truoc()` (`1,20 · 1,25 · 1,25`), đối chiếu tính đối xứng của bảng độ nhạy (mức giảm một nửa bằng đúng nửa mức tăng gấp đôi: `+5,6%`/`−2,8%`, `+40,7%`/`−20,3%`, `+51,8%`/`−25,9%`) và tính cộng tuyến tính của B2 (`+5,6% + 40,7% = +46,3%`).
  - Đối chiếu số đầu ra với công thức gốc trong `docs/du_lieu_va_cong_thuc.md` và quét tự động file `report/team/bang_chi_phi.md` để đảm bảo không còn `...` và không dùng từ cấm.

## 6. Tự đánh giá

- **Điểm mạnh:** Hoàn thành đúng tiến độ và đúng toàn bộ số liệu CP1–CP2 (lệch `0%` so với kiểm chứng công thức), phân tách rõ ranh giới file giúp nhóm làm song song không gặp conflict Git, bàn giao số liệu kịp thời cho các thành viên phụ trách `pilot_plan.yaml` và `ho_so_launch_v0.md`.
- **Điểm cần lưu ý/cải thiện:** Cần chạy lại `src/lab13.py` sau khi thành viên phụ trách CP4 ghép thêm phần tính cỡ mẫu D1, và đọc kỹ toàn bộ `ho_so_launch_v0.md` trước phiên duyệt chéo Gate 2a để nắm chắc cả phần lỗi và thiết kế pilot khi hội đồng đặt câu hỏi.
