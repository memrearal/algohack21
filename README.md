# AlgoHack '21 Problem Setleri Çözümlerim

## 1. Etap - Soru 1
Kullanıcıdan alınan bir karakter dizisinin içerisindeki harfleri, dizinin sonundan başına doğru tekil bir şekilde yazdıran program kodunu yazınız.

#### Örnek program çıktısı:
**Kullanıcının girdiği dizi:** “Hsh72_i,oa5dalh-ih23” **Program çıktısı:** hiladosH

#### Dikkat Edilmesi Gereken Noktalar:
• Girilen metindeki harfler, tekil olarak sondan başa doğru yazılmalıdır. Baştan sona doğru yazdırılan kodlar değerlendirilmeyecektir.
• Dizi içerisinde bir harf, birden fazla varsa sadece 1 defa yazdırılacaktır.
• Case-sensitive dikkat edilmelidir. Yani aynı harfin küçüğü (a) ve büyüğü (A) farklı karakter olarak değerlendirilmelidir.
• Bu sorudan tam puan almak için kullanıcı tarafından girilen karakter dizisini istenilen kriterlere göre çıktı şeklinde yazdırmalısınız. Aksi taktirde hiç puan alamazsınız.


## 1. Etap  - Soru 2

Her bir satırında bir sayı bulunan sıralı erişimli sayilar.txt dosyasından verileri okuyup, daha sonra her bir sayının rakamlarının toplamını bulup bu toplam değerini, rakamları toplanan sayıyla aynı sırada olacak şekilde toplamlar.txt dosyasına yazan program kodunu yazınız.

Örnek text dosyası ve program çıktısı:

![image](https://user-images.githubusercontent.com/50625747/120103499-89e98f00-c158-11eb-997b-0c89434b7173.png)

• 1. satırda: 10 → 1+0 = 1
• 2. satırda: 28 → 2+8=10 → 1+0=1
• 3. satırda: 99876 → 9+9+8+7+6=39 → 3+9=12 → 1+2=3
• 4. satırda: 2 → 2
• 5. satırda: 45 → 4+5= 9
• 6. satırda: 6697 → 6+6+9+7=28 → 2+8=10 → 1+0=1

#### Dikkat Edilmesi Gereken Noktalar:
• Toplam değeri bir rakam değil ise bu toplam değerinin de rakamları toplanıp yeni toplam değeri bulunmalıdır. Bu işlemler toplam değeri rakam oluncaya kadar devam etmelidir.
• Tüm toplam değerleri aralarında bir boşluk ile rakamları toplanan ilk sayı ile aynı sırada toplamlar.txt dosyasında yazılmalıdır.
• Kodunuz sadece bizim verdiğiniz dosyadaki sayılar için değil farklı input dosyaları içinde çalışıyor olmalıdır

## 1. Etap - Soru 3
İnput olarak oruntumatrisi.txt isimli dosya alınarak, dosyada bulunan matriste istenilen örüntünün (soldan sağa, yukarıdan aşağıya ve çapraz) indislerini ve sayısını bulan programı yazınız.

![image](https://user-images.githubusercontent.com/50625747/120103491-81915400-c158-11eb-8439-75e66051848b.png)

    Bu soruda çapraz şekilde aramayı sol üstten sağ alta inerek yapabilirsiniz denildi. Benim çözümüm buna uygun şekilde yapıldı.

Ekran Çıktısı → Örüntülerin bulunduğu indisler ve örüntü adedi yazdırılacaktır.

    • 1. bulunan örüntü: [00] [01] [02]
    • 2. bulunan örüntü: [13] [14] [15]
    • 3. bulunan örüntü: [04] [13] [22]
    • ……
    • 11.bulunan örüntü: [53] [64] [75]
    • Toplam örüntü adedi: 11

#### Dikkat Edilmesi Gereken Noktalar:
• Kodun başında istenilen örüntü kullanıcıdan alınmalıdır. (Örneğin: “Girmek istediğiniz örüntüyü yazınız: 1101” )
• Bir örüntüde yer alan eleman başka bir örüntünün elemanı da olabilir.
• Matristeki örüntüyü ararken soldan sağa, yukarıdan aşağıya ve çapraz şekilde arama yapmalısınız.
• Kodunuz sadece bizim verdiğiniz dosyadaki matris için değil farklı matrislerde istenilen örüntü için çalışıyor olmalıdır.
• Bu sorudan tam puan almak için örüntünün bulunduğu indisleri ve toplam örüntü adetinin eksiksiz bir şekilde çıktıda yazması gerekiyor.

## 1. Etap - Örnek İnputlar:
"etap1inputlar" klasörü içerisinde bulunuyor.

 - etap1inputlar/sayilar.txt
 - etap1inputlar/oruntumatrisi.txt

## 2. Etap Sorusu:

Kullanıcı tarafından iki sayı seçilecektir. (Bu sayılar programa input olarak girilmeyecektir, kullanıcı aklında tutacaktır)

Bu sayıların;

❖ Toplamı 200 ile 1998 arasında olmalıdır.

❖ Sayılar 3 basamaklı olmalıdır.

❖ Sayıların rakamları kendi içinde birbirinden farklı olmalıdır. (Örnek: 456,537 ikilisi gibi)

Sizden bir program yazmanızı ve yazdığınız program ile aklınızda tuttuğunuz bu 2 sayının tahmin yoluyla bulunması istenmektedir. Programa başta 100 puan verilecek ve her bir tahminde 100 puandan bir puan düşülerek son skor değeri de ekranda gösterilecektir.

• Öncelikle bu iki sayının toplamını programdan bulmasını istiyoruz. Bunun için program kullanıcıya bir sayı tahmininde bulunacaktır. Kullanıcı geri dönüş inputu olarak;

✓ 0 değerini girerse tahmin değerinin toplam değere eşit,

✓ 1 değerini girerse tahmin değerinin toplam değerden küçük olduğu,

✓ 2 değerini girerse tahmin değerinin toplam değerden büyük olduğu anlamına gelmektedir.


Örnek:

Kullanıcı aklından 123 ve 294 sayılarını tutsun. (Dikkat: İki sayıyı da oluşturan rakamlar o sayıda bir kez kullanılmıştır.)

Kullanıcının tuttuğu sayıların toplamı :417

Skor:100
Programın 1. Tahmini: :500
Kullanıcıdan Alınacak İnput: 2		// tahmin değeri, toplam değerden büyük

Skor:99
Programın 2. Tahmini: :385
Kullanıcıdan Alınacak İnput: 1		// tahmin değeri, toplam değerden küçük

…

Skor:91
Programın 9. Tahmini: 417
Kullanıcıdan Alınacak İnput :0		// tahmin değeri, toplam değere eşit

Program istediği kadar tahmin yapma hakkına sahiptir. Ancak her tahminde skorun bir azaldığı unutulmamalıdır. Skor, her adımda ekrana yazdırılmalıdır. 

• Sayıların toplamı program tarafından bulunduktan sonra bu sefer programdan başta aklımızda tuttuğumuz sayıları tahmin etmesini isteyeceğiz.

✓ Sayı tahmini sonucunda doğru rakam, doğru basamakta ise “+”,

✓ Sayı tahmini sonucunda sayının içinde bulunan rakam, yanlış basamakta ise “–“,

✓ Sayıda olmayan rakamlar için “ * ” işaretiyle programa input yaparak bilgilendirme yapmalıdır. 

NOT: Program sayılar arasına “,” karakteri ile birbirinden ayırmalıdır. Tahmin işlemi “KüçükSayı,BüyükSayı” formatında olacaktır.

Örnek: Kullanıcının tuttuğu sayılar:123,294

    Skor:91
    Programın 1. Tahmini: :52,265
    Kullanıcıdan Alınacak İnput :+*-,+**
    //1: Sayıda var ve doğru basamakta
    //5: Sayıda yok
    //2: Sayıda var ancak yanlış basamakta
    
    //2: Sayıda var ve doğru basamakta
    //6: Sayıda yok
    //5: Sayıda yok


    Skor:90
    Programın 2. Tahmini: 128,290
    Kullanıcıdan Alınacak İnput :++*,++*

    ...

    ...

    Skor:85
    Programın 7. Tahmini: 123,294
    Kullanıcıdan Alınacak İnput :+++,+++
    Sayılar Bulundu: 123,294
    Skor:85

DEĞERLENDİRME: BU SÜREÇ TARAFIMIZDAN GİRİLEN 3 SAYI ÇİFTİ İLE TEKRARLANIP ELDE EDİLEN SKORLARIN ARİTMETİK ORTALAMASI SİZİN 2. ETAP NOTUNUZ OLARAK BELİRLENECEKTİR. HERKESTE AYNI 3 SAYI ÇİFTİ KULLANILACAKTIR.

Yani algoritmanızı ne kadar iyi kurarsanız, programınız sayıları o kadar hızlı tahmin ederek en fazla puanı almanızı sağlar.
