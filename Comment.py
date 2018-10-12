from DataBase import DB
from Usuario import Usuario

class Comment (object):
    idComment = None
    Descripcion = None
    Post_idPost = None
    Usuario = None

    def SetDescripcion(self, Descripcion):
        self.Descripcion = Descripcion

    def SetPost_idPost(self, Post_idPost):
        self.Post_idPost = Post_idPost

    def SetUsuario(self, Usuario):
        self.Usuario = Usuario

    def AllSetsComments(self, Descripcion, Post_idPost, Usuario):
        self.SetDescripcion(Descripcion)
        self.SetPost_idPost(Post_idPost)
        self.SetUsuario(Usuario)

    def Insert(self):
        cursor = DB().run("INSERT INTO `Comment` (Descripcion_Comment, Usuario_idUsuario, Post_idPost) VALUES ('%s', '%s', '%s')" % (self.Descripcion, self.Usuario.idUsuario, self.Post_idPost))
        self.idPost = cursor.lastrowid

    def Delete(self):
        DB().run("DELETE FROM `Comment`")

    def ObjetizarIdUsuario(self):
        cursor = DB().run("SELECT * FROM Usuario WHERE idUsuario = ('%s')" % (self.Usuario))
        for item in cursor:
            unUsuario = Usuario()
            unUsuario.TraerObjeto(item["Nombre_Usuario"])
            self.SetUsuario(unUsuario)



    def TraerObjeto(self, idComment):
        Cursor = DB().run("SELECT * FROM Comment WHERE idComment = ('%s')" % (idComment))
        for item in Cursor:
            self.idComment = item["idComment"]
            self.Post_idPost = item["Post_idPost"]
            self.Usuario = item["Usuario_idUsuario"]
            self.Descripcion = item["Descripcion_Comment"]
            self.ObjetizarIdUsuario()
