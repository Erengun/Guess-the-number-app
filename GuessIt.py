import random
can = 1
sayi = 0
tahmin = 0
deneme=0
play=1

while play==1:
      Lang = int(input("Choose Languge: \nPress 1 for English. \nPress 2 for Turkish\n:"))
      while 0> Lang or Lang>2:
            Lang = int(input("You Entered a wrong value please try again :"))
      if Lang==2:
            
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
                        play=int(input("Tekrar oynamak için 1'e basın."))
      elif Lang ==1:
            sayi = random.randint(0,100)
            can = int(input("How many lives do you want? : "))
            while 0>can or can>20:
                  can = int(input("It must be between 0-20 : "))
            else:
                  print("--------- \nOkay, Let's Start")
                  while can > 0:
                        print(f"Hearths Left: {can}")
                        tahmin = int(input("Guess the Number : "))
                        deneme += 1
                        if tahmin == sayi:
                              print(f"Congratulations! You find the number at {deneme}. try. ")
                              break
                        else:
                              can -= 1
                        if sayi - tahmin > 0:
                              print(" \nUp\n ")
                        elif sayi - tahmin < 0:
                              print(" \nDown\n ")
                  else:
                        print(f"Your hearts are over. \nThe number was {sayi}")
                        play=int(input("Press 1 for start a new game:"))
            
