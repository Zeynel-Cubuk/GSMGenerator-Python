import time
import colorama
from colorama import Fore

# Algoritma
# +│90 Alan Kodu│Sıfırsız Numara

class GSMGenerator(object):
    def __init__(self,alan_kodu="544"):
        self.alan_kodu = alan_kodu

    def banner(self):
        RED = "\033[1;31m"
        BLUE = "\033[1;34m"
        CYAN = "\033[1;36m"
        GREEN = "\033[0;32m"

        print(GREEN+"  ___     ___   __  __    ___     ___    _  _ ")
        print(GREEN+" / __|   / __| |  \/  |  / __|   | __|  | \| | ")
        print(GREEN+"| (_ |   \__ \ | |\/| | | (_ |   | _|   | .` |  ")
        print(GREEN+" \___|   |___/ |_|__|_|  \___|   |___|  |_|\_|  ")
        print(GREEN+" _|----|_|----|_|----|_|----|_|----|_|----|_")
        print(GREEN+" `-0-0-'`-0-0-'`-0-0-'`-0-0-'`-0-0-'`-0-0-'")
        print(CYAN+"#"*47)
        print(CYAN + "# Author      :" + "KIZILYILDIZ✮")
        print(CYAN + "# Instagram   :" + "www.instagram.com/kiziilyildiz")
        print(CYAN + "# GitHub      :" + "www.github.com/Zeynel-Cubuk")
        print(CYAN + "# Title       :" + "gsm_gen.py")
        print(CYAN + "# Date        :" + "15/1/2021")
        print(CYAN + "# Version     :" + "1.0")
        print(CYAN+"#" * 47)

    def generator(self):
        G = '\033[1;32m'  # koyu yesil

        ulke_kodu = "+90"
        self.numaraOrta = ""

        for i in range(0, 10):
            i = str(i)
            self.numaraOrta = i

            for j in range(0, 10):
                j = str(j)
                self.numaraOrta = i + "" + j

                for k in range(0, 10):
                    k = str(k)
                    self.numaraOrta = i + "" + j + "" + k

                    for t in range(0, 10):
                        t = str(t)

                        for v in range(0, 10):
                            v = str(v)

                            for x in range(0, 10):
                                x = str(x)

                                for y in range(0, 10):
                                    y = str(y)

                                    telefon = ulke_kodu + " " + self.alan_kodu + " " + self.numaraOrta + " " + t + v + " " + x + y
                                    time.sleep(0.25)

                                    print(G + "(GSM): " + telefon)

if __name__ == "__main__":
    gsm = GSMGenerator()
    gsm.banner()

    colorama.init()
    alanKodu = input(Fore.LIGHTMAGENTA_EX+"\nAlan Kodu (232-212-312 .etc): ")
    print("")

    gsm = GSMGenerator(alanKodu)
    gsm.generator()