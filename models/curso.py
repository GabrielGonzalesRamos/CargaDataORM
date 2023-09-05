from config.conexion_bd import session
from sqlalchemy import Column, types, orm, UniqueConstraint, CheckConstraint
from config.conexion_bd import session, Base


class CursoModel(Base):
    __tablename__ = 'tb_curso'
    cursoId = Column(name='id', primary_key=True, autoincrement=True, unique=True, type_=types.Integer, nullable=False)
    cursoNombre = Column(name='nombre', unique=True, type_=types.String(length=100), nullable=False)
    cursoFechaInicio = Column(name='fecha_inicio', type_=types.Date)
    cursoFechaFin = Column(name='fecha_fin', type_=types.Date)

    cursoRegistrados = orm.relationship('AlumnoCursoModel', backref='registroCurso', lazy=True, cascade='all, delete-orphan')

    __table_args__ = (
        UniqueConstraint('nombre', name='avoid_duplicate_tb_curso'),
        CheckConstraint('fecha_inicio < fecha_fin')
    )

    def __init__(self, nombre, fecha_inicio, fecha_fin):
        self.cursoNombre = nombre
        self.cursoFechaInicio = fecha_inicio
        self.cursoFechaFin = fecha_fin
    
    def save(self):
        session.add(self)
        session.commit()


    