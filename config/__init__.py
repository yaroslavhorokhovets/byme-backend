import os

from pydantic import BaseSettings


if os.environ.get("VM_TYPE") == "TEST":
    env_file = "test.env"
    root_path = "/be/"
elif os.environ.get("VM_TYPE") == "PRODUCT":
    env_file = "product.env"
    root_path = "/be/"
else:
    env_file = "local.env"
    root_path = ""

class Settings(BaseSettings):
    AWS_SERVER_PUBLIC_KEY: str
    AWS_SERVER_SECRET_KEY: str
    MONGO_URI: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_DAY: str
    S3_BUCKET_NAME: str
    BYME_HOME: str

    class Config:
        env_file = env_file
        env_file_encoding = 'utf-8'


settings = Settings(_env_file=env_file, _env_file_encoding='utf-8')
