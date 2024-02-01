import requests
import os

os.system("clear")

def opcion1():
   print("")
   url = input("\033[1;36mIngrese la url [https://..]: \033[1;34m")
   os.system("sleep 2")
   print(f"\033[1;32m[Url camuflada]: https://shop-links.co/link?publisher_slug=future&exclusive=1&u1=tomsguide-in-2620345246174741000&url={url}")
   print("")
   endpoint = f'http://tinyurl.com/api-create.php?url={url}'
   response = requests.get(endpoint)
   shortened_url_tinyurl = response.text
   print('[Url acortada] :', shortened_url_tinyurl)    

def opcion2():
   print("")
   url = input("\033[1;36mIngrese la url [https://..]: \033[1;34m")
   os.system("sleep 2")
   print(f"\033[1;32m[Url camuflada]: https://www.digit.in/flipkart/intermediate?url={url}")
   print("")
   endpoint = f'http://tinyurl.com/api-create.php?url={url}'
   response = requests.get(endpoint)
   shortened_url_tinyurl = response.text
   print('[Url acortada] :', shortened_url_tinyurl)

def opcion3():
   print("")
   url = input("\033[1;36mIngrese la url [https://..]: \033[1;34m")
   os.system("sleep 2")
   print(f"\033[1;32m[Url camuflada]: https://www.anrdoezrs.net/click-6361382-15020510?url={url}")
   print("")
   endpoint = f'http://tinyurl.com/api-create.php?url={url}'
   response = requests.get(endpoint)
   shortened_url_tinyurl = response.text
   print('[Url acortada] :', shortened_url_tinyurl)

def opcion4():
   print("")
   url = input("\033[1;36mIngrese la url [https://..]: \033[1;34m")
   os.system("sleep 2")
   print(f"\033[1;32m[Url camuflada]: https://l.wl.co/l?u={url}")
   print("")
   endpoint = f'http://tinyurl.com/api-create.php?url={url}'
   response = requests.get(endpoint)
   shortened_url_tinyurl = response.text
   print('[Url acortada] :', shortened_url_tinyurl)

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
print("|       -[Camuflador y Acortador]-       |")   
print("|________________________________________|")
print("")

while True:
 print("\033[1;36m[1]. \033[1;37mshop-link.co")
 print("\033[1;36m[2]. \033[1;37mdigit.in")
 print("\033[1;36m[3]. \033[1;37manrdoezrs.net")
 print("\033[1;36m[4]. \033[1;37ml.wl.co")
 print("\033[1;36m[0]. \033[1;37mSalir")
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
 elif sel == "0":
    exit()
 else:
    print("\033[1;31m[x]Opcion invalida")
    exit("")
