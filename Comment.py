from DataBase import DB

class Comment (object):
    idComment = None
    Descripcion = None
    Post_idPost = None

    def SetDescripcion(self, Descripcion):
        self.Descripcion = Descripcion

    def SetPost_idPost(self, Post_idPost):
        self.Post_idPost = Post_idPost

    def Insert(self):
        Cursor = DB().run("INSERT INTO Comment (Descripcion_Comment, Post_idPost) VALUES ('%s', '%s')" % (self.Descripcion, self.Post_idPost))
        self.idComment = Cursor.lastrowid