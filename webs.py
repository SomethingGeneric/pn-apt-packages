import sys,webbrowser

if len(sys.argv) == 2:
    term = str(sys.argv[1])
else:
    print("Usage: webs \"<term>\"")
    quit()

webbrowser.open("https://google.com/search?q="+term)
