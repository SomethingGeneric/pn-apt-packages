import os,subprocess,sys

if not os.path.exists("textart-reqs-installed"):
    subprocess.call([sys.executable,"-m","pip","install","art","colorama"])
    f = open("textart-reqs-installed",'w')
    f.write(".")
    f.close()

import art
from colorama import *
init()

if len(sys.argv) == 3:
    color = str(sys.argv[1])
    text = str(sys.argv[2])
else:
    print("Usage: textart <color> <text>")
    quit()

# RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

if color == "red":
    use = Fore.RED
elif color == "green":
    use = Fore.GREEN
elif color == "green":
    use = Fore.GREEN
elif color == "green":
    use = Fore.GREEN
elif color == "green":
    use = Fore.GREEN
elif color == "green":
    use = Fore.GREEN
elif color == "green":
    use = Fore.GREEN
else:
    print("Not a color. Using default.")
    use = Fore.RESET

print(use + text)
