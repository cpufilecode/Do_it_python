f = open("D:/Do_it_python/01/새파일.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()