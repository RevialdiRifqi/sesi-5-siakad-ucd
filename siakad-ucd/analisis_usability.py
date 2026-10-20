"""Analisis hasil pengujian usability: skor SUS, task success rate, waktu per tugas.
Jalankan: python analisis_usability.py   (hanya butuh pandas)"""
import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def skor_sus(baris):
    # Item ganjil (positif): skor-1. Item genap (negatif): 5-skor. Jumlah x 2,5 -> 0-100
    total = sum((baris[f"q{i}"] - 1) if i % 2 else (5 - baris[f"q{i}"]) for i in range(1, 11))
    return total * 2.5

def kategori(s):
    return ("Excellent" if s >= 80.3 else "Good" if s >= 68 else "OK/Marginal" if s >= 51 else "Poor")

sus = pd.read_csv("data/sus_responses.csv")
sus["skor_sus"] = sus.apply(skor_sus, axis=1)
rata = sus["skor_sus"].mean()
print("=== SUS per responden ===")
print(sus[["responden", "skor_sus"]].to_string(index=False))
print(f"\nRata-rata SUS: {rata:.1f} -> {kategori(rata)} (batas 'baik' = 68)")

tugas = pd.read_csv("data/tugas_usability.csv")
ringkas = tugas.groupby("tugas").agg(success_rate=("berhasil", "mean"),
                                    waktu_rata2_detik=("waktu_detik", "mean")).round(2)
ringkas["success_rate"] = (ringkas["success_rate"] * 100).round(0).astype(int).astype(str) + "%"
print("\n=== Kinerja per tugas ===")
print(ringkas.to_string())
