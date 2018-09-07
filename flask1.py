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



    unUsuario.Registro(Usuario, Contra, Email, Nombre, Bio)

    return render_template("helloworld.html")

@app.route("/Registro", methods=['GET', 'POST'])
def Register():
    return render_template("Registro.html")

@app.route("/Inicio")
def Inicio():
    return render_template("Inicio.html")

@app.route("/Perfil")
def Perfil():
    return render_template("Perfil.html")


if __name__ == '__main__':
    app.run(debug=True)
