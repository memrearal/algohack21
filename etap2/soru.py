"""
Muhammed Emre ARAL
"""

import random

# İki sayının toplamını tutacağımız değişken.
toplamlari = 0

# İki sayının toplamı 200 ile 1998 arasında
bas = 200
bitis = 1998

# Hamle sayısını tutan değişken
islem = 0

# Algoritma iki sayının toplamını bulmaya çalışıyor.
devam = True
while devam == True:
	dene = int((bas + bitis)/2)
	print("\nSkor: ",(100-islem))
	print("Programın {}. Tahmini: {}".format(islem+1, dene))
	girdi = int(input("Girdi: "))
	if girdi == 2:
		bitis = dene
	elif girdi == 0:
		toplamlari = dene
		devam = False
	else:
		bas = dene
	islem += 1

# sayının rakamları farklı mı kontrol eden algoritma.
def rakamKontrol(rakam):
	farkli = True
	for i in range(3):
		if str(rakam).count(str(rakam)[i]) != 1:
			farkli = False
	return farkli

print("\n Lütfen Bekleyiniz. \n")

# for döngüsü ile iki sayı alıyor, her iki sayının da rakamları birbirinden farklı ve iki sayının toplamı daha önce bulduğumuz toplam değere eşitse listeye ekliyor.
test = []
for x in range(100, 999):
	for y in range(100, 999):
		if (rakamKontrol(x) and rakamKontrol(y) == True) and (x+y == toplamlari):
			test.append([x,y])

# test edilecek sayı listesindeki sayılardan, basamağı verilen değere eşit olanları filtreliyor.
def filterTestCasesIfEquals(i,b,d):
	# i: hangi sayı
	# b: basamak no
	# d: değer
	global test
	def filterFunc(case):
		if str(case[i])[b] == str(d):
			return True
		else:
			return False

	test = list(filter(filterFunc, test))

# test edilecek sayı listesindeki sayılardan, basamaklarından herhangi birisi verilen değere eşit olmayanları filtreliyor.
def filterTestCasesIfNotEquals(i,d):
	# i: hangi sayı
	# d: değer
	global test
	def filterFunc(case):
		for char in str(case[i]):
			if char == str(d):
				return False
		return True

	test = list(filter(filterFunc, test))

# değer doğru fakat yanlış basamakta ise diğer basamaklarda aynı değerin yer aldığı sayıları filtreliyor.
def filterTestCasesExistButWrongHole(hangiSayi, hangiBasamak, hangiDeger):
	if hangiBasamak == 0:
		aranacakBasamaklar = [1,2]
	elif hangiBasamak == 1:
		aranacakBasamaklar = [0,2]
	else:
		aranacakBasamaklar = [0,1]

	global test	
	def filterFunc(case):
		if str(case[hangiSayi])[aranacakBasamaklar[0]] == str(hangiDeger) or str(case[hangiSayi])[aranacakBasamaklar[1]] == str(hangiDeger):
			return True
		else:
			return False
	test = list(filter(filterFunc, test))


# kullanıcı girdisine göre diğer fonksiyonlere yönlendiren veya sayının bulunduğunu belirten fonksiyon
def tryHardModeOn(sayi,girdi,hangiSayi):
	if girdi == "+++":
		return True
	else:
		for i in range(3):
			if girdi[i] == "+":
				filterTestCasesIfEquals(hangiSayi, i, str(sayi)[i])
			elif girdi[i] == "*":
				filterTestCasesIfNotEquals(hangiSayi, str(sayi)[i])
			else:
				filterTestCasesExistButWrongHole(hangiSayi, i, str(sayi)[i])
		return False

# Algoritma iki sayıyı bulmayı deniyor.
testSayilar = test[int((len(test)-1)/2)];
tahminSayisi = 1
ikinciDevam = True
while ikinciDevam == True:
	print("Programın {}. tahmini: {},{}".format(tahminSayisi, testSayilar[0], testSayilar[1]))
	ilkSayi, ikinciSayi = map(str, input("Girdi: ").split(","))
	x = tryHardModeOn(testSayilar[0], ilkSayi, 0)
	y = tryHardModeOn(testSayilar[1], ikinciSayi, 1)
	if x == True and y == True:
		ikinciDevam = False
		print("Sayılar Bulundu:{},{}".format(testSayilar[0], testSayilar[1]))
		print("Skor:",100-islem)
	else:
		testSayilar = test[random.randint(0, len(test)-1)]
		tahminSayisi += 1
		islem += 1
