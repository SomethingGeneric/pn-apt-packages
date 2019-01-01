import sys,shutil

from oslib import hostmgr

h = hostmgr()

if len(sys.argv) == 2:
    source = str(sys.argv[1])
else:
    print("Usage: sideload \"<source>\"")
    quit()

sp = source + ".src"
shutil.copyfile(sp,"bin"+h.get()+source+".py")
