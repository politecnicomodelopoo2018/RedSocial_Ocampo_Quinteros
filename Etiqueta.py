from DataBase import DB

class Etiqueta(object):
    Usuario_idUsuario = None
    Post_idPost = None

    def setUsuarioIdU(self, UidU):
        self.Usuario_idUsuario = UidU

    def setUsuarioIdUone(self, idPost):
        self.Post_idPost = idPost

    def Insert(self):
        DB().run("INSERT INTO Etiqueta (Usuario_idUsuario, Post_idPost) VALUES ('%s','%s')" % (self.Usuario_idUsuario, self.Post_idPost))

    def Delete(self):
        DB().run("DELETE FROM Etiqueta")