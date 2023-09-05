from sqlalchemy import Column, types, orm, UniqueConstraint, CheckConstraint
from config.conexion_bd import session, Base


class AlumnoModel(Base):
    __tablename__ = 'tb_alumno'
    alumnoId = Column(name='id',autoincrement=True, primary_key=True, unique=True, type_=types.Integer, nullable=False)
    alumnoDNI = Column(name='dni', unique=True, type_=types.String(length=8), nullable=False)
    alumnoNombre = Column(name='nombre', type_=types.String(length=45))
    alumnoApellido = Column(name='apellido', type_=types.String(length=45))
    alumnoDireccion = Column(name='direccion', type_=types.String(length=200))
    alumnoPais = Column(name='pais', type_=types.String(length=200))
    alumnoFechaNacimiento = Column(name='fecha_nacimiento', type_=types.Date)

    alumnoRegistrados = orm.relationship('AlumnoCursoModel', backref='registroAlumno', lazy=True, cascade='all, delete-orphan')

    __table_args__ = (
        UniqueConstraint('nombre', 'apellido', 'dni', name='avoid_duplicate_tb_alumno'),
        CheckConstraint('dni ~ \'^[0-9]{8}$\'', name='only_numbers_8_tb_alumno')
        )

    def __init__(self, nombre, apellido, dni, direccion, pais, fecha_nacimiento):
        self.alumnoNombre = nombre
        self.alumnoApellido = apellido
        self.alumnoDNI = dni
        self.alumnoDireccion = direccion
        self.alumnoPais = pais
        self.alumnoFechaNacimiento = fecha_nacimiento
    
    def save(self):
        session.add(self)
        session.commit()
    

