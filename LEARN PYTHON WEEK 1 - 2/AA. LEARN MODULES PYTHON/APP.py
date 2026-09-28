from AI_UTILS import hitung_kata, sapaan_role, calculate_mae

# Bagian Sapaan Nama
pesan = sapaan_role("Fikri", role="AI Engineer")
print (pesan)


# Bagian Hitung Kata
prompt_text = "Machine learning is transforming how we build artificial intelligence models"

jumlah = hitung_kata(prompt_text)

print (f"TEKS:'{prompt_text}'")
print (f"JUMLAH KATA:'{jumlah}'")

# Bagian Calculat MAE
y_true = [100, 200, 300, 400]
y_pred = [110, 190, 280, 420]

Calculate = calculate_mae (y_true, y_pred)

print(f"INI ANGKA MAE NYA :{Calculate}")