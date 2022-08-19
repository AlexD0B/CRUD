from asyncore import read
import sqlite3
from turtle import update
from venv import create
def comprueba_numeros(variable):
    numeros = "1234567890"
    contador = 0
    for i in numeros:
        if i in variable:
            contador += 1

    if contador > 0:
        return True
    else:
        return False       


def comprueba_caracter(variable2):
    caracteres =  "!@#$%^&*()_+-=|}{↓∟←→♀[]\:';<>?,./︵︶"
    contador = 0
    for i in caracteres:
        if i in variable2:
            contador += 1

    if contador > 0:
        return True
    else:
        return False


def comprueba_letra(variable3):
    letras =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    contador = 0
    for i in letras:
        if i in variable3:
            contador += 1

    if contador > 0:
        return True
    else:
        return False


def comprueba_correo(variable4):
    direcion_correo =  "@.com"
    contador = 0
    for i in direcion_correo:
        if i in variable4:
            contador += 1

    if contador > 1:
        return True
    else:
        return False

db = sqlite3.connect('base_de_datos.db')

try:        
    cur = db.cursor()
    cur.execute('''CREATE TABLE datos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT (20) NOT NULL,
    name2 TEXT (20) NOT NULL,
    apellido TEXT (20) NOT NULL,
    apellido2 TEXT (20) NOT NULL,
    cedula INTEGER,
    telefono INTEGER,
    correo TEXT NOT NULL,
    edad INTEGER);''')
    print ('table created successfully')
except:
    print ('error in operation')
    db.rollback()


def create():
    qry="insert into datos (name,name2,apellido,apellido2,cedula,telefono,correo,edad) values(?,?,?,?,?,?,?,?);"
    try:
        name = input("Escribe tú primer nombre: ").title()
        if len(name) >= 3 and len(name) <= 20:
            if comprueba_numeros(name):
                print("los nombres no llevan numeros")
            else:
                if comprueba_caracter(name):
                    print("Los nombres no llevan caracteres especiales")    
                else:
                    print("nombre valido")      
        else:
            print("El nombre debe llevar minimo 3 caracteres, maximo 20")  
            pass     
        name2 = input("Escribe tú segundo nombre: ").title()
        if len(name2) >= 3 and len(name2) <= 20:
            if comprueba_numeros(name2):
                print("los nombres no llevan numeros")
            else:
                if comprueba_caracter(name2):
                    print("Los nombres no llevan caracteres especiales")    
                else:
                    print("nombre valido")      
        else:
            print("El nombre debe llevar minimo 3 caracteres, maximo 20")  
            pass   
        apellido = input("Escribe tú primer apellido: ").title()
        if len(apellido) >= 3 and len(apellido) <= 20:
            if comprueba_numeros(apellido):
                print("los apellidos no llevan numeros")
            else:
                if comprueba_caracter(apellido):
                    print("Los apellidos no llevan caracteres especiales")    
                else:
                    print("nombre valido")      
        else:
            print("El apellido debe llevar minimo 3 caracteres, maximo 20")  
            pass
        apellido2 = input("Escribe tú segundo apellido: ").title()
        if len(apellido2) >= 3 and len(apellido2) <= 20:
            if comprueba_numeros(apellido2):
                print("los apellidos no llevan numeros")
            else:
                if comprueba_caracter(apellido2):
                    print("Los apellidos no llevan caracteres especiales")    
                else:
                    print("nombre valido")      
        else:
            print("El apellido debe llevar minimo 3 caracteres, maximo 20")  
            pass
        cedula = (input("Introduce tu numero de cedula: "))
        if comprueba_letra(cedula):
            print("Las cedulas no llevan letras")
        else:
            if comprueba_caracter(cedula):
                print("Las cedulas no llevan caracteres especiales")
            else:
                print("Cedula valida")
        telefono = input("Escribe un numero de telefono: ")
        if len(telefono) == 11:
            if telefono.isnumeric():
                if "0412" in telefono or "0414" in telefono or "0416" in telefono or "0424" or "0426" in telefono:
                    print("Telefono valido")                           
        else:
            print("El numero debe de tener 11 digitos")
        correo = input("Coloca tu correo electronico: ")
        if len(correo) >= 6 and len(correo) <= 30:
            print("Correo valido")
        else:
            print("El correo debe debe llevar minimo 6 caracteres, maximo 30 y terminar en '@.com' ")      
        edad = int(input("edad: "))
        cur=db.cursor()
        cur.execute(qry, (name,name2,apellido,apellido2,cedula,telefono,correo,edad))
        db.commit()
        print ("one record added successfully")
    except:
        print ("error in operation")
    db.rollback()
    

def read():
    sql="SELECT * from datos;"
    cur=db.cursor()
    cur.execute(sql)
    while True:
        record=cur.fetchone()
        if record==None:
            break
        print (record)
    

def update():
    qry="update datos set edad=? where name=?;"
    try:
        edad = int(input("Introduce la edad a actualizar: "))
        name = input("El nombre de la persona: ").title()
        cur = db.cursor()
        cur.execute(qry, (edad,name))
        db.commit()
        print("record updated successfully")
    except:
        print("error in operation")
    db.rollback()
    
def delete():
    qry="DELETE from datos where name=?;"
    try:
        name = input("nombre de la persona a eliminar: ").title()
        cur=db.cursor()
        cur.execute(qry, (name,))
        db.commit()
        print("record deleted successfully")
    except:
        print("error in operation")
    db.rollback()
    

def menu():
    eleccion = 0

    while eleccion != 6:

        eleccion = int(input('introduzca un numero del 1-5 para realizar las siguientes acciones\n-presione 1 para añadir un usuario\n-presione 2 para mostrar todos los usuarios\n-presione 3 para actualizar un usuario\n-presione 4 para eliminar un usuario\n-presione 5 para salir del programa\n-eleccion: '))

        if eleccion == 1:
            create()
      
        elif eleccion == 2:
            read()

        elif eleccion == 3:
            update()

        elif eleccion == 4:
            delete()
        elif eleccion == 5:
            break
        else:
            print('la opcion no esta disponible')

menu()
