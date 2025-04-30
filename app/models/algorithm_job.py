from datetime import datetime

from sqlalchemy import Column, TIMESTAMP, TEXT, text
from sqlmodel import Field, SQLModel


# algorithm job table
class AlgorithmJob(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  # 作业ID
    task_name: str  # 任务名称
    sensor_id: str  # 传感器编号
    status: int = Field(default=0)  # 0:待运行 1:运行中 2:成功 3:失败 4:取消
    message: str = Field(sa_column=Column(TEXT))  # 原因
    created_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        ))
    updated_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
            server_onupdate=text("CURRENT_TIMESTAMP"),
        ))
