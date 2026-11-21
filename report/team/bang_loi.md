# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Thành viên 2 (Người 2) · Người gắn nhãn 2: Thành viên 4 (Người 4) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Kết quả đối chiếu:** Cả hai thành viên gắn nhãn độc lập trùng khớp tuyệt đối **20/20 ca** (đạt tỉ lệ đồng thuận 100%, vượt mức yêu cầu $\ge 80\%$). Không có ca nào bất đồng nhãn giữa hai người.
- **Quy tắc phân biệt theo nguyên nhân gốc cho các ca dễ nhầm lẫn:**
  - **Ca 6, 9 là Do người dùng (không phải Hệ thống):** Nguyên nhân gốc là khách chọn sai mục hoặc nhập sai định dạng mã; việc trợ lý chưa thông minh để gợi ý phân loại đúng là vấn đề nằm ở cột giải pháp khắc phục.
  - **Ca 13 là Giới hạn hệ thống (không phải Hệ thống):** Bảo hiểm hàng hóa là sản phẩm của đối tác bên ngoài nằm ngoài phạm vi phục vụ và dữ liệu của trợ lý.
  - **Ca 8, 15 là Hệ thống (không phải Ngầm):** Lỗi tính sai hoặc viện dẫn điều khoản không tồn tại đã lộ ra ngoài văn bản hoặc bị nhân viên bắt được khi kiểm tra.
  - **Ca 18 là Ngữ cảnh (không phải Do người dùng hay Hệ thống):** Trợ lý tính tiền hoàn toàn đúng theo chính sách, chỉ thiếu ngữ cảnh giải thích công thức tính khiến khách hàng hiểu lầm.
  - **Ca 12, 17 là Ngầm:** Trợ lý vẫn trả kết quả thành công và không kích hoạt cảnh báo bề nổi, nhưng âm thầm phát sinh chi phí token gấp 3 suốt 3 tuần hoặc áp dụng bảng giá cũ gây lệch tiền 212 đơn mà không ai hay biết.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tự động tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh trực quan | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn “đã hoàn” không có bản ghi sổ cái ok cùng `trace_id`; cảnh báo ngay khi phát hiện > 0 ca | Chỉ báo “đã hoàn” khi sổ cái trả mã kết quả thành công; lỗi 503 sau 3 lần retry thì báo “đang xử lý” và tự động chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại vì khiếu nại số tiền nhưng kiểm tra thấy đúng chính sách, đo theo tuần; cảnh báo khi > 1,5% số ca/tuần | Mẫu tin nhắn luôn ghi rõ chi tiết công thức tính toán: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với lý do `reason = thieu_du_lieu`, theo dõi hàng ngày theo loại yêu cầu | Giữ cơ chế chuyển giao kèm bản tóm tắt nội dung; đưa các đơn thuộc chặng quốc tế ra khỏi phạm vi thử nghiệm pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra đối soát ngẫu nhiên 100 đơn/tuần so với bảng giá hiện hành; ngưỡng kích hoạt cảnh báo khi > 1% đơn bị lệch | Tự động xóa bộ nhớ đệm (cache invalidation) khi cập nhật bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng đối soát |
