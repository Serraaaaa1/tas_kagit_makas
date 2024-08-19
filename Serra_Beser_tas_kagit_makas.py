Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import random
#Seçim ve puan ekleme fonksiyonu
def tas_kagit_makas():
    global bilgisayar, oyuncu, oyun_devam
    
    # Bilgisayarın rastgele seçimi
    bilgisayar_girdisi = random.choice(seçenekler)
    
    kullanıcı_girdisi = input("Taş, Kağıt veya Makas seçiniz: ").lower()
    
    # Geçerli bir seçim yapılmadıysa tekrar girdi iste
    while kullanıcı_girdisi not in seçenekler:
        print("Geçersiz seçim! Lütfen taş, kağıt veya makas giriniz.")
        kullanıcı_girdisi = input("Taş, Kağıt veya Makas seçiniz: ").lower()
    
    print("Bilgisayarın seçimi: "+ str(bilgisayar_girdisi)+ "  Sizin seçiminiz: " + str(kullanıcı_girdisi))
    
    if bilgisayar_girdisi == 'taş' and kullanıcı_girdisi == 'kağıt':
        oyuncu += 1
    elif bilgisayar_girdisi == kullanıcı_girdisi:
        print('Berabere kaldınız.')
    elif bilgisayar_girdisi == 'kağıt' and kullanıcı_girdisi == 'taş':
        bilgisayar += 1
    elif bilgisayar_girdisi == 'kağıt' and kullanıcı_girdisi == 'makas':
        oyuncu += 1
    elif bilgisayar_girdisi == 'taş' and kullanıcı_girdisi == 'makas':
        bilgisayar += 1
    elif bilgisayar_girdisi == 'makas' and kullanıcı_girdisi == 'taş':
        oyuncu += 1
    elif bilgisayar_girdisi == 'makas' and kullanıcı_girdisi == 'kağıt':
        bilgisayar += 1
    
    print("Skor: Bilgisayar " + str(bilgisayar) + "-" +str(oyuncu) +" Siz\n")
#Oyunun fonksiyonu
def tas_kagit_makas_SERRA_BESER():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz! Oyunda size taş, kağıt ve makastan oluşan üç seçenek verilecektir.\nSizinle aynı anda bilgisayar da seçeneklerden birini seçecektir")
    print("Taş makasa karşı kazanırken kağıda karşı yenilmektedir. Makas ise kağıda karşı kazanır.")
    print("Oyunu kazanmak için 2 kere bilgisayara karşı kazanmalısınız. Aynı seçeneği seçerseniz berabere kalırsınız ve puan alamazsınız.")
    print("Her turun sonunda size ve bilgisayara devam etmek isteyip istemediğiniz sorulacaktır. Eğer devam etmek istemezseniz oyun bitecektir.")

    global bilgisayar, oyuncu, seçenekler, seçenekler_2, oyun_devam

    bilgisayar = 0
...     oyuncu = 0
... 
...     seçenekler = ['taş', 'kağıt', 'makas']
...     seçenekler_2 = ['evet', 'hayır']
... 
...     # Oyun devam ediyor mu durumu
...     oyun_devam = True
...     
...     while bilgisayar < 2 and oyuncu < 2 and oyun_devam:
...         tas_kagit_makas()  # Seçim fonksiyonunu burada çağırıyoruz
... 
...         # Eğer biri 2 galibiyete ulaştıysa oyunu sonlandır
...         if bilgisayar == 2 or oyuncu == 2:
...             oyun_devam = False
...             break  # Döngüden çıkış yapıldı
...         
...         while True:
...             kullanıcı_cevabı = input("Oyuna devam etmek ister misiniz? (evet/hayır): ").lower()
...             if kullanıcı_cevabı in seçenekler_2:
...                 break
...             print("Geçersiz seçim! Lütfen evet veya hayır giriniz.")
...         
...         bilgisayar_cevabı = random.choice(seçenekler_2)
...         print("Bilgisayar oyuna devam etmek ister mi?:  " + str(bilgisayar_cevabı))
...         
...         if bilgisayar_cevabı == "evet" and kullanıcı_cevabı == "evet":
...             print("Oyuna devam ediyorsunuz.")
...         else:
...             print("Oyuna devam etmek istemediniz.")
...             oyun_devam = False  # Oyun bitti
... 
...     if bilgisayar == 2:
...         print("Bilgisayar 2 kez kazandı. Oyun bitti.")
...     elif oyuncu == 2:
...         print("Siz 2 kez kazandınız. Oyun bitti.")
...     else:
...         print("Oyun erken sonlandırıldı.")
