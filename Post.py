from DataBase import DB
import datetime


class Post (object):
    idPost = None
    Imagen = None
    Fecha_Creacion_Post = None
    Descripcion_Post = None
    Ubicacion_Post = None
    Usuario_idUsuario = None


    ## --------SubirFotos-----------

    def SetUsuario_idUsuario (self, Usuario_idUsuario):
        self.Usuario_idUsuario = Usuario_idUsuario

    def SetImagen(self, URLImagen):
        self.Imagen = URLImagen

    def SetFecha_Creacion (self):
        self.Fecha_Creacion_Post = datetime.date.today()

    def SetDescripcion_Post (self,Descripcion_Post):
        self.Descripcion_Post = Descripcion_Post

    def SetUbicacion(self,Ubicacion_Post):
        self.Ubicacion_Post = Ubicacion_Post

    def Insert(self):
        cursor = DB().run("INSERT INTO Post (Fecha_Creacion_Post, Descripcion_Post, Ubicacion_Post) VALUES ('%s', '%s', '%s')" % (self.Fecha_Creacion_Post, self.Descripcion_Post, self.Ubicacion_Post))
        self.idPost = cursor.lastrowid

    def SubirFoto(self, idUsuario, URL_Imagen, Descripcion, Ubicacion):
        self.SetUsuario_idUsuario(idUsuario)
        self.SetImagen(URL_Imagen)
        self.SetFecha_Creacion()
        self.SetDescripcion_Post(Descripcion)
        self.SetUbicacion(Ubicacion)
        self.Insert()

    ## --------Updates&Deletes-------------

    def Delete(self):
        DB().run("DELETE FROM Post WHERE idPost = ('%d')" % (self.idPost))

    def UpdateDescripcion(self, descri):
        self.SetDescripcion_Post(descri)
        DB.run("UPDATE Post SET Descripcion_Post = ('%s')" % (self.Descripcion_Post))

    def UpdateUbicacion(self, ubicacion):
        self.SetUbicacion(ubicacion)
        DB.run("UPDATE Post SET Ubicacion_Post = ('%s')" % (self.Ubicacion_Post))