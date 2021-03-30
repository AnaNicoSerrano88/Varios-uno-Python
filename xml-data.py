import xml.etree.ElementTree as ET
from datetime import datetime

#tree = ET.parse('C:/Users/hectorgabriel_garcia/Downloads/AppXml/archivo.xml')
tree = ET.parse('C:/xmlCorona/20200825114917_K9173613964_1.xml')
root = tree.getroot()


#for child in root:
    #print(child.tag)

#print([elem.tag for elem in root.iter()])

#for elem in root.iter('SERIAL_NUMBER'):
    #print(elem)


for dato in root.findall("./RESULT_DATA/HEADER/TESTER/SERIAL_NUMBER"):
    print("SERIAL NUMBER TESTER: ", dato.text)

for dato in root.findall("./RESULT_DATA/HEADER/DUT/SERIAL_NUMBER"):
    print("SERIAL NUMBER DUT: ",dato.text)

for producto_code in root.findall("./RESULT_DATA/HEADER/DUT/PRODUCT_CODE"):
    print(producto_code.text)

for fecha_inicio in root.findall("./RESULT_DATA/TEST_START"):
    convertstring = str(fecha_inicio.text)
    year = int(convertstring[0:4])
    day = int(convertstring[4:6])
    month = int(convertstring[6:8])
    hora = int(convertstring[8:10])
    minuto = int(convertstring[10:12])
    segundo = int(convertstring[12:14])


fecha_hora = datetime(year,month,day, hora, minuto, segundo)
print(fecha_hora)

print("\n")
print("PUNTOS DE MEDICION STATUS: ")

nombre_medicion = []
for dato in root.findall("./RESULT_DATA/RESULTS/SEQUENCE/MEASUREMENT/NAME"):
    nombre_medicion.append(dato.text)
print (len(nombre_medicion))

status_prueba = []
for dato in root.findall("./RESULT_DATA/RESULTS/SEQUENCE/MEASUREMENT/STATUS"):
    status_prueba.append(dato.text)
    
resultados_prueba_attr = []
resultados_prueba = []
for dato in root.findall("./RESULT_DATA/RESULTS/SEQUENCE/MEASUREMENT/RESULT"):
    resultados_prueba.append(dato.attrib)
    resultados_prueba.append(dato.text)

puntos_medicion = {}
numero = 0
for data in nombre_medicion:
    puntos_medicion[data] = [status_prueba[numero], resultados_prueba[numero], resultados_prueba[numero]]
    numero = numero + 1

falla_test = list()
for medicion, status in puntos_medicion.items(): 
    #print(medicion,":",status[0])
    if (status[0] == "FAIL"):
        falla_test.append(medicion)
        #print(medicion,":",status[0])
        print(medicion,":",status)

print (len(falla_test))
'''
for medicion, status in puntos_medicion.items():
    print(medicion,":",status)
'''