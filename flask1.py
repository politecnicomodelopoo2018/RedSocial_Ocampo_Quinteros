from flask import *
from DataBase import DB
from Usuario import Usuario
from Post import Post
from Like import Like
from Comment import Comment
from UHU import UHU
from Etiqueta import Etiqueta

DB().SetConnection('127.0.0.1', 'root', 'alumno', 'mydb')

unUsuario = Usuario()
unPost = Post()
unLike = Like()
unUHU = UHU()
unComment = Comment()
unaEtiqueta = Etiqueta()


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def Logeoin():
    Usuario = request.form.get("Usuario")
    Contra = request.form.get("Contrasena")
    Email = request.form.get("Email")
    Nombre = request.form.get("Nombre")
    Bio = request.form.get("Bio")

    if request.args.get('BorrarCuenta') == '1':
        unUsuario.DeleteManual()


    if type(Usuario) != type(None):
        unUsuario.Registro(Usuario, Contra, Email, Nombre, Bio)

    return render_template("helloworld.html")

@app.route("/Registro", methods=['GET', 'POST'])
def Register():
    return render_template("Registro.html")


@app.route("/Inicio", methods=['GET', 'POST'])
def Inicio():
    Usuario1 = request.form.get("Usuario")
    Contrasena1 = request.form.get("Contrasena")

    if (type(Usuario1) != None, type(Contrasena1) != None):
        unUsuario.TraerObjeto(Usuario1)
        if unUsuario.ValidarContrasena(Contrasena1) == True:
            return render_template("Inicio.html", user = unUsuario.Nombre)
        if unUsuario.ValidarContrasena(Contrasena1) == False:
            return redirect("/")


@app.route("/Perfil", methods=['GET', 'POST'])
def Perfil():
    EditedPassword = request.form.get("Contrasena")
    EditedName = request.form.get("Nombre")
    EditedBio = request.form.get("Bio")

    if type(EditedName) != type(None):
        unUsuario.UpdateNombreVisible(EditedName)
        unUsuario.UpdateBiografia(EditedBio)
        unUsuario.UpdateContrasena(EditedPassword)

    return render_template("Perfil.html")

@app.route("/EditarPerfil", methods=['GET', 'POST'])
def EditarPerfil():
    return render_template("EditarPerfil.html", UsuarioEdit = unUsuario.Nombre, ContraEdit = unUsuario.Contrasena, EmailEdit = unUsuario.Email, NombreEdit = unUsuario.NombreVisible, BioEdit = unUsuario.Biografia)

if __name__ == '__main__':
    app.run(debug=True)
