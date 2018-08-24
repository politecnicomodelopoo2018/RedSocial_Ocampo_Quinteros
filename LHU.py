from DataBase import DB

class LHU (object):
    Like_idLike = None
    Usuario_idUsuario = None

    def SetLIL(self, idlike):
        self.Like_idLike = idlike

    def SetUIU(self, idU):
        self.Usuario_idUsuario = idU

    def Insert(self):
        DB().run("INSERT INTO Like_has_Usuario (Like_idLike, Usuario_idUsuario) VALUES ('%s','%s')"%(self.Like_idLike, self.Usuario_idUsuario))

    def Delete(self):
        DB().run("DELETE FROM Like_has_Usuario")