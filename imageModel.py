from pydantic.networks import AnyUrl

from .base import BaseModel
from pydantic.fields import Field
from pydantic.types import PositiveInt

__all__ = [
    "ImageFields",
    "BaseImage",
    "GetImageURL",
    "ImageURL",
    "DownloadImage",
    "CreateStaticImage",
]


class ImageFields:
    id = Field(description="Image id.")
    external_path = Field(description='Image url.')
    static_path = Field(description='Image path.')
    is_downloaded = Field(description='Image state.')


class BaseImage(BaseModel):
    """Базовая модель"""


class GetImageURL(BaseImage):
    is_downloaded: ImageFields.is_downloaded


class ImageURL(BaseImage):
    id: PositiveInt = ImageFields.id
    external_path: AnyUrl = ImageFields.external_path


class DownloadImage(BaseImage):
    id: PositiveInt = ImageFields.id
    external_path: AnyUrl = ImageFields.external_path
    static_path: ImageFields.static_path


class CreateStaticImage(BaseImage):
    id: PositiveInt = ImageFields.id
    static_path: ImageFields.static_path
