import strawberry


@strawberry.type
class PropertyIngestionResponse:
    message: str
    code: int
