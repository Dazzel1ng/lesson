from Hero import *

myhero = Hero("Nikita", 5 , "Human")
mysuperhero = Hero("Saha", 3, "Human", 1)

myhero.show_hero()
mysuperhero.show_hero()

mysuperhero.makemagic()
mysuperhero.show_hero()


mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.show_hero()

mysuperhero.magic = 10
mysuperhero.show_hero()
