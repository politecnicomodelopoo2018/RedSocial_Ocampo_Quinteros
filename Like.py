from DataBase import DB

class Like(object):
    Usuario_idUsuario = None
    Post_idPost = None

    def SetPost_idPost(self, Post_IdPost):
        self.Post_idPost = Post_IdPost

    def SetUsuario_idUsuario(self, Usuario_idUsuario):
        self.Usuario_idUsuario = Usuario_idUsuario

    def Insert(self):
        DB().run("INSERT INTO `Like` (Usuario_idUsuario, Post_idPost) VALUES (%s, %s)" % (self.Usuario_idUsuario, self.Post_idPost))