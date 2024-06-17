import pymysql

class ConnectorUsuarios():
    def __init__(self):
        self.con = pymysql.connect(
            host = "localhost",
            user = "root", 
            password = "root",
            db = "ComedorConecta"
        )
        self.cursor = self.con.cursor()
        
    def insertar(self, username, email, passwd, centro, telefono):
        sql = "insert into users (username, email, passwd, centro, telefono) values (%s, %s, %s, %s, %s)".format(username, email, 
                passwd, centro, telefono)
        self.con.cursor().execute(sql, (username, email, passwd, centro, telefono))
        self.con.commit()
       
    def devuelveTodos(self):
        try:
            sql = "SELECT id, username, email, passwd, centro, telefono FROM users"
            self.cursor.execute(sql)
            usuarios = self.cursor.fetchall()
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {str(e)}")
            return []
    
    def devuelvePorID(self, id):
        try:
            sql = "SELECT username, email, passwd, centro, telefono FROM users where id = %s".format(id)
            self.cursor.execute(sql, (id))
            usuario = self.cursor.fetchone()
            return usuario
        except Exception as e:
            print(f"Error al obtener usuario: {str(e)}")
    
    def actualizarUsuario(self, id, username, email, centro, telefono):
        sql = "update users set username = %s, email = %s, centro = %s, telefono = %s where id = %s".format(username, email, 
                centro, telefono, id)
        self.cursor.execute(sql, (username, email, centro, telefono, id))
        self.con.commit()
    
    def borrarUsuario(self, id):
        sql = "delete from users where id = %s".format(id)
        self.cursor.execute(sql, (id))
        self.con.commit()
        
    def devuelvePorUsuario(self, identificador):
        try:
            sql = "SELECT * FROM users WHERE username = %s"
            self.cursor.execute(sql, (identificador,))
            usuario = self.cursor.fetchone()
            
            return usuario
        except Exception as e:
            print(f"Error al obtener usuario: {str(e)}")
            return None
    
    def devuelvePorCorreo(self, correo):
        try:
            sql = "SELECT * FROM users WHERE email = %s"
            self.cursor.execute(sql, (correo,))
            usuario = self.cursor.fetchone()
            
            return usuario
        except Exception as e:
            print(f"Error al obtener usuario: {str(e)}")
            return None
        
    def cambiaContrasena(self, contrasena_nueva, email):
        try:
            sql = "UPDATE users SET passwd = %s WHERE email = %s".format(contrasena_nueva, email)
            self.cursor.execute(sql, (contrasena_nueva, email,))
            self.con.commit()
        except Exception as e:
            print(f'Error al cambiar la contraseña: {str(e)}')
            return None