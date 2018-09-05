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


