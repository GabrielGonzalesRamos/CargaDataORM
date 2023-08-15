from sqlalchemy import Column, types, orm
from config.conexion_bd import session, Base


class AlumnoModel(Base):
    __tablename__ = 'TB_ALUMNO'
    alumnoId = Column(name='ID', primary_key=True, autoincrement=True, unique=True, type_=types.Integer, nullable=False)
    alumnoMatricula = Column(name='MATRICULA', unique=True, type_=types.String(length=45), nullable=False)
    alumnoNombre = Column(name='NOMBRE', type_=types.String(length=45))
    alumnoApellido = Column(name='APELLIDO', type_=types.String(length=45))
    alumnoDireccion = Column(name='DIRECCION', type_=types.String(length=200))
    alumnoPais = Column(name='PAIS', type_=types.String(length=200))
    alumnoFechaNacimiento = Column(name='FECHA_NACIMIENTO', type_=types.Date)

    alumnoRegistrado = orm.relationship('AlumnoCursoModel', backref='registroAlumno', lazy=True, cascade='all, delete-orphan')

    def __init__(self, nombre, apellido, matricula, direccion, pais, fecha_nacimiento):
        self.alumnoNombre = nombre
        self.alumnoApellido = apellido
        self.alumnoMatricula = matricula
        self.alumnoDireccion = direccion
        self.alumnoPais = pais
        self.alumnoFechaNacimiento = fecha_nacimiento
    
    def save(self):
        session.add(self)
        session.commit()
    

