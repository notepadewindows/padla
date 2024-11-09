import random
from distutils.command.clean import clean
from random import randint




class stats:
   def __init__(self):
       self.hp = 100
       self.money = 20
       self.attack = 2


your_hero = stats()
sg = 0
battle = 0
finish = 0
class enemy:
   def __init__(self):
       self.hp = 20
       self.attak = 3
ratt = enemy()
start = input("Магазин(N), Печера(P)")


if start == "N":
   vubir2 = input("Сапоги Гермеса:20(S), Вихід(B)")
   if vubir2 == "S":
       if your_hero.money >= 20:
           print("Дякую за покупку!")
           your_hero.hp +=20
           your_hero.money-=20
           sg = 1
           start = clean
       elif your_hero.money <20:
           print("Ти бомж")
           start = clean
       elif sg == 1:
           print("це вже є")
           start = clean
print("Життя:", your_hero.hp, "Монети:", your_hero.money, "Атака:", your_hero.attack)


if start == "P":
   print("ви знайшли крису")
   while True :
       battle = input("атака(A), убігти(R)")
       if battle == "A":
           print("Життя:", your_hero.hp, "Монети:", your_hero.money, "Атака:", your_hero.attack)
           print("Життя боса:", ratt.hp)
           hod =randint(1,2)
           if hod == 1:
               ratt.hp -= your_hero.attack
               if ratt.hp <=0:
                   print("ви перемогли")
                   your_hero.money += 20
                   break
           else:
                your_hero.hp -= ratt.attak
                if your_hero.hp <= 0:
                    print("ти програв")
                    break
print("Життя:", your_hero.hp, "Монети:", your_hero.money, "Атака:", your_hero.attack)
print("Життя боса:", ratt.hp)