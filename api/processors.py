from .utils import Image
from .exceptions import ImageProcessError, ImageCropProcessError

IMAGE_ACCEPTED_EXTENSIONS = ["png", "jpg", "jpeg", "webp", "gif"]

class ImageProcessor:

    def parse_b64(self, img_b64: str):
        try:
            img, self.extension = Image.decode(img_b64)
            if self.extension not in IMAGE_ACCEPTED_EXTENSIONS:
                raise ImageProcessError

            self.image = Image.read_bytes(img)
        except:
            raise ImageProcessError

    def validate_coordinates(self, x0: int, x1: int, y0: int, y1: int):
        width = self.image.shape[1]
        height = self.image.shape[0]
        top_endpoint = y0+y1
        right_endpoint = x0+x1
        if top_endpoint > height or right_endpoint > width:
            raise ImageCropProcessError(f"Coordinates and sizes exceeds the maximum image dimension {width}x{height}")
        
    def crop(self, x0: int, x1: int, y0: int, y1: int):
        self.validate_coordinates(x0, x1, y0, y1)
        self.image = self.image[y0:y0+y1, x0:x0+x1]
        
    def encode_b64(self):
        encoded = Image.encode(self.image, self.extension)
        return f"data:image/{self.extension};base64,{encoded}"