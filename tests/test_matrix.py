"""
Bộ kiểm thử tự động (Unit Test) cho cơ sở dữ liệu phôi tròng:
1. SV VIP 1.67 (Mã 05587: Aspherique_Mr7_SF)
2. SV VIP 1.60 (Mã 00466: Aspherique_MR8_SF_Extended)
3. RX PAL 1.60 sht/reg (Mã 03023: FBS_Mr8_SF)
"""
import json
import os

def test_lens(file_name, test_cases):
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", file_name)
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    matrix = data["matrix"]
    print(f"\n=== KIỂM THỬ MA TRẬN: {data['name']} ===")
    print(f"Dải SPH: {data['sph_min']} đến {data['sph_max']} D | Dải CYL: {data['cyl_min']} đến {data['cyl_max']} D")

    all_pass = True
    for sph, cyl, expected, desc in test_cases:
        actual = matrix.get(sph, {}).get(cyl, 0)
        # Handle string or int equality
        passed = str(actual) == str(expected)
        status = "✅ PASS" if passed else "❌ FAIL"
        if not passed:
            all_pass = False
        print(f"[{status}] SPH: {sph:>6} | CYL: {cyl:>6} => Thực tế: Ø{actual:<5} | Mong đợi: Ø{expected:<5} ({desc})")

    return all_pass

def main():
    cases_167 = [
        ("-3.25", "-2.25", 80, "Vùng Hồng (Ø80)"),
        ("-6.00", "-2.00", 80, "Ranh giới cận vừa: Vùng Hồng (Ø80)"),
        ("-7.00", "-2.00", 75, "Ranh giới cận cao: Vùng Tím (Ø75)"),
        ("-10.00", "-2.00", 70, "Vùng Xanh dương (Ø70)"),
        ("-16.00", "0.00", 65, "Cực đại cận SPH -16: Vùng Xanh lá (Ø65)"),
        ("8.00", "0.00", 65, "Cực đại viễn SPH +8: Vùng Xanh lá (Ø65)"),
        ("8.00", "-4.50", 60, "Vùng Cam (Ø60)"),
        ("8.00", "-6.00", 55, "Vùng Đỏ (Ø55)"),
        ("-16.00", "-6.00", 0, "Vượt dải (0)"),
    ]

    cases_160 = [
        ("10.00", "0.00", 65, "Cực đại viễn SPH +10: Vùng Xanh lá (Ø65)"),
        ("10.00", "-4.25", 60, "Viễn cao + loạn: Vùng Hồng (Ø60)"),
        ("10.00", "-6.00", 60, "Viễn cao + loạn cực đại: Vùng Hồng (Ø60)"),
        ("4.00", "-2.00", 70, "Viễn vừa: Vùng Xanh dương (Ø70)"),
        ("0.00", "-2.00", 75, "Độ thấp: Vùng Tím (Ø75)"),
        ("-4.00", "-2.00", 75, "Cận vừa: Vùng Tím (Ø75)"),
        ("-8.00", "-2.00", 70, "Cận cao: Vùng Xanh dương (Ø70)"),
        ("-12.00", "-1.00", 65, "Cận rất cao: Vùng Xanh lá (Ø65)"),
        ("-13.00", "-6.00", 0, "Vượt dải (0)"),
    ]

    cases_pal_160 = [
        ("8.00", "0.00", "70/75", "Cực đại viễn SPH +8: Vùng Xanh lá (Ø70/75)"),
        ("8.00", "-5.50", "65/70", "Viễn cao + loạn cao: Vùng Tím (Ø65/70)"),
        ("6.00", "-2.00", "75/80", "Viễn vừa: Vùng Xanh dương (Ø75/80)"),
        ("0.00", "-2.00", "75/80", "Độ 0: Vùng Xanh dương (Ø75/80)"),
        ("-4.00", "-2.00", "75/80", "Cận vừa: Vùng Xanh dương (Ø75/80)"),
        ("-8.00", "-1.00", "70/75", "Cận cao SPH -8 CYL -1: Vùng Xanh lá (Ø70/75)"),
        ("-5.00", "-5.50", "60/65", "Cận vừa + loạn cao: Vùng Hồng (Ø60/65)"),
        ("-10.00", "0.00", "65/70", "Cận rất cao SPH -10: Vùng Tím (Ø65/70)"),
        ("-12.00", "0.00", "60/65", "Cực đại cận SPH -12: Vùng Hồng (Ø60/65)"),
        ("-12.00", "-6.00", 0, "Vượt dải (0)"),
    ]

    cases_pal_167 = [
        ("9.00", "0.00", "65/70", "Cực đại viễn SPH +9: Vùng Xanh lá (Ø65/70)"),
        ("9.00", "-6.00", "65/70", "Cực đại viễn SPH +9 CYL -6: Vùng Xanh lá (Ø65/70)"),
        ("8.00", "0.00", "70/75", "Viễn SPH +8 CYL 0: Vùng Xanh dương (Ø70/75)"),
        ("8.00", "-5.00", "70/75", "Viễn SPH +8 CYL -5: Vùng Xanh dương (Ø70/75)"),
        ("8.00", "-5.25", "65/70", "Viễn SPH +8 CYL -5.25: Vùng Xanh lá (Ø65/70)"),
        ("6.00", "0.00", "75/80", "Viễn vừa SPH +6: Vùng Tím (Ø75/80)"),
        ("0.00", "-2.00", "75/80", "Độ 0 SPH: Vùng Tím (Ø75/80)"),
        ("-5.00", "-6.00", "65/70", "Cận SPH -5 CYL -6: Vùng Xanh lá (Ø65/70)"),
        ("-5.25", "-6.00", "60/65", "Cận SPH -5.25 CYL -6: Vùng Hồng (Ø60/65)"),
        ("-12.00", "0.00", "60/65", "Cực đại cận SPH -12 CYL 0: Vùng Hồng (Ø60/65)"),
        ("-12.00", "-0.25", 0, "Vượt dải SPH -12 CYL -0.25: Vượt dải (0)"),
        ("-12.00", "-6.00", 0, "Vượt dải (0)"),
    ]

    p1 = test_lens("sv_vip_167.json", cases_167)
    p2 = test_lens("sv_vip_160.json", cases_160)
    p3 = test_lens("pal_160.json", cases_pal_160)
    p4 = test_lens("pal_167.json", cases_pal_167)

    print("\n" + "="*50)
    if p1 and p2 and p3 and p4:
        print("🎉 TẤT CẢ 4 BỘ MA TRẬN (SV 1.67, SV 1.60, RX PAL 1.60, RX PAL 1.67) ĐỀU ĐẠT CHÍNH XÁC 100%!")
    else:
        print("⚠️ CÓ LỖI XẢY RA TRONG DỮ LIỆU!")
    print("="*50)

if __name__ == "__main__":
    main()
