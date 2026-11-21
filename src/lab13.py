"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs)

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=cps,
        hoa_don_moi_yc=hoa_don_moi_yc,
    )


def in_ket_qua_cp1(runs, reqs):
    """In kết quả Nhiệm vụ A1, A2, A3, A4."""
    print('\n=== A1 · Ba phép thử đáp án biết trước (p = 0,8) ===')
    print(f'  Tối đa 2 lần chạy           : {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  Chạy đến khi đúng           : {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  Hệ số chi phí tối đa 3 lần  : {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    print('\n=== A2 · Mô hình chi phí từ trace ===')
    kq = mo_hinh(runs, reqs)
    for ten, gia_tri in kq.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:16s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:16s} {gia_tri:>14,.0f}')
    so_lan_gap = kq['cps'] / kq['hoa_don_moi_yc']
    print(f'  CPS / hoá đơn mỗi yêu cầu   : {so_lan_gap:.1f}x [simulated]')
    print(f'  Tỉ trọng làm lại            : {kq["lam_lai"] / kq["tong"] * 100:.1f}% [simulated]')
    print(f'  Tỉ trọng xem lại            : {kq["xem_lai"] / kq["tong"] * 100:.1f}% [simulated]')
    print(f'  Tỉ trọng giờ nhân viên      : {(kq["xem_lai"] + kq["lam_lai"]) / kq["tong"] * 100:.1f}% [simulated]')
    chi_phi_he_thong_yc = (kq['tong'] + (len(reqs) - kq['thanh_cong']) * BASELINE) / len(reqs)
    print(f'  Chi phí cả hệ thống/yêu cầu : {chi_phi_he_thong_yc:,.0f} đ ({chi_phi_he_thong_yc / BASELINE:.2f}x) [simulated]')

    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f'{"Loại":12s} {"Số YC":>6s} {"Thành công":>11s} {"Lần/YC":>8s} {"CPS [sim]":>12s} {"So 12.000đ":>11s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, sub)
        tl_tc = r['thanh_cong'] / len(sub) * 100
        lan_tb = sub['so_lan_chay'].mean()
        print(f'{loai:12s} {len(sub):>6d} {tl_tc:>10.1f}% {lan_tb:>8.2f} {r["cps"]:>11,.0f}đ {r["cps"] / BASELINE:>10.2f}x')

    print('\n  Tỉ lệ status == ok theo lần chạy (attempt):')
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(int)
    bang_ok = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print(bang_ok.loc[['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']].round(1).to_string())

    print('\n=== A4 · Chi phí cố định 40 triệu đ/tháng (noi_dia + hang_nang) ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    chi_phi_co_dinh = 40_000_000
    print(f'  CPS biến đổi trong phạm vi  : {kq_pv["cps"]:,.0f} đ ({kq_pv["thanh_cong"]} việc thành công / {len(reqs)} mẫu) [simulated]')
    for nhan, khoi_luong in [('45.000 YC/tháng', 45_000), ('22.500 YC/tháng (1/2)', 22_500)]:
        viec_thang = khoi_luong * (kq_pv['thanh_cong'] / len(reqs))
        co_dinh_moi_viec = chi_phi_co_dinh / viec_thang
        tong_cps = kq_pv['cps'] + co_dinh_moi_viec
        print(f'  {nhan:22s}: {viec_thang:>7,.0f} việc | cố định {co_dinh_moi_viec:>6,.0f}đ | tổng {tong_cps:>6,.0f}đ ({tong_cps / BASELINE:.2f}x) [simulated]')


def in_ket_qua_cp2(runs, reqs):
    """In kết quả Nhiệm vụ B1, B2, B3, B4."""
    print('\n=== B1 · Bảng độ nhạy (đổi từng yếu tố) [simulated] ===')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    print(f'  {"Gốc (A2)":28s} {goc:>8,.0f} đ')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / goc - 1.0) * 100
        print(f'  {ten:28s} {cps:>8,.0f} đ ({pct:+6.1f}%)')

    print('\n=== B2 · Đổi một cặp (giá token x2 + tỉ lệ xem lại x2) [simulated] ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f'  Token x2 + Xem lại x2       : {cps_cap:,.0f} đ ({(cps_cap / goc - 1.0) * 100:+.1f}%)')

    print('\n=== B3 · Giới hạn chạy lại và chi phí cả hệ thống [simulated] ===')
    print(f'{"Giới hạn":10s} {"Tổng trợ lý":>14s} {"Không TC":>10s} {"Cả hệ thống":>14s} {"CPS":>10s}')
    for lim in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=lim)
        khong_tc = len(reqs) - r['thanh_cong']
        ca_he_thong = r['tong'] + khong_tc * BASELINE
        print(f'{f"{lim} lần":10s} {r["tong"]:>13,.0f}đ {khong_tc:>10d} {ca_he_thong:>13,.0f}đ {r["cps"]:>9,.0f}đ')

    print('\n=== B4 · Xem lại 100% (phạm vi noi_dia + hang_nang) [simulated] ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    co_ok = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    thanh_cong_pv = int((pham_vi['ket_qua'] == 'thanh_cong').sum())
    token_tool_pv = (
        runs_pv['tokens_in'] / 1000.0 * GIA_VAO
        + runs_pv['tokens_out'] / 1000.0 * GIA_RA
        + runs_pv['tool_calls'] * GIA_TOOL
    ).sum()
    xem_lai_100 = co_ok * 5 * LUONG_PHUT

    lam_lai_9p = so_lam_lai * 9 * LUONG_PHUT
    tong_9p = token_tool_pv + xem_lai_100 + lam_lai_9p
    cps_9p = tong_9p / thanh_cong_pv
    hoa_von_9p = (BASELINE * thanh_cong_pv - token_tool_pv - lam_lai_9p) / (co_ok * LUONG_PHUT)

    tb_phut_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    lam_lai_tb = so_lam_lai * tb_phut_lam_lai * LUONG_PHUT
    tong_tb = token_tool_pv + xem_lai_100 + lam_lai_tb
    cps_tb = tong_tb / thanh_cong_pv
    hoa_von_tb = (BASELINE * thanh_cong_pv - token_tool_pv - lam_lai_tb) / (co_ok * LUONG_PHUT)

    print(f'  YC có >=1 run ok: {co_ok} | ca lam_lai: {so_lam_lai} | thanh_cong: {thanh_cong_pv} | token+tool: {token_tool_pv:,.0f}đ')
    print(f'  Giả định 9 phút/ca làm lại  : tổng {tong_9p:,.0f}đ -> CPS {cps_9p:,.0f}đ ({cps_9p / BASELINE:.2f}x), hoà vốn <= {hoa_von_9p:.1f} phút/lần xem')
    print(f'  Trung bình thực tế {tb_phut_lam_lai:.1f}p/ca : tổng {tong_tb:,.0f}đ -> CPS {cps_tb:,.0f}đ ({cps_tb / BASELINE:.2f}x), hoà vốn <= {hoa_von_tb:.1f} phút/lần xem')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_ket_qua_cp1(runs, reqs)
    in_ket_qua_cp2(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu (Người 3 bổ sung sau khi pull).
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
