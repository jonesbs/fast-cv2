from pydantic import BaseModel, validator, ValidationError
from .processors import ImageProcessor

class ImageInformationRequest(BaseModel):
    image_data: str


class ImageInformationResponse(BaseModel):
    image_size: int
    image_resolution: str

    @staticmethod
    def parse_from_img(processor: ImageProcessor):
        return ImageInformationResponse(
            image_size=processor.image.size,
            image_resolution="{}x{}".format(processor.image.shape[1], processor.image.shape[0])
        )

class ImageCropRequest(BaseModel):
    image_data: str
    x0: int
    x1: int
    y0: int
    y1: int

    @validator("*")
    def validate_coordinates(item):
        if isinstance(item, int) and item < 0:
            raise ValueError("Coordinates need to be positive values")

class ImageCropResponse(BaseModel):
    result_image: str
