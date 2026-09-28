def sapaan_role (nama, role="data scientist"):
    pesan = f"Selamat Belajar {nama} Untuk mengejar {role}"
    return pesan


def hitung_kata (text):
    kata = text.split()
    total_kata = len(kata)
    return total_kata

def calculate_mae (y_true, y_pred):
    total_error = 0
    jumlah_data = len (y_true)

    for asli, prediksi in zip (y_true, y_pred):
        selisih = abs (asli - prediksi)
        total_error = total_error + selisih

    mae = total_error / jumlah_data
    return mae