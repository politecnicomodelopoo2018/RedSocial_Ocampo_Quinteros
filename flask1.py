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

UPLOAD_FOLDER = 'static/img/'
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


@app.route("/Confirmacion", methods=['GET', 'POST'])
def Confirmacion():
    Usuario1 = request.form.get("Usuario")
    Contrasena1 = request.form.get("Contrasena")

    if (type(Usuario1) != None, type(Contrasena1) != None):
        unUsuario.TraerObjeto(Usuario1)
        if unUsuario.ValidarContrasena(Contrasena1) == True:
            session['User'] = Usuario1
            return redirect("/Inicio")
        if unUsuario.ValidarContrasena(Contrasena1) == False:
            return redirect("/")

@app.route("/Inicio", methods = ['GET', 'POST'])
def Inicio():
    unUsuario.TraerObjeto(session['User'])
    Usuariohtml = unUsuario.TraerObjeto(session['User'])
    PostSeleccionado = []
    cursor = DB().run("SELECT * FROM Post ORDER BY(idPost)DESC")
    for item in cursor:
        unPost=Post()
        unPost.TraerObjeto(item["idPost"])
        unPost.Contador()
        PostSeleccionado.append(unPost)
    cursor2 = DB().run("SELECT * FROM `Like`")
    LikesExistentes = []
    for item2 in cursor2:
        unLike=Like()
        unLike.TraerObjeto(item2["Post_idPost"], item2["Usuario_idUsuario"])
        LikesExistentes.append(unLike)
    return render_template("VerPost.html", PostSeleccionado=PostSeleccionado, LikesExistentes=LikesExistentes, Usuariohtml=Usuariohtml)


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
            return redirect("/Inicio")
    return render_template("SubirPost.html")

@app.route("/Like", methods = ['GET', 'POST'])
def Likecito():

    idPosta = request.args.get("IdPost")
    unLike.AllSets(idPosta, unUsuario.idUsuario)
    cursor = DB().run("SELECT * FROM `Like` WHERE Post_idPost = ('%s') AND Usuario_idUsuario = ('%s') " % (idPosta, unUsuario.idUsuario))
    if len(cursor.fetchall())==0:
        unLike.Insert()
    else:
        DB().run("DELETE FROM `Like` WHERE Post_idPost = ('%s')" % (idPosta))

    return redirect("/Inicio#p" + idPosta )



if __name__ == '__main__':
    app.run(debug=True)