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

def solKosegen(matrix):
	liste = []
	for i in range(len(matrix[0])):
		liste.append(matrix[i][i])
	return liste

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
	capraz = solKosegen(matrix)
	patternler = []
	tryHard="".join(capraz)
	bulus = [[m.start(0), m.end(0)-1] for m in re.finditer(oruntu, tryHard)]
	return bulus

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

	caprazOruntuler = []
	for cap in matrixCapraz(matrix, oruntu):
		baslangic = ((cap[0]) * len(matrix[0])) + cap[0]+1
		orR = []
		for i in range(len(oruntu)):
			deger = baslangic+(i*(len(matrix[0])+1))
			orR.append(deger)
		caprazOruntuler.append(orR)


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
	for k,oruntuler in enumerate(yatayOruntuler+dikeyOruntuler+caprazOruntuler):
		oruntuX = ""
		for el in oruntuler:
			oruntuX += "["+str(el)+"]"
		print("{}. bulunan örüntü: {}".format(k+1,oruntuX))
	print("Toplam {} tane örüntü bulundu.".format(len(yatayOruntuler+dikeyOruntuler+caprazOruntuler)))
test_case(matrix)