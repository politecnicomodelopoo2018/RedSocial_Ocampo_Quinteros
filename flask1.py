from flask import *
from DataBase import DB
from Usuario import Usuario
from Post import Post
from Like import Like
from Comment import Comment
from UHU import UHU
from Etiqueta import Etiqueta
import os
from werkzeug.utils import secure_filename



DB().SetConnection('127.0.0.1', 'root', 'alumno', 'mydb')

unUsuario = Usuario()
unPost = Post()
unLike = Like()
unUHU = UHU()
unComment = Comment()
unaEtiqueta = Etiqueta()

UPLOAD_FOLDER = '/home/yisusyrama/'
app = Flask(__name__, static_url_path='/static')
app.secret_key = b'Tubidaor'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = {('png', 'jpg', 'jpeg')}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
def Logeoin():
    return render_template("helloworld.html")

@app.route("/LogOut", methods=['GET', 'POST'])
def Logueoout():
    session.pop('User', None)
    unUsuario.Registro(None, None, None, None, None)
    return redirect("/")

@app.route("/Registro", methods=['GET', 'POST'])
def Register():
    return render_template("Registro.html")

@app.route("/Registrado", methods=['GET', 'POST'])
def Registrado():
    Usuario = request.form.get("Usuario")
    Contra = request.form.get("Contrasena")
    Email = request.form.get("Email")
    Nombre = request.form.get("Nombre")
    Bio = request.form.get("Bio")

    if type(Usuario) != type(None):
        unUsuario.Registro(Usuario, Contra, Email, Nombre, Bio)
        return redirect("/")


@app.route("/Inicio", methods=['GET', 'POST'])
def Inicio():
    Usuario1 = request.form.get("Usuario")
    Contrasena1 = request.form.get("Contrasena")

    if (type(Usuario1) != None, type(Contrasena1) != None):
        unUsuario.TraerObjeto(Usuario1)
        if unUsuario.ValidarContrasena(Contrasena1) == True:
            session['User'] = Usuario1
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

@app.route("/BorrarCuenta", methods=['GET', 'POST'])
def BorrarCuenta():
    unUsuario.DeleteManual()
    return redirect("/")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/SubirPost", methods = ['GET', 'POST'])
def SubirPost():
    request.form.get("URL_Post")
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            unPost.SubirFoto(unUsuario.idUsuario, filename, request.form.get("Descripcion_Post"), request.form.get("Ubicacion_Post"))
            return redirect("/Perfil")
    return render_template("SubirPost.html")

@app.route("/VerPost", methods = ['GET', 'POST'])
def VerPost():
    PostSeleccionado = []
    cursor = DB().run("SELECT * FROM Post ORDER BY(idPost)")
    for item in cursor:
        unPost.TraerObjeto(item["idPost"])
        PostSeleccionado.append(unPost)

    return render_template("VerPost.html", PostSeleccionado=PostSeleccionado)

if __name__ == '__main__':
    app.run(debug=True)
