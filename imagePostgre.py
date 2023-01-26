from app.internal.repository.handlers.postgresql.collect_response import collect_response
from app.internal.repository.postgresql.connection import get_connection
from app.internal.repository import Repository
from app.pkg import models

__all__ = ["Image"]


class Image(Repository):
    @collect_response
    async def read_false(self, query: models.GetImageURL) -> models.ImageURL:
        q = """
            select 
                id, 
                static_path,
                external_path,
                is_downloaded
            from images
            where images.is_downloaded = %(is_downloaded)s;
            returning
                id, external_path;
        """
        async with get_connection() as cur:
            await cur.execute(q, query.to_dict(show_secrets=True))
            return await cur.fetchone()
