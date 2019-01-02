import sys,os

if len(sys.argv) == 2:
    term = str(sys.argv[1])
else:
    print("Usage: pyrepl \"<code>\"")
    quit()

os.system(sys.executable + " -m " + term)
