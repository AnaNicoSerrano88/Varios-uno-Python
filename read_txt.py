f = open("C:/Users/LENOVO-T480s-I5/Desktop/fichero.txt", "r")

while(True):
    linea = f.readline()
    print(linea)
    if not linea:
        break


f.close()