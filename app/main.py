from fastapi import FastAPI
from app.database import engine, Base
from app.routes import courses

# Cria tabelas no PostgreSQL automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar rotas
app.include_router(courses.router, prefix="/courses", tags=["Courses"])

@app.get("/")
def root():
    return {"message": "API funcionando, minha rainha!"}
