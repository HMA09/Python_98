print(range(6))
print(*range(6))
print(*range(6,9))
print(*range(6,15,2))
print(*range(60,100,5))
print(range(60,100,5))

print(*range(60,100,5),sep="-") #sep: separate
print(*range(60,100,5),sep="\n")
print(*range(60,100,5),sep="\t")

print("muz","nar","dut",sep="--")

print("Adınızı giriniz:")
print("Soyadınızı giriniz:")

print("Adınızı giriniz:",end="\n")
print("Soyadınızı giriniz:",end="\n")

print("Adınızı giriniz:",end="\t")
print("Soyadınızı giriniz:",end="\t")


print("Adınızı giriniz:",end="\t")
print("Soyadınızı giriniz:",end="#Bitti")
