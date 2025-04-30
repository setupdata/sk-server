from fastapi import FastAPI

from app.api.main import api_router
from app.core.config import settings
from ray import serve, init

# fastapi
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@serve.deployment
@serve.ingress(app)
class FastAPIWrapper:
    pass

# ray
init(dashboard_host="0.0.0.0")

serve.start(http_options={"host": "0.0.0.0"})

serve.run(FastAPIWrapper.bind(), route_prefix="/", blocking=True)
