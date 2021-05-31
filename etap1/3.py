import re

matrix = []

def matrixYukle():
	with open("oruntumatrisi.txt") as f:
		for satir in f.readlines():
			satirM = []
			for element in satir.split("	"):
				satirM.append(str(int(element)))
			matrix.append(satirM)
		f.close()

def matrixYatay(matrix, oruntu):
	patternler = []
	for satir in matrix:
		tryHard="".join(satir)
		bulus = [[m.start(0), m.end(0)-1] for m in re.finditer(oruntu, tryHard)]
		if bulus == []:
			patternler.append([])
		else:
			patternler.append(bulus)
	return patternler

def column(matrix):
	columnler = []
	for i in range(len(matrix[0])):
		columnler.append([row[i] for row in matrix])
	return columnler

def matrixDikey(matrix, oruntu):
	dikeyler = column(matrix)
	patternler = []
	for k,satir in enumerate(dikeyler):
		tryHard="".join(satir)
		bulus = [[m.start(0), m.end(0)-1] for m in re.finditer(oruntu, tryHard)]
		if bulus == []:
			patternler.append([])
		else:
			patternler.append(bulus)
	return patternler

def matrixCapraz(matrix, oruntu):
	caprazOruntuler = []
	for x in range(len(matrix)-(len(oruntu)-1)):
		for y in range(len(matrix[0])-(len(oruntu)-1)):
			kontrol=""
			for i in range(len(oruntu)):
				kontrol += matrix[x+i][y+i]
			noktalar = []
			for i in range(len(oruntu)):
				nokta = (x+i)*len(matrix[0]) + y+i + 1
				noktalar.append(nokta)
			if kontrol == oruntu:
				caprazOruntuler.append(noktalar)
	return caprazOruntuler

def test_case(matrix):
	matrixYukle()
	oruntu = input("Örüntü: ")

	yatayOruntuler = []
	for yat in matrixYatay(matrix, oruntu):
		for elem in yat:
			x = yat.index(elem)+1*len(matrix[0])+elem[0]
			orR = []
			for i in range(len(oruntu)):
				orR.append(x+i)
			yatayOruntuler.append(orR)
	dikeyOruntuler = []
	for dik in matrixDikey(matrix, oruntu):
		for elem in dik:
			x = elem[0]
			y = elem[1]
			baslangic = (x) * len(matrix[0])
			bitis = (y) * len(matrix[0])
			orR = []
			for i in range(len(oruntu)):
				orR.append(baslangic+i*len(matrix[0]))
			dikeyOruntuler.append(orR)
	caprazOruntuler = matrixCapraz(matrix,oruntu)
	for k,oruntuler in enumerate(yatayOruntuler+dikeyOruntuler+caprazOruntuler):
		oruntuX = ""
		for el in oruntuler:
			oruntuX += "["+str(el)+"]"
		print("{}. bulunan örüntü: {}".format(k+1,oruntuX))
	print("Toplam {} tane örüntü bulundu.".format(len(yatayOruntuler+dikeyOruntuler+caprazOruntuler)))

test_case(matrix)
