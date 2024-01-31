import os

os.system("clear")

def opcion1():
   print("")
   url = input("\033[1;35mIngrese la url [https://..]: \033[1;34m")
   os.system("sleep 2")
   print(f"\033[1;35m[Url camuflada]: \033[1;36mhttps://shop-links.co/link?publisher_slug=future&exclusive=1&u1=tomsguide-in-2620345246174741000&url={url}")
 
def opcion2():
   print("")
   url = input("\033[1;35mIngrese la url [https://..]: \033[1;34m")
   os.system("sleep 2")
   print(f"\033[1;35m[Url camuflada]: \033[1;36mhttps://www.digit.in/flipkart/intermediate?url={url}")

def opcion3():
   print("")
   url = input("\033[1;35mIngrese la url [https://..]: \033[1;34m")
   os.system("sleep 2")
   print(f"\033[1;35m[Url camuflada]: \033[1;36mhttps://www.anrdoezrs.net/click-6361382-15020510?url={url}")

def opcion4():
   print("")
   url = input("\033[1;35mIngrese la url [https://..]: \033[1;34m")
   os.system("sleep 2")
   print(f"\033[1;35m[Url camuflada]: \033[1;36mhttps://l.wl.co/l?u={url}")

print("\033[1;33m")
print(" ________________________________________")
print("|                                        |")
print("|                                        |")
print("|__  __           _    _     _       _   |")
print("\033[1;31m|  \/  | __ _ ___| | _| |   (_)_ __ | | _|")
print("\033[1;35m| |\/| |/ _` / __| |/ / |   | | '_ \| |/ /")
print("\033[1;34m| |  | | (_| \__ \   <| |___| | | | |   <")
print("\033[1;36m|_|  |_|\__,_|___/_|\_\_____|_|_| |_|_|\_\ ")
print("|                                        |")
print("|            Code by: Netxus             |")   
print("|________________________________________|")
print("")

while True:
 print("\033[1;36m[1]. \033[1;37mshop-link.co")
 print("\033[1;36m[2]. \033[1;37mdigit.in")
 print("\033[1;36m[3]. \033[1;37manrdoezrs.net")
 print("\033[1;36m[4]. \033[1;37ml.wl.co")
 sel = input("Opción: ")
 if sel == "1":
    opcion1()
    exit()                                            
 elif sel == "2":
    opcion2()
    exit()
 elif sel == "3":
    opcion3()
    exit()                                             
 elif sel == "4":
    opcion4()
    exit()
