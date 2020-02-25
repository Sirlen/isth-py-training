"""Service methods for file endpoints"""

# SCE
from app.common import Constants

import os


class fileRepository:

    def get_file(self, id):
        return NotImplementedError

    def post_file(self, nombre, data):

        filepath = os.path.join(FILE_UPLOAD_PATH, nombre) if not os.path.exists(FILE_UPLOAD_PATH): os.makedirs(FILE_UPLOAD_PATH) f = open(filepath, "a")
        return NotImplementedError

        