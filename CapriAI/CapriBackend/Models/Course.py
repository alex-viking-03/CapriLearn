from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLAlchemyEnum

from Database import Base
from Enums import ProgrammingLanguages

class Course(Base):
    __tablename__ = "courses"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    language: Mapped[ProgrammingLanguages.ProgrammingLanguage] = mapped_column(
        SQLAlchemyEnum(
            ProgrammingLanguages.ProgrammingLanguage,
            values_callable = lambda enum: [item.value for item in enum]
            ), 
        nullable=False
        )
    difficulty: Mapped[int] = mapped_column(Integer, nullable=False)
