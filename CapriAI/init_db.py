from Database import Base, engine

from Models.Course import Course
from Models.Task import Task
from Models.TaskTestCase import TaskTestCase
from Models.User import User

Base.metadata.create_all(engine)

print("Database initialized!")