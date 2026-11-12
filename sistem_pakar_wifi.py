import json

def muat_kb(nama_file):
    with open(nama_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def jalankan_forward_chaining(kb):
    print("=" * 50)
    print(f"Sistem Pakar: {kb['judul']}")
    print("=" * 50)
    print("Jawab pertanyaan dengan 'y' (ya) atau 't' (tidak).\n")
    
    semua_premis = set()
    for aturan in kb["aturan"]:
        for syarat in aturan["jika"]:
            semua_premis.add(syarat)
            
    memori = []
    for premis in sorted(list(semua_premis)):
        jawaban = input(f"Apakah {premis}? (y/t) > ").strip().lower()
        if jawaban == 'y':
            memori.append(premis)
            
    print(f"\nFakta awal yang dimasukkan: {', '.join(memori) if memori else 'tidak ada'}\n")
    print("-" * 50)
    print("Proses Mesin Inferensi (Forward Chaining):")
    print("-" * 50)
    
    jejak_kesimpulan = {}
    siklus = 1
    
    while True:
        aturan_baru_ditemukan = False
        
        for aturan in kb["aturan"]:
            r_id = aturan["id"]
            maka_hasil = aturan["maka"]
            mode = aturan["mode"]
            syarat_list = aturan["jika"]
            
            if maka_hasil in memori:
                continue
                
            if mode == "dan":
                terpenuhi = all(s in memori for s in syarat_list)
            elif mode == "atau":
                terpenuhi = any(s in memori for s in syarat_list)
            else:
                terpenuhi = False
                
            if terpenuhi:
                memori.append(maka_hasil)
                jejak_kesimpulan[maka_hasil] = {
                    "aturan": r_id,
                    "syarat": syarat_list,
                    "sumber": aturan["sumber"]
                }
                print(f"Siklus {siklus}: {r_id} -> {maka_hasil}")
                aturan_baru_ditemukan = True
                siklus += 1
                break
                
        if not aturan_baru_ditemukan:
            print(f"Siklus {siklus}: tidak ada aturan baru, berhenti\n")
            break

    semua_syarat = set()
    for aturan in kb["aturan"]:
        for s in aturan["jika"]:
            semua_syarat.add(s)
            
    kesimpulan_akhir = [m for m in jejak_kesimpulan.keys() if m not in semua_syarat]
    
    print("=" * 50)
    if kesimpulan_akhir:
        print(f"Kesimpulan: {', '.join(kesimpulan_akhir)}")
        print("Alasan:")
        for k in kesimpulan_akhir:
            cetak_alasan(k, jejak_kesimpulan, indent=2)
    else:
        print("Kesimpulan: tidak ada (kasus negatif)")
        
    print("-" * 50)
    print(f"Catatan: {kb['batas']}")
    print("=" * 50)

def cetak_alasan(target, jejak, indent=2):
    if target in jejak:
        info = jejak[target]
        syarat_str = ", ".join(info["syarat"])
        print(f"{' ' * indent}{target}  <- {info['aturan']} ({syarat_str}) [{info['sumber']}]")
        for s in info["syarat"]:
            if s in jejak:
                cetak_alasan(s, jejak, indent + 4)

if __name__ == "__main__":
    kb = muat_kb("kb_wifi.json")
    jalankan_forward_chaining(kb)