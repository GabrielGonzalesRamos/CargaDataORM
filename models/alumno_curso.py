from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey
from config.conexion_bd import Base


class AlumnoCursoModel(Base):
    __tablename__ = 'TB_ALUMNO_CURSO'
    acIdAlumno = Column(ForeignKey(column='TB_ALUMNO.ID', onupdate='CASCADE', ondelete='CASCADE'), name='ID_ALUMNO', type_=types.Integer, primary_key=True, nullable=False)
    acIdCurso = Column(ForeignKey(column='TB_CURSO.ID', onupdate='CASCADE', ondelete='CASCADE'), name='ID_CURSO', type_=types.Integer, primary_key=True, nullable=False)

    def __init__(self, id_alumno, id_curso):
        self.acIdAlumno = id_alumno
        self.acIdCurso = id_curso

