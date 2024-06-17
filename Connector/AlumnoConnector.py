import pymysql
from PySide6.QtCore import Qt

class AlumnoConnector():
    def __init__(self):
        self.con = pymysql.connect(
            host = "localhost",
            user = "root", 
            password = "root",
            db = "ComedorConecta"
        )
        self.cursor = self.con.cursor()
        
    def insertar(self, numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre):
        sql = "insert into alumno (numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre) values (%s, %s, %s, %s, %s, %s, %s)".format(numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre)
        self.con.cursor().execute(sql, (numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre))
        self.con.commit()
       
    def devuelveTodos(self):
        try:
            sql = "SELECT numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre FROM alumno"
            self.cursor.execute(sql)
            alumnos = self.cursor.fetchall()
            return alumnos
        except Exception as e:
            print(f"Error al obtener alumnos: {str(e)}")
            return []
    
    def devuelvePorNumero(self, numero):
        try:
            sql = "SELECT numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre FROM alumno where numero = %s".format(numero)
            self.cursor.execute(sql, (numero))
            alumno = self.cursor.fetchone()
            return alumno
        except Exception as e:
            print(f"Error al obtener el alumno: {str(e)}")
    
    def actualizarAlumno(self, numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre):
        sql = "update alumno set primerApellido = %s, segundoApellido = %s, curso = %s, ensenanza = %s, grupo = %s, nombre = %s where numero = %s".format(primerApellido, segundoApellido, curso, ensenanza, grupo, nombre, numero)
        self.cursor.execute(sql, (primerApellido, segundoApellido, curso, ensenanza, grupo, nombre, numero))
        self.con.commit()

    def eliminar_alumnos_seleccionados(self, numeros):
        if not numeros:
            print("No se han seleccionado alumnos para eliminar.")
            return

        try:
            placeholders = ', '.join(['%s'] * len(numeros))
            sql = f"DELETE FROM alumno WHERE numero IN ({placeholders})"
            
            connection = pymysql.connect(host='localhost', user='root', password='root', db='ComedorConecta')
            cursor = connection.cursor()
            cursor.execute(sql, numeros)
            connection.commit()
            print(f"Se han eliminado {cursor.rowcount} alumnos.")
        except Exception as e:
            print(f"Error al eliminar alumnos: {str(e)}")
        finally:
            cursor.close()
            connection.close()
    
    def devuelvePorCurso(self, curso):
        try:
            sql = "SELECT numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre FROM alumno WHERE curso = %s"
            self.cursor.execute(sql, (curso,))
            alumnos = self.cursor.fetchall()
            return alumnos
        except Exception as e:
            print(f"Error al obtener los alumnos del curso: {str(e)}")
            return []

    def actualizaNombrePadre(self, nuevo_nombre_padre, numero):
        try:
            nombre = str(nuevo_nombre_padre)
            num_alumno = str(numero)
            sql = "UPDATE madre SET nombre = %s WHERE num_hijo = %s"
            self.cursor.execute(sql, (nombre, num_alumno))
            self.con.commit()
            return True
        except Exception as e:
            print(f"Error actualizando nombre del padre: {e}")
            return False
    
    def devuelvePadrePorNumeroHijo(self, numero):
        try:
            sql = "SELECT id, nombre, num_hijo, email, direccion FROM madre WHERE num_hijo = %s".format(numero)
            self.cursor.execute(sql, (numero))
            madre = self.cursor.fetchone()
            return madre
        except Exception as e:
            print(f"Error al obtener las madres del curso: {str(e)}")
            return None

    def importarAlumnos(self, alumnos):
        for alumno in alumnos:
            try:
                self.cursor.execute("""
                    INSERT INTO alumno (numero, primerApellido, segundoApellido, curso, ensenanza, grupo, nombre)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    alumno['numero'],
                    alumno['primer_apellido'],
                    alumno['segundo_apellido'],
                    alumno['curso'],
                    alumno['ensenanza'],
                    alumno['grupo'],
                    alumno['nombre']
                ))
                self.con.commit()
            except Exception as err:
                print("Error al insertar el alumno:", err)

        self.cursor.close()
        self.con.close()
