from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey
from config.conexion_bd import Base


class AlumnoCursoModel(Base):
    __tablename__ = 'tb_alumno_curso'
    acIdAlumno = Column(ForeignKey(column='tb_alumno.id', onupdate='CASCADE', ondelete='CASCADE'), name='id_alumno', type_=types.Integer, primary_key=True, nullable=False)
    acIdCurso = Column(ForeignKey(column='tb_curso.id', onupdate='CASCADE', ondelete='CASCADE'),name='id_curso', type_=types.Integer, primary_key=True, nullable=False)

    def __init__(self, id_alumno, id_curso):
        self.acIdAlumno = id_alumno
        self.acIdCurso = id_curso

