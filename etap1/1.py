girdi = input("karakter dizisini giriniz")
cikti = ""
for i in range(len(girdi)):
	if girdi[len(girdi)-(i+1)].isnumeric() == False:
		if girdi[len(girdi)-(i+1)].isalpha() == True:
			if girdi[len(girdi)-(i+1)] not in cikti:
				cikti += girdi[len(girdi)-(i+1)]
print(cikti)