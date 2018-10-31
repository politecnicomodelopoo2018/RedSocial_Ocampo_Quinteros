from flask import *
from DataBase import DB
from Usuario import Usuario
from Post import Post
from Like import Like
from Comment import Comment
import os
from werkzeug.utils import secure_filename

DB().SetConnection('127.0.0.1', 'root', 'alumno', 'mydb')

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
    if 'User' in session:
        UsuarioLogOut = Usuario()
        UsuarioLogOut.RegistroSinInsert(None, None, None, None, None)
        session.pop('User', None)
        return redirect("/")
    else:
        return redirect("/")

@app.route("/Registro", methods=['GET', 'POST'])
def Register():
    return render_template("Registro.html")

@app.route("/Registrado", methods=['GET', 'POST'])
def Registrado():
    if type(request.args.get("HTML")) != type(None):
        if int(request.args.get("HTML")) == 1:
            UsuarioRegistrado = Usuario()
            UsuarioGet = request.form.get("Usuario")
            Contra = request.form.get("Contrasena")
            Email = request.form.get("Email")
            Nombre = request.form.get("Nombre")
            Bio = request.form.get("Bio")

            if type(UsuarioGet) != type(None):
                UsuarioRegistrado.Registro(UsuarioGet, Contra, Email, Nombre, Bio)
                return redirect("/")
    elif type(request.args.get("HTML")) == type(None):
        return redirect("/")

@app.route("/Confirmacion", methods=['GET', 'POST'])
def Confirmacion():
    if int(request.args.get("Co")) == 1:
        UsuarioConfirmacion = Usuario()
        Usuario1 = request.form.get("Usuario")
        Contrasena1 = request.form.get("Contrasena")

        if (type(Usuario1) != None, type(Contrasena1) != None):
            UsuarioConfirmacion.TraerObjeto(Usuario1)
            if UsuarioConfirmacion.ValidarContrasena(Contrasena1) == True:
                session['User'] = Usuario1
                return redirect("/Inicio")
            if UsuarioConfirmacion.ValidarContrasena(Contrasena1) == False:
                return redirect("/")
    elif int(request.args.get("Co")) != 1:
        return redirect("/")

@app.route("/Inicio", methods = ['GET', 'POST'])
def Inicio():
    if 'User' in session:
        UsuarioInicio = Usuario()
        UsuarioInicio.TraerObjeto(session['User'])
        cursorsito = DB().run("SELECT * FROM Usuario")
        for itemsito in cursorsito:
            if itemsito["Nombre_Usuario"] == None:
                UsuarioInicio.TraerObjeto(itemsito["idUsuario"])
                UsuarioInicio.DeleteManual()
        Usuariohtml = UsuarioInicio.TraerObjeto(session['User'])
        PostSeleccionado = []
        CommentSeleccionado = []
        cursor = DB().run("SELECT * FROM Post ORDER BY(idPost)DESC")
        for item in cursor:
            PostInicio = Post()
            PostInicio.TraerObjeto(item["idPost"])
            PostInicio.Contador()
            PostSeleccionado.append(PostInicio)
        cursor2 = DB().run("SELECT * FROM `Like`")
        LikesExistentes = []
        for item2 in cursor2:
            LikeInicio = Like()
            LikeInicio.TraerObjeto(item2["Post_idPost"], item2["Usuario_idUsuario"])
            LikesExistentes.append(LikeInicio)
        cursor3 = DB().run("SELECT * FROM Comment ORDER BY(idComment)ASC")
        for item3 in cursor3:
            CommentInicio = Comment()
            CommentInicio.TraerObjeto(item3["idComment"])
            CommentSeleccionado.append(CommentInicio)
        return render_template("VerPost.html", PostSeleccionado=PostSeleccionado, LikesExistentes=LikesExistentes, Usuariohtml=Usuariohtml, UserIniciado=UsuarioInicio, CommentSeleccionado=CommentSeleccionado)
    elif 'User' not in session:
        return redirect("/")


@app.route("/EditarPerfil", methods=['GET', 'POST'])
def EditarPerfil():
    if 'User' in session:
        UsuarioEditarPerfil = Usuario()
        UsuarioEditarPerfil.TraerObjeto(session['User'])
        return render_template("EditarPerfil.html", UsuarioEdit = UsuarioEditarPerfil.Nombre, ContraEdit = UsuarioEditarPerfil.Contrasena, EmailEdit = UsuarioEditarPerfil.Email, NombreEdit = UsuarioEditarPerfil.NombreVisible, BioEdit = UsuarioEditarPerfil.Biografia)
    else:
        return redirect("/")

@app.route("/PerfilEditado", methods=['GET', 'POST'])
def PerfilEditado():
    if 'User' in session:
        UsuarioPerfilEditado = Usuario()
        UsuarioPerfilEditado.TraerObjeto(session['User'])
        EditedPassword = request.form.get("Contrasena")
        EditedName = request.form.get("Nombre")
        EditedBio = request.form.get("Bio")
        if type(EditedName) != type(None):
            UsuarioPerfilEditado.UpdateNombreVisible(EditedName)
            UsuarioPerfilEditado.UpdateBiografia(EditedBio)
            UsuarioPerfilEditado.UpdateContrasena(EditedPassword)
        return redirect("/Inicio")
    else:
        return redirect("/")

@app.route("/BorrarCuenta", methods=['GET', 'POST'])
def BorrarCuenta():
    if 'User' in session:
        UsuarioBorrarCuenta = Usuario()
        UsuarioBorrarCuenta.TraerObjeto(session['User'])
        UsuarioBorrarCuenta.DeleteManual()
        UsuarioBorrarCuenta.RegistroSinInsert(None, None, None, None, None)
        return redirect("/")
    else:
        return redirect("/")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/SubirPost", methods = ['GET', 'POST'])
def SubirPost():
    if 'User' in session:
        PostSubirPost = Post()
        UsuarioSubirPost = Usuario()
        UsuarioSubirPost.TraerObjeto(session['User'])
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
                PostSubirPost.SubirFoto(UsuarioSubirPost.idUsuario, filename, request.form.get("Descripcion_Post"), request.form.get("Ubicacion_Post"))
                return redirect("/Inicio")
        return render_template("SubirPost.html")
    else:
        return redirect("/")

@app.route("/Like", methods = ['GET', 'POST'])
def Likecito():
    if 'User' in session:
        LikeLike = Like()
        UsuarioLike = Usuario()
        UsuarioLike.TraerObjeto(session['User'])
        idPosta = request.args.get("IdPost")
        idUserinho = UsuarioLike.idUsuario
        LikeLike.AllSets(idPosta, idUserinho)
        cursor = DB().run("SELECT * FROM `Like` WHERE Post_idPost = ('%s') AND Usuario_idUsuario = ('%s') " % (idPosta, idUserinho))
        if len(cursor.fetchall())==0:
            LikeLike.Insert()
        else:
            DB().run("DELETE FROM `Like` WHERE Post_idPost = ('%s') AND Usuario_idUsuario = ('%s')" % (idPosta, idUserinho))
        return redirect("/Inicio#p" + idPosta)
    else:
        return redirect("/")

@app.route("/Comentario", methods = ['GET', 'POST'])
def Comentarios():
    if 'User' in session:
        CommentComment = Comment()
        UsuarioComentario = Usuario()
        UsuarioComentario.TraerObjeto(session['User'])
        idPosta = request.args.get("IdPost")
        Userinho = UsuarioComentario
        ComentariosDesc = request.form.get("Comentario")
        CommentComment.AllSetsComments(ComentariosDesc, idPosta, Userinho)
        CommentComment.Insert()
        return redirect("/Inicio#p" + idPosta)
    else:
        return redirect("/")

@app.route("/BorrarComentario", methods = ['GET', 'POST'])
def BorrarComentarios():
    if 'User' in session:
        UsuarioBorrarComentario = Usuario()
        UsuarioBorrarComentario.TraerObjeto(session['User'])
        idPosta = request.args.get("IdPost")
        idUserinho = UsuarioBorrarComentario.idUsuario
        idComment = request.args.get("IdComment")
        DB().run("DELETE FROM Comment WHERE idComment = ('%s') AND Usuario_idUsuario = ('%s') AND Post_idPost = ('%s')" % (idComment, idUserinho, idPosta))
        return redirect("/Inicio#p" + idPosta)
    else:
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)