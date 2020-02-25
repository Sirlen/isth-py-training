# Empty
"""Methods for altering the file tables"""
from app.infrastructure import file_repository

# SCE
from app.domain.model import Usuario



def get_file(nombre):   
    """Get a file"""
    return file_repository.get_file(nombre)


def post_file(nombre, contenido):

    
    """Create an new file"""
    return file_repository.post_file(nombre, contenido)
    
    
    if len(Username)<6:
        print('El Username no puede ser menor a 6 caracteres')
        Username = Usuario.Nombre + Usuario.Apellido

    if (nombre[0:1]).islower())
        print('El nombre debe tener la primera letra mayuscula')
        print(nombre[0:1]).islower())
        print(nombre.lower().capitalize())


