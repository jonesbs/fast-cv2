import base64
import cv2
import re
import numpy as np

from .exceptions import ImageProcessError

class Image:

    @staticmethod
    def decode(image:str):
        image = re.search(r'^data:image/([a-zA-Z]+);base64,(.*)', image)
        return base64.decodebytes(image.group(2).encode("utf8")), image.group(1)

    @staticmethod
    def encode(image, extension) -> str:
        _, image = cv2.imencode(f".{extension}", image)
        return base64.b64encode(image.tobytes()).decode("utf8")
    
    @staticmethod
    def read_bytes(image):
        image = np.asarray(bytearray(image), dtype="uint8")
        cv2_object = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
        if cv2_object is None:
            raise ImageProcessError
        
        return cv2_object