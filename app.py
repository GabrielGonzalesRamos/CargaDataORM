from sqlalchemy import func
from config.conexion_bd import session
from models.alumno import AlumnoModel
from models.curso import CursoModel
from models.alumno_curso import AlumnoCursoModel
from random import randint
from faker import Faker
from datetime import datetime
from uuid import uuid4
import os


fake = Faker(['es_MX', 'es_AR', 'es_CL', 'es_CO'])

def TablaAlumno(alumnos):
    for i in range(1,int(alumnos) + 1):
        matricula = uuid4()
        nombre = f'{fake.first_name()}'
        apellido = f'{fake.last_name()} {fake.last_name()}'
        direccion =  fake.address()
        pais = fake.current_country()
        fecha_nacimiento = fake.date_between_dates(date_start=datetime(1990,1,1), date_end=datetime(2000,12,31))
        try:
            AlumnoModel(nombre=nombre, apellido=apellido, matricula=matricula, direccion=direccion, pais=pais, fecha_nacimiento=fecha_nacimiento).save()
        except Exception as E:
            print(E)

def TablaCurso():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'others/', '{}'.format(os.environ.get('TXT'))), mode='r') as cursos:
        for i in cursos.readlines():
            fecha_inicio = fake.date_between_dates(date_start=datetime(2023,1,1), date_end=datetime(2023,7,31))
            fecha_fin = fake.date_between_dates(date_start=fecha_inicio, date_end=datetime(2023,7,31))
            try:
                CursoModel(nombre=i.strip(), fecha_inicio=fecha_inicio, fecha_fin=fecha_fin).save()
            except Exception as E:
                print(E)

def TablaAlumnoCurso(alumnos):
    id_min_alumno = session.query(func.min(AlumnoModel.alumnoId)).scalar()
    id_max_alumno = session.query(func.max(AlumnoModel.alumnoId)).scalar()
    id_min_curso = session.query(func.min(CursoModel.cursoId)).scalar()
    id_max_curso = session.query(func.max(CursoModel.cursoId)).scalar()
    
    contador = 1
    
    while contador <= (int(alumnos)//2):

        alumno = randint(id_min_alumno, id_max_alumno)
        curso = randint(id_min_curso, id_max_curso)
        try:
            session.add(AlumnoCursoModel(id_alumno=alumno, id_curso=curso))
            session.commit()
            contador += 1
        except Exception as E:
            session.rollback()
        
if __name__ == '__main__':
    TablaAlumno(500)
    TablaCurso()
    TablaAlumnoCurso(500)

        

