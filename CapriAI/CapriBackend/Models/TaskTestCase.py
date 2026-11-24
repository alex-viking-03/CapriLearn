from sqlalchemy import Boolean, Integer, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from Database import Base

class TaskTestCase(Base):
    __tablename__ = "task_test_cases"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey("tasks.id"), nullable=False)
    input_data: Mapped[dict | list | str | int | float | bool] = mapped_column(JSON, nullable=False)
    expected_result: Mapped[dict | list | str | int | float | bool] = mapped_column(JSON, nullable=False)
    is_hidden: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)