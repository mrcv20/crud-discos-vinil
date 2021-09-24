from app import ma


class DiscoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'genero', 'titulo', 'valor', 'artista')



discos_schema = DiscoSchema(many=True)


# class VynilDiscSchema(SQLAlchemySchema):
#     class Meta:
#         model = VynilDisc
#         load_instance = True
#     id = auto_field()
#     genero = auto_field()
#     titulo = auto_field()
#     valor = auto_field()

