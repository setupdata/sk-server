from app.models import AlgorithmJob
from sqlmodel import Session, select

from app.core.db import engine


def create_job(task_name: str, sensor_id: str, status: int) -> AlgorithmJob:
    job = AlgorithmJob(task_name=task_name, sensor_id=sensor_id, status=status)

    with Session(engine) as session:
        session.add(job)
        session.commit()
        session.refresh(job)

    return job

def update_job_state(job_id: int, status: int, message: str) -> None:
    with Session(engine) as session:
        statement = select(AlgorithmJob).where(AlgorithmJob.id == job_id)
        results = session.exec(statement)
        job = results.one()

        job.state = status
        job.message = message

        session.commit()

    return