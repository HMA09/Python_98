print("İDEAL KİLO HESAPLAMA")

print("╔═════════════════════╗")
print("║   CİNSİYET SEÇİMİ   ║")
print("║                     ║")
print("║  1-ERKEK            ║")
print("║  2-KADIN            ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")

c=int(input("Seçiminiz Nedir:"))
b=int(input("Boyunuzu Giriniz:"))

if c ==1:
    print("İdeal Kilonuz:", 50+(2.3/2.54)*(b-152.4))
if c ==2:
    print("İdeal Kilonuz:", 45.5+(2.3/2.54)*(b-152.4))
