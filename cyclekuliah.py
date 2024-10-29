from metaflow import FlowSpec, step

class KuliahInformatikaFlow(FlowSpec):

    @step
    def start(self):
        print("Mulai proses mengikuti kuliah di Informatika.")
        self.next(self.bayar_spp)

    @step
    def bayar_spp(self):
        print("Langkah 1: Bayar SPP.")
        # Simulasi proses pembayaran
        self.pembayaran_berhasil = True  # Ganti dengan logika pembayaran yang sesuai
        if self.pembayaran_berhasil:
            print("Pembayaran SPP berhasil.")
        else:
            print("Pembayaran SPP gagal.")
        self.next(self.pengambilan_mata_kuliah)

    @step
    def pengambilan_mata_kuliah(self):
        print("Langkah 2: Pengambilan mata kuliah.")
        self.next(self.nilai_uts_uas)

    @step
    def nilai_uts_uas(self):
        print("Langkah 3: Menginput nilai UTS dan UAS.")
        # Simulasi input nilai
        self.nilai_uts = 90  # Ganti dengan input nilai yang sesuai
        self.nilai_uas = 80  # Ganti dengan input nilai yang sesuai
        self.next(self.penentuan_nilai_akhir)

    @step
    def penentuan_nilai_akhir(self):
        print("Langkah 4: Menentukan nilai akhir mata kuliah.")
        self.nilai_akhir = (self.nilai_uts + self.nilai_uas) / 2
        if 85 <= self.nilai_akhir <= 100:
            self.hasil_nilai = 'A'
        else:
            self.hasil_nilai = 'B'
        
        print(f"Nilai UTS: {self.nilai_uts}, Nilai UAS: {self.nilai_uas}, Nilai Akhir: {self.nilai_akhir}, Hasil: {self.hasil_nilai}")
        self.next(self.end)

    @step
    def end(self):
        print("Proses selesai.")

if __name__ == '__main__':
    KuliahInformatikaFlow()