print("NOT HESAPLAMA PROGRAMI")
print("=====================================\n")

ad = input("Adınızı Giriniz\t:")
n1 = int(input("1. Yazılı Notun Nedir\t:"))
n2 = int(input("2. Yazılı Notun Nedir\t:"))

ortalama=(n1+n2)//2

if ortalama>90: print(f"Süper. Ortalamanız:",{ortalama})
if ortalama>80: print(f"Güzel. Ortalamanız:",{ortalama})
elif ortalama>50: print(f"{ortalama} ortalama ile geçtiniz.") 
else: print(f"Malesef Kaldınız. Ortalamanız:",{ortalama})   