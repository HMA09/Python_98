print("YAŞ HESAPLAMA")
a=int(input("Doğum Yılınızı Giriniz:"))
if a<1900 :
    print("HATA:Doğum Yılınızı dört haneli olarak giriniz!****")
if a>=1900 :
    print("Yaşınız:", 2025-a)
