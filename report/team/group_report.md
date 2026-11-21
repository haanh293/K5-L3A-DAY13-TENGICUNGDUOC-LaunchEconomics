# Báo cáo nhóm · Lab 13: Định giá agent và lập kế hoạch pilot (Gate 2a)

Báo cáo ngắn gọn (2 trang). Số liệu chi tiết nằm trong các file hồ sơ tương ứng; ở đây tổng hợp các kết quả chính và đề xuất của nhóm.

---

## 1. Thông tin nhóm

- Tên nhóm: TENGICUNGDUOC
- Lớp: L3A
- Thành viên: xem [`TEAM.md`](../../TEAM.md)

---

## 2. Mục tiêu và cách tiếp cận

Dự án thực hiện đánh giá toàn diện tính khả thi kinh tế và kỹ thuật của Trợ lý Hoàn phí LogiX-VN trước hội đồng thẩm định Gate 2a. Mục tiêu là trả lời 4 câu hỏi cốt lõi:
1. **Có đáng chạy không?** Sử dụng khung kinh tế học Cost-of-Pass: Tử số cộng mọi lần chạy (kể cả lỗi), cộng thời gian xem lại và làm lại của nhân viên; mẫu số chỉ tính các yêu cầu giải quyết thành công.
2. **Nhân viên có dùng không?** Đo lường tỉ lệ sử dụng (adoption), tỉ lệ bỏ qua gợi ý và xây dựng hệ thống 10 event telemetry mang `trace_id`.
3. **Khi hỏng thì sao?** Phân loại 20 ca lỗi theo 5 nhóm của Google PAIR (gắn nhãn độc lập 2 người) và lập kế hoạch khắc phục có người phụ trách cụ thể.
4. **Pilot thiết kế thế nào để ra quyết định?** Thiết kế A/B testing theo cụm nhân viên (Cluster RCT), giải bài toán cỡ mẫu hiệu dụng với ICC = 0,02 và lập 3 luật dừng 4 vế (NẾU – TRONG – THÌ – KHÔNG THÌ).

---

## 3. Giải pháp

- **Nhiệm vụ A — Mô hình chi phí (CP1):** Viết mã nguồn [`src/lab13.py`](../../src/lab13.py) vượt qua 3 phép thử đáp án biết trước (1,20 · 1,25 · 1,25). Tính toán mô hình chi phí từ trace [`report/team/bang_chi_phi.md`](bang_chi_phi.md): Chi phí trung bình là **4.472 đ** [simulated] (gấp 16,3 lần hóa đơn token). Tách theo loại yêu cầu: `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69×) tiết kiệm chi phí rõ rệt; `quoc_te` (22.515 đ = 1,88×) bị lỗ và chạy lại tới 3 lần không cải thiện; `doi_tac` (10.215 đ = 0,85×) sát ngưỡng nên đưa ra khỏi phạm vi pilot.
- **Nhiệm vụ B — Bảng độ nhạy (CP2):** Thử nghiệm 9 kịch bản độ nhạy tại [`report/team/bang_chi_phi.md`](bang_chi_phi.md). Kết luận: **Số ca làm lại** (+51,8%) và **Tỉ lệ xem lại** (+40,7%) là 2 yếu tố tác động mạnh nhất, trong khi giá token chỉ ảnh hưởng +5,6%. Đặc biệt, nếu xem lại 100% thì chi phí tăng lên 11.743 đ – 12.415 đ (0,98× – 1,03×) [simulated], xóa sạch lợi ích kinh tế so với nhân viên tự làm (12.000 đ). Giới hạn 2 lần chạy là tối ưu cho toàn công ty (6.901.220 đ) [simulated].
- **Nhiệm vụ C — Bảng lỗi (CP3):** Hai thành viên gắn nhãn độc lập 20 ca lỗi tại [`report/team/bang_loi.md`](bang_loi.md) đạt tỉ lệ đồng thuận tuyệt đối **20/20 = 100%** (4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm). Xây dựng bảng khắc phục cho 5 ca tiêu biểu với thước đo phát hiện và một vai trò chịu trách nhiệm.
- **Nhiệm vụ D — Kế hoạch Pilot (CP4):** Soạn thảo [`report/team/pilot_plan.yaml`](pilot_plan.yaml). Chọn phương án chia theo nhân viên (20 đối chứng vs 20 can thiệp, ngẫu nhiên phân tầng theo depot), chấp nhận đánh đổi MDE 6 điểm ($n=859$/nhóm, $m \ge 299$ đơn/người) và thiết lập 3 luật dừng chặt chẽ kèm cơ chế rollback trong 30 phút.
- **Nhiệm vụ E — Chỉ số, Rủi ro & Hồ sơ Launch (CP5):** Hoàn thiện 3 chỉ số tính từ dữ liệu, 2 chỉ số đề xuất, 10 event telemetry có `trace_id` và 3 rủi ro kinh tế tại [`report/team/chi_so.md`](chi_so.md); đúc kết bản hồ sơ launch v0 một trang tại [`report/team/ho_so_launch_v0.md`](ho_so_launch_v0.md).

---

## 4. Kết quả

- **Các con số tài chính cốt lõi:**
  - Chi phí mỗi việc thành công trong phạm vi pilot (`noi_dia` + `hang_nang`): **3.414 đ** [simulated]; cộng chi phí cố định (40 tr/tháng ở 45.000 yc/tháng) là **4.599 đ = 0,38×** so với 12.000 đ nhân viên tự làm [simulated] (tiết kiệm 62% chi phí).
  - Tỉ lệ thành công trong phạm vi pilot: **91,6%** (900/982 ca).
  - Chỉ số chính đợt chạy thử: **82,83%** (đóng trong 24h và không mở lại trong 7 ngày).
  - Tỉ lệ lỗi lọt đến khách: **4,25%** (51/1.200 ca).
- **Đề xuất cuối cùng tại Gate 2a:** **Go có điều kiện**
  - Giới hạn phạm vi nghiêm ngặt: Chỉ pilot trên `noi_dia` và `hang_nang`; loại bỏ `quoc_te` và `doi_tac`.
  - Bốn điều kiện chốt chặn: (1) Vá lỗi đối soát sổ cái hoàn tiền (ca 7, 20) trước khi chạy; (2) Giám đốc vận hành ký duyệt chấp nhận MDE 6 điểm; (3) Đo lường thời gian thực tế bằng event telemetry sau tuần 1; (4) Có lộ trình giảm dần tỉ lệ xem lại theo bậc.

---

## 5. Khó khăn và cách xử lý

1. **Giới hạn số lượng nhân viên CSKH (40 người):** Với 40 nhân viên, phân cụm chỉ đạt cỡ mẫu hiệu dụng tối đa 1.000 < 1.251, không đủ để phát hiện mức chênh 5 điểm phần trăm với power 0,80.
   - *Cách xử lý:* Tính toán chính xác Design Effect ($DE = 6,96$), giải bài toán ngược để xác định MDE khả thi là 6 điểm phần trăm ($n=859$, $m \ge 299$ đơn/người) và công khai đánh đổi mức power còn ~0,64 nếu tác động thật là 5 điểm để Giám đốc vận hành phê duyệt.
2. **Rủi ro chi phí xem lại làm triệt tiêu hiệu quả kinh tế:** Trực giác ban đầu cho rằng nên xem lại 100% để đảm bảo an toàn.
   - *Cách xử lý:* Bảng B4 chứng minh xem lại 100% đẩy chi phí lên 1,03× baseline nhân viên. Nhóm đề xuất lộ trình "Tiered Review" giảm dần tỉ lệ xem lại khi chất lượng agent ổn định (tỉ lệ sửa/bỏ < 15%).

---

## 6. Tổng hợp đóng góp

Nhóm thực thi theo mô hình **Single Writer** (mỗi file chỉ 1 người sửa) đạt 0% xung đột git:
- Người 1: Phụ trách CP1 + CP2, viết code `lab13.py` giai đoạn 1, hoàn thành `bang_chi_phi.md`.
- Người 2: Phụ trách CP3, gắn nhãn độc lập 20 ca lỗi, tính đồng thuận và lập `bang_loi.md`, chuẩn bị `phieu_cham.md`.
- Người 3: Phụ trách CP4, viết code D1 `lab13.py` giai đoạn 2, thiết kế và hoàn thành `pilot_plan.yaml`.
- Người 4: Phụ trách CP5, hoàn thành telemetry & rủi ro trong `chi_so.md`, hồ sơ `ho_so_launch_v0.md`, `group_report.md` và gắn nhãn độc lập CP3.

---

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu thời gian xem lại/làm lại đang là giả lập:** Cần hệ thống đo thời gian thực tế trên UI CSKH ngay tuần đầu pilot để cập nhật lại mô hình chi phí.
- **Độ trễ cập nhật bảng giá:** Cần bổ sung cơ chế tự động xóa bộ nhớ đệm (cache invalidation) khi phòng tài chính cập nhật bảng giá cước mới để tránh lỗi ngầm như ca 17.

---

## 8. Tài liệu tham khảo

1. Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arXiv:2504.13359](https://arxiv.org/abs/2504.13359).
2. Google PAIR, *People + AI Guidebook: Errors + Graceful Failure*, [pair.withgoogle.com](https://pair.withgoogle.com).
3. Tài liệu thống kê `statsmodels.stats.power.NormalIndPower`.
