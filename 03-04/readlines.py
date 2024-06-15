f = open("D:/Do_it_python/01/새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()