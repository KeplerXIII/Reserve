from app.internal.repository.repository import BaseRepository
from app.pkg import models


class Image:

    def __init__(self, repository: BaseRepository):
        self.repository = repository

    async def get_images(self, query: models.GetImageURL) -> models.ImageURL:
        return await self.repository.read(query=query)

    def create_static(self, cmd: models.CreateStaticImage) -> models.CreateStaticImage:
        pass

    def converter(self):
        pass
