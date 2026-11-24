from fastapi import FastAPI

from Controllers import (CapriController, 
                         TaskController, 
                         CourseController, 
                         TaskTestCaseController, 
                         UserController,
                         AdminController)

app = FastAPI(
    title = "Capri API",
    description = "Backend and AI engine for Capri",
    version = "0.1.0"
)

app.include_router(CapriController.router)
app.include_router(TaskController.router)
app.include_router(CourseController.router)
app.include_router(TaskTestCaseController.router)
app.include_router(UserController.router)
app.include_router(AdminController.router)