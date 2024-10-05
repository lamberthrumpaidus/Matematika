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
            "25. Bilangan Prima": self.bilangan_prima,
            "26. FPB": self.fpb,
            "27. KPK": self.kpk,
            "28. Deret Aritmatika": self.deret_aritmatika,
            "29. Deret Geometri": self.deret_geometri,
            "30. Persamaan Linear": self.persamaan_linear,
            "31. Persamaan Kuadrat": self.persamaan_kuadrat,
            "32. Integral": self.integral,
            "33. Turunan": self.turunan,
            "34. Peluang": self.peluang,
            "35. Distribusi Normal": self.distribusi_normal,
            "36. Distribusi Binomial": self.distribusi_binomial,
            "37. Distribusi Poisson": self.distribusi_poisson,
            "38. Konversi Desimal ke Biner": self.desimal_ke_biner,
            "39. Konversi Biner ke Desimal": self.biner_ke_desimal,
            "40. Konversi Desimal ke Oktal": self.desimal_ke_oktal,
            "41. Konversi Oktal ke Desimal": self.oktal_ke_desimal,
            "42. Konversi Desimal ke Heksadesimal": self.desimal_ke_heksadesimal,
            "43. Konversi Heksadesimal ke Desimal": self.heksadesimal_ke_desimal,
            "44. Konversi Celcius ke Fahrenheit": self.celcius_ke_fahrenheit,
            "45. Konversi Fahrenheit ke Celcius": self.fahrenheit_ke_celcius,
            "46. Konversi Kilometer ke Mil": self.kilometer_ke_mil,
            "47. Konversi Mil ke Kilometer": self.mil_ke_kilometer,
            "48. Konversi Meter ke Kaki": self.meter_ke_kaki,
            "49. Konversi Kaki ke Meter": self.kaki_ke_meter,
            "50. Konversi Gram ke Kilogram": self.gram_ke_kilogram,
            "51. Konversi Kilogram ke Gram": self.kilogram_ke_gram,
            "52. Konversi Liter ke Mililiter": self.liter_ke_mililiter,
            "53. Konversi Mililiter ke Liter": self.mililiter_ke_liter,
            "54. Konversi Jam ke Menit": self.jam_ke_menit,
            # Additional methods can be added here
        }

    def run(self):
        while True:
            print("\nPilih fungsi matematika yang ingin dijalankan:")
            for key in self.konsep.keys():
                print(key)

            choice = input("Masukkan nomor fungsi (atau 'exit' untuk keluar): ")
            if choice.lower() == 'exit':
                break

            func = self.konsep.get(f"{choice}. {self.konsep.get(choice)}")
            if func:
                params = self.get_parameters(func)
                result = func(*params)
                print("Hasil:", result)
            else:
                print("Pilihan tidak valid.")

    def get_parameters(self, func):
        # Get parameters required for the function
        params_count = func.__code__.co_argcount
        params = []
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

    def bilangan_prima(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def fpb(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def kpk(self, a, b):
        return abs(a * b) // self.fpb(a, b)

    def deret_aritmatika(self, a, d, n):
        return [a + d * i for i in range(n)]

    def deret_geometri(self, a, r, n):
        return [a * (r ** i) for i in range(n)]

    def persamaan_linear(self, a, b):
        return f'y = {a}x + {b}'

    def persamaan_kuadrat(self, a, b, c):
        D = b ** 2 - 4 * a * c
        if D < 0:
            return "Error: Tidak ada akar real."
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return (x1, x2)

    def integral(self, function, a, b, num_steps=1000):
        step = (b - a) / num_steps
        total_area = 0.0
        for i in range(num_steps):
            total_area += function(a + i * step) * step
        return total_area

    def turunan(self, function, x, h=1e-5):
        return (function(x + h) - function(x - h)) / (2 * h)

    def peluang(self, success, trials):
        return success / trials if trials > 0 else "Error: Trials must be greater than zero."

    def distribusi_normal(self, x, mean, std_dev):
        return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mean) / std_dev) ** 2)

    def distribusi_binomial(self, n, k, p):
        comb = self.kombinasi(n, k)
        return comb * (p ** k) * ((1 - p) ** (n - k))

    def distribusi_poisson(self, k, lambd):
        return (lambd ** k * math.exp(-lambd)) / math.factorial(k)

    def desimal_ke_biner(self, n):
        return bin(n).replace("0b", "")

    def biner_ke_desimal(self, b):
        return int(b, 2)

    def desimal_ke_oktal(self, n):
        return oct(n).replace("0o", "")

    def oktal_ke_desimal(self, o):
        return int(o, 8)

    def desimal_ke_heksadesimal(self, n):
        return hex(n).replace("0x", "").upper()

    def heksadesimal_ke_desimal(self, h):
        return int(h, 16)

    def celcius_ke_fahrenheit(self, c):
        return (c * 9/5) + 32

    def fahrenheit_ke_celcius(self, f):
        return (f - 32) * 5/9

    def kilometer_ke_mil(self, km):
        return km * 0.621371

    def mil_ke_kilometer(self, mi):
        return mi / 0.621371

    def meter_ke_kaki(self, m):
        return m * 3.28084

    def kaki_ke_meter(self, ft):
        return ft / 3.28084

    def gram_ke_kilogram(self, g):
        return g / 1000

    def kilogram_ke_gram(self, kg):
        return kg * 1000

    def liter_ke_mililiter(self, l):
        return l * 1000

    def mililiter_ke_liter(self, ml):
        return ml / 1000

    def jam_ke_menit(self, j):
        return j * 60

    def menit_ke_detik(self, m):
        return m * 60

# Example of how to use the class
if __name__ == "__main__":
    matematika = Matematika()
    matematika.run()
