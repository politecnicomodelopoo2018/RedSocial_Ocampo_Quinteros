def Insert(self):
    cursor = DB().run("INSERT INTO Ciatura (Nombre_Criatura, Descripcion_Criatura, Traduccion_Criatura, Reino_idReino) VALUES ('%s', '%s', '%s', '%s')" % (self.Nombre, self.Descripcion, self.Traduccion, self.idReino))
    self.id = cursor.lastrowid


def Update(self, Nombre, Descripcion, Traduccion, idReino, idUpdate):
    DB().run("UPDATE Ciatura SET Nombre_Criatura = ('%s'), Descripcion_Criatura = ('%s'), Traduccion_Criatura = ('%s'), Reino_idReino = ('%s') WHERE idCiatura = ('%d')" % (
    Nombre, Descripcion, Traduccion, idReino, idUpdate))


def Delete(self, idDelete):
    DB().run("DELETE FROM Ciatura WHERE idCiatura = ('%d')" % (idDelete))