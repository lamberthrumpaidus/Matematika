import math
import statistics

class Matematika:
    def __init__(self):
        self.konsep = {
            "1. Penjumlahan": self.penjumlahan,
            "2. Pengurangan": self.pengurangan,
            "3. Perkalian": self.perkalian,
            "4. Pembagian": self.pembagian,
            "5. Akar Kuadrat": self.akar_kuadrat,
            "6. Pangkat": self.pangkat,
            "7. Logaritma": self.logaritma,
            "8. Sinus": self.sinus,
            "9. Cosinus": self.cosinus,
            "10. Tangen": self.tangen,
            "11. Luas Lingkaran": self.luas_lingkaran,
            "12. Keliling Lingkaran": self.keliling_lingkaran,
            "13. Luas Segitiga": self.luas_segitiga,
            "14. Volume Kubus": self.volume_kubus,
            "15. Volume Balok": self.volume_balok,
            "16. Volume Silinder": self.volume_silinder,
            "17. Mean": self.mean,
            "18. Median": self.median,
            "19. Modus": self.modus,
            "20. Variansi": self.variansi,
            "21. Standar Deviasi": self.standar_deviasi,
            "22. Faktorial": self.faktorial,
            "23. Permutasi": self.permutasi,
            "24. Kombinasi": self.kombinasi,
            # Tambahkan fungsi lain jika diperlukan
        }

    def run(self):
        while True:
            print("\nPilih fungsi matematika yang ingin dijalankan:")
            for key in self.konsep.keys():
                print(key)

            choice = input("Masukkan nomor fungsi (atau 'exit' untuk keluar): ")
            if choice.lower() == 'exit':
                break

            func = self.konsep.get(f"{choice}. {list(self.konsep.keys())[int(choice)-1].split('. ')[1]}")
            if func:
                params = self.get_parameters(func)
                result = func(*params)
                print("Hasil:", result)
            else:
                print("Pilihan tidak valid.")

    def get_parameters(self, func):
        params_count = func.__code__.co_argcount
        params = []
        if func in [self.mean, self.median, self.modus, self.variansi, self.standar_deviasi]:
            data_input = input("Masukkan data (dipisahkan dengan koma): ")
            data = list(map(float, data_input.split(',')))
            return [data]
        for i in range(params_count):
            param = input(f"Masukkan parameter {i+1}: ")
            params.append(float(param))  # Convert to float for calculations
        return params

    # Define all the methods below (e.g., penjumlahan, pengurangan, etc.)
    def penjumlahan(self, a, b):
        return a + b

    def pengurangan(self, a, b):
        return a - b

    def perkalian(self, a, b):
        return a * b

    def pembagian(self, a, b):
        return a / b if b != 0 else "Error: Pembagian dengan nol."

    def akar_kuadrat(self, a):
        return math.sqrt(a) if a >= 0 else "Error: Akar kuadrat dari bilangan negatif."

    def pangkat(self, a, b):
        return a ** b

    def logaritma(self, a, base=math.e):
        return math.log(a, base) if a > 0 else "Error: Logaritma dari bilangan non-positif."

    def sinus(self, a):
        return math.sin(math.radians(a))

    def cosinus(self, a):
        return math.cos(math.radians(a))

    def tangen(self, a):
        return math.tan(math.radians(a))

    def luas_lingkaran(self, r):
        return math.pi * r ** 2

    def keliling_lingkaran(self, r):
        return 2 * math.pi * r

    def luas_segitiga(self, a, t):
        return 0.5 * a * t

    def volume_kubus(self, s):
        return s ** 3

    def volume_balok(self, p, l, t):
        return p * l * t

    def volume_silinder(self, r, t):
        return math.pi * r ** 2 * t

    def mean(self, data):
        return statistics.mean(data)

    def median(self, data):
        return statistics.median(data)

    def modus(self, data):
        return statistics.mode(data)

    def variansi(self, data):
        return statistics.variance(data)

    def standar_deviasi(self, data):
        return statistics.stdev(data)

    def faktorial(self, n):
        return math.factorial(n)

    def permutasi(self, n, r):
        return math.factorial(n) // math.factorial(n - r)

    def kombinasi(self, n, r):
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Example of how to use the class
if __name__ == "__main__":
    matematika = Matematika()
    matematika.run()
