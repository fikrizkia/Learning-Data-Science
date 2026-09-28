import re

ulasan = "Model AI v2 ini memiliki 5 keunggulan dibanding model v1 tahun 2024"

bersih = re.sub(r"[^a-zA-Z\s]", "", ulasan)

print("Sebelum", ulasan)
print("Setelah", bersih)