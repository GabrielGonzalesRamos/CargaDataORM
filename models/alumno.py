from sqlalchemy import Column, types, orm, UniqueConstraint, CheckConstraint
from config.conexion_bd import session, Base


class AlumnoModel(Base):
    __tablename__ = 'TB_ALUMNO'
    alumnoId = Column(name='ID',autoincrement=True, primary_key=True, unique=True, type_=types.Integer, nullable=False)
    alumnoDNI = Column(name='DNI', unique=True, type_=types.String(length=8), nullable=False)
    alumnoNombre = Column(name='NOMBRE', type_=types.String(length=45))
    alumnoApellido = Column(name='APELLIDO', type_=types.String(length=45))
    alumnoDireccion = Column(name='DIRECCION', type_=types.String(length=200))
    alumnoPais = Column(name='PAIS', type_=types.String(length=200))
    alumnoFechaNacimiento = Column(name='FECHA_NACIMIENTO', type_=types.Date)

    alumnoRegistrado = orm.relationship('AlumnoCursoModel', backref='registroAlumno', lazy=True, cascade='all, delete-orphan')

    __table_args__ = (
        UniqueConstraint('NOMBRE', 'APELLIDO', 'DNI', name='avoid_duplicate_tb_alumno'),
        CheckConstraint('DNI LIKE "%[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]%"', name='only_numbers_8_tb_alumno')
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
    

