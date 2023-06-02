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


def consuiltaProducto(nombreproducto):
    db, cursor = conexion()
    cursor.execute(f"""select * from producto where relacion ='{nombreproducto}';""")
    resultados = cursor.fetchall()
    cursor.close()
    db.close()
    return resultados

# if __name__ == '__main__':
#     resultados=consuiltaProducrto('power_drill')
#
#     for fila in resultados:
#         # Acceder a los valores de cada columna
#         print( fila[0])
#         print( fila[1])
    # print("se inicio")
    # insertar()