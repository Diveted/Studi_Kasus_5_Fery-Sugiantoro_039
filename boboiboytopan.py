def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "standard":
        tarif = 200000
    elif jenis_kamar == "deluxe":
        tarif = 350000
    else:
        return 0

    total = tarif * lama_menginap
    return total

jenis_kamar = input("masukkan jenis kamar (standard/deluxe): ")
check_in = int(input("masukkan tanggal check-in: "))
check_out = int(input("masukkan tanggal check-out: "))
bulan_tahun = input("masukkan bulan dan tahun: ")

lama_menginap = check_out - check_in

total_biaya = hitung_biaya(jenis_kamar, lama_menginap)

print("\n=== PEMESANAN HOTEL ===")
print("jenis kamar      :", jenis_kamar)
print("check-in         :", check_in, bulan_tahun)
print("check-out        :", check_out, bulan_tahun)
print("lama menginap    :", lama_menginap, "malam")
print("total biaya      : Rp", total_biaya)