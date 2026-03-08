from fastapi import FastAPI
from routes.upload_report import router as upload_router
from routes.patient_history import router as history_router

app = FastAPI(title="Doctor AI Bot")

app.include_router(upload_router)
app.include_router(history_router)

@app.get("/")
def home():
    return {"message": "Doctor AI Bot Running"}