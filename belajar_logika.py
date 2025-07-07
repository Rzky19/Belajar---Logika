def rekomendasi_belajar(tidur, makan, stres, aktivitas):
    if (tidur and makan and stres) or \
       (tidur and makan and aktivitas) or \
       (tidur and stres and aktivitas) or \
       (makan and stres and aktivitas):
        return "✅ Disarankan untuk belajar."
    else:
        return "❌ Tidak disarankan belajar."

# Simulasi kombinasi kondisi
kondisi_uji = [
    (1, 1, 1, 1),
    (1, 1, 1, 0),
    (1, 0, 1, 1),
    (0, 1, 1, 1),
    (0, 0, 0, 0)
]

for t, m, s, a in kondisi_uji:
    print(f"Tidur={t}, Makan={m}, Stres={s}, Aktivitas={a} → {rekomendasi_belajar(t, m, s, a)}")
