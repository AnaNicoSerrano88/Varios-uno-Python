import sqlite3

db = "timerSIAT.db"

def crear_bd():
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla de Categorías ya existe.")
    else:
        print("La tabla de Categorías se ha creado correctamente.")

    try:
        cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabla de Platos ya existe.")
    else:
        print("La tabla de Platos se ha creado correctamente.")

    conexion.close()


def agregar_categoria():
    categoria = input("¿Nombre de la nueva categoría?\n> ")

    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()

    try:
        cursor.execute(f"INSERT INTO categoria VALUES (null, '{categoria}')")
    except sqlite3.IntegrityError:
        print(f"La categoría '{categoria}' ya existe.")
    else:
        print(f"Categoría '{categoria}' creada correctamente.")

    conexion.commit()
    conexion.close()


def agregar_plato():

    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoría para añadir el plato:")
    for categoria in categorias:
        print(f"[{categoria[0]}] {categoria[1]}")

    categoria_usuario = int(input("> "))

    plato = input("¿Nombre del nuevo plato?\n> ")

    try:
        cursor.execute(f"INSERT INTO plato VALUES (null, '{plato}', {categoria_usuario})")
    except sqlite3.IntegrityError:
        print(f"El plato '{plato}' ya existe.")
    else:
        print(f"Plato '{plato}' creado correctamente.")

    conexion.commit()
    conexion.close()


def mostrar_menu():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()  

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()   
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute(f"SELECT * FROM plato WHERE categoria_id={categoria[0]}").fetchall()
        for plato in platos:
            print(f"\t{plato[1]}")

    conexion.close()


# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion = input(
        "\nIntroduce una opción:" \
        "\n[1] Agregar una categoría" \
        "\n[2] Agregar un plato" \
        "\n[3] Mostrar el menú" \
        "\n[4] Salir del programa\n\n> ")

    if opcion == "1":
        agregar_categoria()

    elif opcion == "2":
        agregar_plato()

    elif opcion == "3":
        mostrar_menu()

    elif opcion == "4":
        print("Nos vemos!")
        break

    else:
        print("Opción incorrecta")