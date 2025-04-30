from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "sk-server"
    API_V1_STR: str = "/api/v1"

    MYSQL_DSN: str = "mysql+mysqldb://root:123456@localhost/sk-server"

    VIBRATE_MODEL_BASE_PATH: str = "./models"


settings = Settings()  # type: ignore
