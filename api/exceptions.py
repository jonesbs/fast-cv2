from fastapi import HTTPException

class ImageProcessError(HTTPException):
    status_code = 400
    detail = "Data invalid"

    def __init__(self):
        super().__init__(self.status_code, self.detail)


class ImageCropProcessError(HTTPException):
    status_code = 400
    detail = "Data invalid"

    def __init__(self, message=None):
        if message is None:
            message = self.detail

        super().__init__(self.status_code, message)