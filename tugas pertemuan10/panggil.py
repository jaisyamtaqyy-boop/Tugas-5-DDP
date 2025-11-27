import bangun_datar, bangun_ruang

print("=====luas bangun datar=====")
print(f"luas persegi = {bangun_datar.luas_persegi(5)}")
print(f"luas segitiga = {bangun_datar.luas_segitiga(5, 5)}")
print(f"luas linggkaran = {bangun_datar.luas_lingkaran(5)}")
print(f"luas ketupat = {bangun_datar.luas_ketupat(5, 5)}")
print(f"luas jajar genjang = {bangun_datar.luas_jajar_genjang(5, 5)}")


print("=====luas bangun ruang=====")
print(f"luas kubus = {bangun_ruang.luas_kubus(10)}")
print(f"luas balok = {bangun_ruang.luas_balok(10, 12, 15)}")
print(f"luas bola = {bangun_ruang.luas_bola(10)}")
print(f"luas tabung = {bangun_ruang.luas_tabung(10, 15)}")
print(f"luas kerucut = {bangun_ruang.luas_kerucut(10, 15)}")