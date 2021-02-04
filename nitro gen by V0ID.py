import time
import os
import random
from colored import fg, bg, attr


print('''%s███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝%s''' % (fg(126), attr(0))+ "%sby V0id%s" % (fg(79), attr(0)) )
time.sleep(0.5)
tip = input("what kind of codes do you want to generate (%sclassic%s/" % (fg(123), attr(0)) + "%sboost%s) " %(fg(207), attr(0)))
if tip != "classic":
    if tip != "boost":
        print("%sunknown code type%s" % (fg(1), attr(0)))
        time.sleep(1)
        exit(1)
time.sleep(0.5)
try:
    numar = int(input("how many nitro " + tip + " codes do you want to generate "))
except:
    print("%sN/A%s" % (fg(1), attr(0)))
    time.sleep(1)
    exit(1)
animation = "|/-\\"
idx = 0
t_end = time.time() + 5
while time.time() < t_end:
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)
if os.path.exists("nitro codes.txt"):
    os.remove("nitro codes.txt")
fisier = open("nitro codes.txt", "x")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
if tip == "classic":
    while numar > 0:
        codeLen = 16
        cod = ''.join(random.choice(letters) for i in range(codeLen))
        fisier.write("https://discord.gift/" + cod + "\n")
        print("%shttps://discord.gift/%s"% (fg(123), attr(0))+ cod)
        numar-=1
if tip == "boost":
    while numar > 0:
        codeLen = 24
        cod = ''.join(random.choice(letters) for i in range(codeLen))
        fisier.write("https://discord.gift/" + cod + "\n")
        print("%shttps://discord.gift/%s"% (fg(207), attr(0))+ cod)
        numar -= 1
print("%sSucces! Press enter to close the application!%s" % (fg(10), attr(0)))
input()