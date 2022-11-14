## BİR FONKSİYONUN MAKSİMUM VE MİNİMUM NOKTALARINI BULMAK İÇİN NEDEN TÜREV KULLANIRIZ?
Bir fonksiyonun maksimum ve minimum noktalarını bulmak için neden türev kullanırız?

Merhaba, türev pek çok hesaplamada araç olarak kullanılır. Bu yazıda, “bir fonksiyonun maksimum ve minimum noktalarını bulmak için neden türev kullanırız?” sorusuna cevap arayacağız.

Peki öncelikle “Türev Nedir?” ile başlayalım.

Türev, bir şeyin bir diğer şeye göre değişim miktardır. Yani türev, değişimi ölçmek için kullanılır. Mesela alınan yolun zamana göre değişimi bize hızı verir. Aşağıdaki grafikte 50. Saniyedeki hızı bulmayı deneyelim.

![GitHub](https://raw.githubusercontent.com/aliyasir7/patika/main/Picture1.png)

Mavi eğride 50. Saniye bir noktaya karşılık gelir. Bu noktaya A diyelim. A’dan x ekseninde delta x kadar ilerlediğimizde B noktasına ulaşırız. Yine x ekseninde delta x kadar geri gittiğimizde C noktasına ulaşırız. Delta x sıfıra çok yakın bir değer olduğu için B ve C noktalarını birleştirdiğimizde mavi eğriye A noktasındaki teğet doğrusunu elde etmiş oluruz.

![GitHub](https://raw.githubusercontent.com/aliyasir7/patika/main/Picture2.png)

B noktası ile C noktası arasındaki x eksenindeki uzaklık 2 delta x iken, y eksenindeki uzaklık 2 delta y’dir. Yani zamanda 2 delta x’lik değişim olduğunda 2 delta y’lik yol almış oluruz. Böylelikle birim zamanda delta y / delta x kadar yol almış oluruz. Şekilde üçgenin uzun kenarı teğet doğrumuzun üzerinde olduğu için eğimleri eşittir. Üçgenin uzun kenarının eğimi delta Y/ delta x olduğu için teğetimizin eğimi de delta y/ delta x’dir. Böylece birim zamanda alınan yol yani hız teğet doğrumuzun eğimine eşit olur.

Türevi kullandığımız bir diğer nokta bir fonksiyonun maksimum veya minimum değerini bulma işlemleridir. Fonksiyonun türevinin 0’a eşit olduğu noktalarda bu fonksiyon ya maksimum ya da minimum değerini alır. Bu açıdan bakıldığında bu değeri bulmak çok kolay gibi gelebilir. Peki neden böyledir? Bir fonksiyonun maksimum / minimum değerleri neyi ifade ediyor?

![GitHub](https://raw.githubusercontent.com/aliyasir7/patika/main/Picture3.png)

Şekildeki dağları bir fonksiyon gibi düşünebiliriz. x1 noktasından bir grup dağcı x2 noktasına varmak için yola çıkmış olsun. Bu grup x3 noktasına varana kadar sürekli yükselme hızları değişse de yukarıya doğru tırmanırlar. Bu noktaya geldiklerinde tırmanmaları bir süreliğine durur ve aşağıya inmeye başlarlar. x4 noktasına gelene kadar bu aşağıya iniş devam eder. Burada gidiş yönünü değiştiren, inişleri çıkışlara, çıkışları inişlere çeviren noktalar fonksiyonun minimum ve maksimum noktalarıdır.

x3 noktasını düşünecek olursak, bu nokta çıkışın inişe döndüğü bir maksimum noktasıdır. Bu noktadan türevi yani değişimi ifade eden delta x kadar geriye ve delta x kadar ileriye gidersek aşağıdaki gibi D ve F noktalarına ulaşırız. Hız hesaplama örneğinde olduğu gibi delta x sıfıra çok yakın olduğu için D, x3 ve F noktalarından geçen doğru y ekseninde herhangi bir delta y değişimi göstermeyeceğinden x eksenine paraleldir. X eksenine paralel olan doğruların eğimi 0 olduğu için x3 noktasındaki teğet doğrusunun eğimi yani bu noktadaki türev 0’dır. Aynı yaklaşımlar dağcıların iniş ve çıkış yönlerinin değiştiği tüm noktalar için uygulanabildiği için x4 ve x5 noktalarının da türevi 0 olur.

Özetle bir fonksiyonun türevini sıfır yapan değerleri bulursak , bu noktalar bize o fonksiyonun maksimum ve minimum değerlerini vermiş olur.



