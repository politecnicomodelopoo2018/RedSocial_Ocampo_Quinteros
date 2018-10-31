from DataBase import DB
import datetime

class Usuario (object):

    idUsuario = None
    Nombre = None
    Contrasena = None
    Email = None
    FechaIngreso = None
    NombreVisible = None
    Biografia = None

    # -------------Registro--------------

    def SetNombre(self, Nombre):
        self.Nombre = Nombre

    def SetContrasena(self, Contrasena):
        self.Contrasena = Contrasena

    def SetMail(self, Mail):
        self.Email = Mail

    def SetFecha(self):
        self.FechaIngreso = datetime.date.today()

    def SetNombreVisible(self, Nombre):
        self.NombreVisible = Nombre

    def SetBiografia(self, Bio):
        self.Biografia = Bio

    def Insert(self):
        cursor = DB().run("INSERT INTO Usuario (Nombre_Usuario, Contraseña_Usuario, Email_Usuario, Fecha_ingreso_Usuario, Nombrevisible_Usuario, Biografia_Usuario) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (self.Nombre, self.Contrasena, self.Email, self.FechaIngreso, self.NombreVisible, self.Biografia))
        self.idUsuario = cursor.lastrowid

    def Registro(self, Name, Contra, Email, NombreVi, Bio):
        self.SetNombre(Name)
        self.SetContrasena(Contra)
        self.SetMail(Email)
        self.SetFecha()
        self.SetNombreVisible(NombreVi)
        self.SetBiografia(Bio)
        self.Insert()

    def RegistroSinInsert(self, Name, Contra, Email, NombreVi, Bio):
        self.SetNombre(Name)
        self.SetContrasena(Contra)
        self.SetMail(Email)
        self.SetFecha()
        self.SetNombreVisible(NombreVi)
        self.SetBiografia(Bio)

    # ----------Delete & UpdateNombreVisible & UpdateBio-------------

    def DeleteManual(self):
        DB().run("DELETE FROM Usuario WHERE idUsuario = ('%d')" % (self.idUsuario))

    def UpdateNombreVisible(self, Nombre):
        self.SetNombreVisible(Nombre)
        DB().run("UPDATE Usuario SET Nombrevisible_Usuario = ('%s')" % (self.NombreVisible))

    def UpdateBiografia(self, Bio):
        self.SetBiografia(Bio)
        DB().run("UPDATE Usuario SET Biografia_Usuario = ('%s')" % (self.Biografia))

    # -------------ContrasenaUpdate--------------

    def UpdateContrasena(self, contrasena):
        self.SetContrasena(contrasena)
        DB().run("UPDATE Usuario SET Contraseña_Usuario = ('%s') WHERE idUsuario = ('%s')" % (self.Contrasena, self.idUsuario))

    def ValidarContrasena(self, ContrasenaValidar):
        Validacion = False
        if self.Contrasena == ContrasenaValidar:
            Validacion = True
        return Validacion

    # -------------Utilities--------------

    def TraerObjeto(self, Usuario):
        Cursor = DB().run("SELECT * FROM Usuario WHERE Nombre_Usuario = ('%s')" % (Usuario))
        for item in Cursor:
            self.idUsuario = item["idUsuario"]
            self.Nombre = item["Nombre_Usuario"]
            self.Email = item["Email_Usuario"]
            self.Contrasena = item["Contraseña_Usuario"]
            self.FechaIngreso = item["Fecha_ingreso_Usuario"]
            self.NombreVisible = item["Nombrevisible_Usuario"]
            self.Biografia = item["Biografia_Usuario"]