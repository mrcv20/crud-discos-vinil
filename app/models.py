from . import db
from typing import List


class Artist(db.Model):
    __tablename__ = "artistas"

    id = db.Column(db.Integer, primary_key=True, index=True)
    artista = db.Column(db.String(20), nullable=False)
    discos = db.relationship("VinylDisc", primaryjoin="Artist.id == VinylDisc.id_artista", cascade='all, delete-orphan')


    @classmethod
    def find_all(cls) -> List["Artist"]:
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, _id) -> "Artist":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_artist(cls, _artista) -> ["Artist"]:
        return cls.query.filter_by(artista=_artista).first()    

    def save_in_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def update_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()



class VinylDisc(db.Model):
    __tablename__ = "discos"

    id = db.Column(db.Integer, primary_key=True, index=True)
    genero = db.Column(db.String(20))
    titulo = db.Column(db.String(50))
    valor = db.Column(db.Float)
    id_artista = db.Column(db.Integer, db.ForeignKey('artistas.id'), nullable=False)
    artista = db.relationship("Artist", back_populates="discos")
    

    @classmethod
    def find_all(cls) -> List["VinylDisc"]:
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, _id) -> "VinylDisc":
        return cls.query.filter_by(id=_id).first()
    
    def save_in_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def update_db(self) -> None:
        db.session.update(self)
        db.session.commit()




