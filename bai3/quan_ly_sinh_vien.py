danh_sach_sv = [(8.5, "huy"), (7.0, "manh"), (9.2, "ngo"), (6.5, "dung")]
danh_sach_sv.append((8.0, "em"))
danh_sach_sv.remove((7.0, "manh"))
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])
print("Chi co trong danh sach khong?", (9.2, "ngo") in danh_sach_sv)

danh_sach_sv.sort()
print("Danh sach sau khi sap xep theo diem tang dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")

danh_sach_sv.sort(reverse=True)
print("Danh sach sau khi sap xep theo diem giam dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")