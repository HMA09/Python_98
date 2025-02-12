print("Newton’un Hareket Yasası")
print("Newton hareket yasasına göre bir cismin belirli bir yükseklikten serbest bırakıldığında")
print("Yere Düşme Süresi ile Serbest bırakıldığı yüksekliği bulabilir yada")
print("Serbest bırakıldığı yüksekliği ile Yere Düşme Süresi bulabilir.")
print("╔══════════════════════╗")
print("║Newton Hareket Yasası ║")
print("║                      ║")
print("║ 1-Yüksekliği?        ║")
print("║ 2-Yere Düşme Süresi? ║")
print("║                      ║")
print("║ Hangisini Hesaplamak ║")
print("║      İstersin?       ║")
print("╚══════════════════════╝")

a=int(input("Seçiminizi Nedir:"))
import math
if a==1:
    t=int(input("Cismin Yere Düşme Süresini Giriniz:"))
    print("Cismin yüksekliği:", 1/2*9.81*t**2)
    input()
if a==2:
    h=int(input("Cismin Yerden Yüksekliğini Giriniz:"))
    print("Cismin yere düşme süresi:", math.sqrt(h/(9.81/2)))
    input()
