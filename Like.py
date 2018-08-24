from DataBase import DB

class Like(object):
    idLike = None
    Post_idPost = None

    def SetPost_idPost(self, Post_IdPost):
        self.Post_idPost = Post_IdPost

    def Insert(self):
        Cursor = DB().run("INSERT INTO Like (Post_idPost) VALUES ('%s')"%(self.Post_idPost))
        self.idLike = Cursor.lastrowid