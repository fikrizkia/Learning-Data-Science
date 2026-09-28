import re

postingan = "Belajar #Python dan #DataScience sangat seru untuk karir #AI"

data_bersih = re.findall (r"#\w+", postingan)
data_sub = re.sub (r"#","", postingan)

print("DATA HASTAG KOTOR : ", data_bersih)
print ("DATA BERSIH DARI HASTAG : ", data_sub)