from DataBase import DB
import datetime

class Usuario (object):

    idUsuario = None
    Nombre = None
    Contrasena = None
    Email = None
    FechaIngreso = None
    NombreVisible = None

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

    def Registro(self, Name, Contra, Email, NombreVi):
        self.SetNombre(Name)
        self.SetContrasena(Contra)
        self.SetMail(Email)
        self.SetFecha()
        self.SetNombreVisible(NombreVi)