import os,subprocess,sys

if len(sys.argv) == 2:
    command = str(sys.argv[1])
else:
    print("Usage: system <command>")
    quit()

os.system(command)
