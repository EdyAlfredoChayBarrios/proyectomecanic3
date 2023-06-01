import mysql.connector

def conexion():
    db= mysql.connector.connect(
        host='localhost',
        port='2526',
        user='mecanico',
        password='1234',
        database = 'mecanic3'
    )
    cursor = db.cursor()
    return db, cursor


def insertar(nombre,idChat):
    db, cursor = conexion()
    cursor.execute(f"""INSERT INTO `mecanic3`.`cliente` (`nombreCompleto`,`chatId`) VALUES ('{nombre}','{idChat}');""")
    db.commit()
    db.close()

#
# if __name__ == '__main__':
#     print("se inicio")
#     insertar()