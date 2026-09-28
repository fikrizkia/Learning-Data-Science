import re

teks_kontak = "Hubungi admin di nomor 08123456789 atau 08567890123 jika ada kendala."

nomor_telepon = re.findall(r"\d+", teks_kontak)


print (nomor_telepon)