from . import db



# class Artist(db.Model):
#     __tablename__ = "artistas"

#     id = db.Column(db.Integer, primary_key=True, index=True)
#     nome = db.Column(db.String(20))
#     generos = db.Column(db.String(50))
#     children = db.relationship("VinylDisc")
    
    
class VinylDisc(db.Model):
    __tablename__ = "discos"

    id = db.Column(db.Integer, primary_key=True, index=True)
    genero = db.Column(db.String(20))
    titulo = db.Column(db.String(50))
    valor = db.Column(db.Float)
    artista = db.Column(db.String(25))


    def __repr___(self):
        return 'VynilDisc(titulo=%s)' % self.titulo



