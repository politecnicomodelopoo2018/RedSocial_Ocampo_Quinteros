from DataBase import DB

class UHU(object):
    Usuario_idUsuario = None
    Usuario_idUsuarione = None

    def setUsuarioIdU (self, UidU):
        self.Usuario_idUsuario = UidU

    def setUsuarioIdUone (self, UidUone):
        self.Usuario_idUsuarione = UidUone

    def Insert(self):
        DB().run("INSERT INTO Usuario_has_Usuario (Usuario_idUsuario, Usuario_idUsuario1) VALUES ('%s','%s')"%(self.Usuario_idUsuario, self.Usuario_idUsuarione))

    def Delete(self):
        DB().run("DELETE FROM Usuario_has_Usuario")