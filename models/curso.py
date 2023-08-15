from config.conexion_bd import session
from sqlalchemy import Column, types, orm
from config.conexion_bd import session, Base


class CursoModel(Base):
    __tablename__ = 'TB_CURSO'
    cursoId = Column(name='ID', primary_key=True, autoincrement=True, unique=True, type_=types.Integer, nullable=False)
    cursoNombre = Column(name='NOMBRE', unique=True, type_=types.String(length=100), nullable=False)
    cursoFechaInicio = Column(name='FECHA_INICIO', type_=types.Date)
    cursoFechaFin = Column(name='FECHA_FIN', type_=types.Date)

    cursoRegistrados = orm.relationship('AlumnoCursoModel', backref='registroCurso', lazy=True, cascade='all, delete-orphan')

    def __init__(self, nombre, fecha_inicio, fecha_fin):
        self.cursoNombre = nombre
        self.cursoFechaInicio = fecha_inicio
        self.cursoFechaFin = fecha_fin
    
    def save(self):
        session.add(self)
        session.commit()


    