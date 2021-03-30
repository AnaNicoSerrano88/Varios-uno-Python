import requests

api = 'http://production.42-q.com/mes-api/p2581dc1/units/'

serial_number = '8S5B20R07042ZZP287A04TX'

reque = requests.get(api + serial_number.upper() + '/history')
location = reque.json()['success']



if location == False:
    messagebox.showerror("ERROR SERIAL", "NUMERO SERIE NO CONTIENE INFORMACION EN SFDC")
    clean_serial_entry()

else:
                
    location = reque.json()['data']["serial"]['current_location']
    print(location)