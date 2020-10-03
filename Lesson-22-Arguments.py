import sys

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?" :
        print("Help Requested")
        print("Usage of the program is python.exe myfile.py argv1 argv2 ")
    print("Arguments enterend^]:" + (sys.argv[1:]))
else:
    print("Arguments NOT PROVIDED")

os.system("dir > test.txt")
os.mkdir("my dir")
sys.exit(2)