from ninja import Router

from accounts.authentication import JWTAuth
from shortener.services.shortener_service import ShortenerService
from .schemas import UrlCreateSchema, UrlSchema, UrlUpdateSchema

auth = JWTAuth()
router = Router(tags=["Shortener"])
service = ShortenerService()


@router.get("/urls", auth=auth, response=list[UrlSchema])
def get_urls(request):
    return service.get_all(request.auth)

@router.post("/urls", auth=auth, response=UrlSchema)
def create_url(request, data: UrlCreateSchema):
    return service.create(
        long_url=data.long_url,
        user=request.auth,
        title=data.title
    )

@router.patch("/urls/{code}", auth=auth, response=UrlSchema)
def edit_url(request, code: str, data: UrlUpdateSchema):
    return service.edit(
        code=code,
        user=request.auth,
        title=data.title,
        long_url=data.long_url
    )

@router.delete("/urls/{code}", auth=auth, response={204: None})
def delete_url(request, code: str):
    service.delete(
        code=code,
        user=request.auth,
    )
    return 204, None