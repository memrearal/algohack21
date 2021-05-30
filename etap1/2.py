import os
if os.path.exists("toplamlar.txt"):
  os.remove("toplamlar.txt")
rakamlar = []
def rakamToplamBul(sayi):
	sayi = int(sayi)
	sayi = str(sayi)
	toplam = 0
	for i in range(len(sayi)):
		if sayi[i] != "\n":
			toplam += int(sayi[i])
	return toplam

with open('sayilar.txt') as f:
    lines = f.readlines()
    for line in lines:
    	rakamTop = 0
    	girdi = line
    	devam = True
    	tryHard = []
    	while devam == True:
    		sonuc = rakamToplamBul(girdi)
    		if sonuc <= 9:
    			rakamTop = sonuc
    			rakamlar.append([int(line), tryHard, rakamTop])
    			tryHard = []
    			devam = False
    		else:
    			tryHard.append(str(sonuc))
    			girdi = sonuc
    f.close()

with open('toplamlar.txt', 'a') as f:
	string = ""
	for k, r in enumerate(rakamlar):
		tryHard=" ".join(r[1])
		if k != len(rakamlar)-1:
			if tryHard == " ":
				string += str(r[2]) + "\n"
			else:
				string += tryHard + " " + str(r[2]) + "\n"
		else:
			if tryHard == " ":
				string += str(r[2]) + "\n"
			else:
				string += tryHard + " " + str(r[2])
	f.write(string)
	f.close()