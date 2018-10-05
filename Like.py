from DataBase import DB

class Like(object):
    Usuario_idUsuario = None
    Post_idPost = None

    def SetPost_idPost(self, Post_IdPost):
        self.Post_idPost = Post_IdPost

    def SetUsuario_idUsuario(self, Usuario_idUsuario):
        self.Usuario_idUsuario = Usuario_idUsuario

    def AllSets(self, idPost, idUsuario):
        self.SetPost_idPost(idPost)
        self.SetUsuario_idUsuario(idUsuario)

    def Insert(self):
        DB().run("INSERT INTO `Like` (Usuario_idUsuario, Post_idPost) VALUES (%s, %s)" % (self.Usuario_idUsuario, self.Post_idPost))

    def Delete(self):
        DB().run("DELETE FROM Like")

    def TraerObjeto(self, idpost, idusuario):
        Cursor = DB().run("SELECT * FROM `Like` WHERE Usuario_idUsuario = ('%s') AND Post_idPost = ('%s')" % (idusuario, idpost))
        for item in Cursor:
            self.Usuario_idUsuario = item["Usuario_idUsuario"]
            self.Post_idPost = item["Post_idPost"]
