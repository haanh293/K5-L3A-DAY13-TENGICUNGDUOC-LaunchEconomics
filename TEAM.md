# Team

## Thông tin nhóm

- Tên nhóm: Nhóm 4 (LogiX-Economics)
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-TENGICUNGDUOC-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `main`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò | File độc quyền phụ trách |
| --: | ------ | ---- | ----- | ------ | ------- | ------------------------ |
|   1 | Thành viên 1 | 20220001 | tv1@sis.hust.edu.vn | github1 | **Kinh tế & Độ nhạy (CP1 + CP2)**: Viết code A1–B4, tính toán Cost-of-Pass, đối chiếu số liệu | `src/lab13.py` (phase 1), `report/team/bang_chi_phi.md` |
|   2 | Thành viên 2 | 20220002 | tv2@sis.hust.edu.vn | github2 | **Bảng lỗi & Duyệt chéo (CP3)**: Gán nhãn độc lập 20 ca lỗi, tính tỷ lệ đồng thuận, lập bảng khắc phục | `report/team/bang_loi.md`, `report/team/phieu_cham.md` |
|   3 | Thành viên 3 | 20220003 | tv3@sis.hust.edu.vn | github3 | **Thiết kế Pilot (CP4)**: Code D1 (statsmodels), thiết kế A/B testing theo cụm nhân viên, viết 3 luật dừng | `report/team/pilot_plan.yaml`, `src/lab13.py` (phase 2) |
|   4 | Thành viên 4 (Lead) | 20225827 | tv4@sis.hust.edu.vn | github4 | **Chỉ số, Rủi ro & Hồ sơ Launch (CP5 + Repo Lead)**: Telemetry 10 event, rủi ro kinh tế, hồ sơ Gate 2a | `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md` |

*Ghi chú quy tắc:*
- Bốn vai của lab được phân bổ minh bạch theo cơ chế Single Writer (0% Git conflict).
- Đổi người viết code sau giờ giải lao: Người 1 code CP1+CP2, sau đó Người 3 code CP4 trong `src/lab13.py`.
- Hai người gắn nhãn độc lập ở CP3: Người 2 và Người 4 thực hiện gắn nhãn độc lập trong 8 phút không trao đổi, sau đó Người 4 gửi danh sách nhãn qua chat để Người 2 điền vào `bang_loi.md`.

---

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng `report/team/<MSSV>_<HoTen>.md`.

### Thành viên 4 (Repo Lead / Gatekeeper)
- **MSSV:** 20225827
- **Phần việc phụ trách:** Quản trị repo, phân phối tiến độ; hoàn thiện Nhiệm vụ E1, E2 (`chi_so.md`); gán nhãn độc lập 20 ca lỗi CP3; tổng hợp hồ sơ Gate 2a (`ho_so_launch_v0.md`); viết báo cáo nhóm (`group_report.md`).
- **Đóng góp cụ thể:**
  - Thiết kế kiến trúc phân công lao động song song 0% xung đột git.
  - Tính thử 3 chỉ số từ 1.200 records CSV và đề xuất 2 chỉ số mới (đo lường adoption & audit sai tiền).
  - Chuẩn hóa 10 event telemetry có `trace_id` kèm ma trận kiểm tra chéo (Cross-check).
  - Lượng hóa 3 kịch bản rủi ro kinh tế lớn nhất từ ma trận độ nhạy.
  - Độc lập gán nhãn 20 ca lỗi theo chuẩn Google PAIR đạt 100% đồng thuận.
  - Xây dựng hồ sơ launch v0 với khuyến nghị "Go có điều kiện" và 4 điều kiện chốt chặn.
- **Bằng chứng:** Các file `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md`.
