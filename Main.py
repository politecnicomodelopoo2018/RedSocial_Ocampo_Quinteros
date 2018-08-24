from DataBase import DB
from Usuario import Usuario

DB().SetConnection('127.0.0.1', 'root', 'alumno', 'mydb')

unUsuario = Usuario()

ContrasenaAValidar = input()

Cursor = DB().run("SELECT * FROM Usuario WHERE idUsuario = 1")
for item in Cursor:
    print(item)

if unUsuario.ValidarContrasena(ContrasenaAValidar) == True:
    print("Entro")
    ContrasenaNueva = input()
    unUsuario.UpdateContrasena(ContrasenaNueva)