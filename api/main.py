from fastapi import FastAPI
from .processors import ImageProcessor
from .serializers import ImageInformationResponse, ImageInformationRequest, ImageCropResponse, ImageCropRequest

app = FastAPI(version="0.0.1")

@app.post("/image-information", response_model=ImageInformationResponse)
async def image_information(request: ImageInformationRequest):
    im = ImageProcessor()
    im.parse_b64(request.image_data)
    return ImageInformationResponse.parse_from_img(im)


@app.post("/image-crop", response_model=ImageCropResponse)
async def image_crop(request: ImageCropRequest):
    im = ImageProcessor()
    im.parse_b64(request.image_data)
    im.crop(request.x0, request.x1, request.y0, request.y1)
    return ImageCropResponse(result_image=im.encode_b64())