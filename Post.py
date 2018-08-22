from DataBase import DB
import datetime


class Post (object):
    idPost = None
    Fecha_Creacion_Post = None
    Descripcion_Post = None
    Ubicacion_Post = None
    Usuario_idUsuario = None

    def SetFecha_Creacion (self):
        self.Fecha_Creacion_Post = datetime.date.today()

    def SetDescripcion_Post (self,Descripcion_Post):
        self.Descripcion_Post = Descripcion_Post

    def SetUbicacion(self,Ubicacion_Post):
        self.Ubicacion_Post = Ubicacion_Post

    def SetUsuario_idUsuario (self, Usuario_idUsuario):
        self.Usuario_idUsuario = Usuario_idUsuario

    def Insert(self):
        cursor = DB().run("INSERT INTO Post (Fecha_Creacion_Post, Descripcion_Post, Ubicacion_Post) VALUES ('%s', '%s', '%s')" % (self.Fecha_Creacion_Post, self.Descripcion_Post, self.Ubicacion_Post))
        self.idPost = cursor.lastrowid

    def Delete(self):
        DB().run("DELETE FROM Post WHERE idPost = ('%d')" % (self.idPost))

    def UpdateDescripcion(self, descri):
        self.SetDescripcion_Post(descri)
        DB.run("UPDATE Post SET Descripcion_Post = ('%s')" % (self.Descripcion_Post))

    def UpdateUbicacion(self, ubicacion):
        self.SetUbicacion(ubicacion)
        DB.run("UPDATE Post SET Ubicacion_Post = ('%s')" % (self.Ubicacion_Post))