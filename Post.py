from DataBase import DB
import datetime


class Post (object):
    idPost = None
    Fecha_Creacion_Post = None
    Descripcion_Post = None
    Ubicacion_Post = None
    Usuario_idUsuario = None
    URL_post = None
    NumeroDeLikes = 0


    ## --------SubirFotos-----------

    def SetUsuario_idUsuario (self, Usuario_idUsuario):
        self.Usuario_idUsuario = Usuario_idUsuario

    def SetFecha_Creacion (self):
        self.Fecha_Creacion_Post = datetime.date.today()

    def SetDescripcion_Post (self,Descripcion_Post):
        self.Descripcion_Post = Descripcion_Post

    def SetUbicacion(self,Ubicacion_Post):
        self.Ubicacion_Post = Ubicacion_Post

    def SetURL (self, URL_post):
        self.URL_post = URL_post

    def Insert(self):
        cursor = DB().run("INSERT INTO Post (Fecha_Creacion_Post, Descripcion_Post, Ubicacion_Post, ""Usuario_idUsuario,URL_Post) VALUES ('%s', '%s', '%s', '%s', '%s')" % (self.Fecha_Creacion_Post, self.Descripcion_Post, self.Ubicacion_Post, self.Usuario_idUsuario, self.URL_post))
        self.idPost = cursor.lastrowid

    def SubirFoto(self, idUsuario, URL_Imagen, Descripcion, Ubicacion):
        self.SetUsuario_idUsuario(idUsuario)
        self.SetFecha_Creacion()
        self.SetDescripcion_Post(Descripcion)
        self.SetUbicacion(Ubicacion)
        self.SetURL(URL_Imagen)
        self.Insert()

    ## --------Updates&Deletes-------------

    def Delete(self,id):
        DB().run("DELETE FROM Post WHERE idPost = ('%d')" % (id))

    def UpdateDescripcion(self, descri):
        self.SetDescripcion_Post(descri)
        DB().run("UPDATE Post SET Descripcion_Post = ('%s')" % (self.Descripcion_Post))

    def UpdateUbicacion(self, ubicacion):
        self.SetUbicacion(ubicacion)
        DB().run("UPDATE Post SET Ubicacion_Post = ('%s')" % (self.Ubicacion_Post))

    # -------------Utilities--------------

    def TraerObjeto(self, idPost):
        Cursor = DB().run("SELECT * FROM Post WHERE idPost = ('%s')" % (idPost))
        for item in Cursor:
            self.idPost = item["idPost"]
            self.Fecha_Creacion_Post = item["Fecha_Creacion_Post"]
            self.Descripcion_Post = item["Descripcion_Post"]
            self.Ubicacion_Post = item["Ubicacion_Post"]
            self.Usuario_idUsuario = item["Usuario_idUsuario"]
            self.URL_post = item["URL_Post"]

    def NombreVisibleUsuario(self):
        NombrePene = DB().run("SELECT Nombrevisible_Usuario FROM Usuario WHERE idUsuario = ('%s')" % (self.Usuario_idUsuario))
        for item in NombrePene:
            NombrePenesito = item["Nombrevisible_Usuario"]
        return NombrePenesito

    def Contador(self):
        cursor = DB().run("SELECT COUNT(*) as H FROM `Like` WHERE ('%s')=Post_idPost" % (self.idPost))
        Contadores = cursor.fetchone()
        self.NumeroDeLikes = Contadores["H"]