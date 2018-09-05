from DataBase import DB

class Comment (object):
    idUHU = None
    Descripcion = None
    Post_idPost = None

    def SetDescripcion(self, Descripcion):
        self.Descripcion = Descripcion

    def SetPost_idPost(self, Post_idPost):
        self.Post_idPost = Post_idPost

    def SetIdUHU(self, idUHU):
        self.idUHU = idUHU

    def Insert(self):
        DB().run("INSERT INTO `Comment` (Descripcion_Comment, Usuario_idUsuario, Post_idPost) VALUES ('%s', '%s', '%s')" % (self.Descripcion, self.Post_idPost, self.idUHU))

    def Delete(self):
        DB().run("DELETE FROM `Comment`")