from DataBase import DB

class CHU(object):
    Comment_idComment = None
    Usuario_idUsuario = None

    def SetLIL(self, idComment):
        self.Comment_idComment = idComment

    def SetUIU(self, idU):
        self.Usuario_idUsuario = idU

    def Insert(self):
        DB().run("INSERT INTO Comment_has_Usuario (Comment_idComment, Usuario_idUsuario) VALUES ('%s','%s')" % (self.Comment_idComment, self.Usuario_idUsuario))

    def Delete(self):
        DB().run("DELETE FROM Comment_has_Usuario")
