"""
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile 
buldurmaya çalışın.
** "random modülü" için "python random" şeklinde arama yapın.
*** 100 üzerinden puanlama yapın. Her soru 20 puan.
**** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
     ürzerinden hesaplansın.
"""

import random

can = 1
sayi = 0
tahmin = 0
deneme=0
sayi = random.randint(0,100)
can = int(input("Kaç can istersin :) : "))
while 0>can or can>20:
      can = int(input("Kaç can istersin (0-20 arasında) : "))
else:
      print("--------- \nPeki, hadi başlayalım")
      while can > 0:
            print(f"Kalan can: {can}")
            tahmin = int(input("Tahmini Alayım : "))
            deneme += 1
            if tahmin == sayi:
                  print(f"Tebrikler! {deneme}. denemede bildin")
                  break
            else:
                  can -= 1
            if sayi - tahmin > 0:
                  print(" \nYukarı\n ")
            elif sayi - tahmin < 0:
                  print(" \nAşağı\n ")
      else:
            print(f"Can hakkın bitti kank \nSayı {sayi}'di")