from fastapi import APIRouter
from app.models.service_model import Service
from app.models.service_schema import ServiceCreate
from app.database.db import SessionLocal

router = APIRouter()

@router.get("/")
def home():
    return {"message": "CloudLite Monitor API running"}

@router.post("/services")
def create_service(service: ServiceCreate):
    db = SessionLocal()

    new_service = Service(
        name=service.name,
        url=service.url,
        status=service.status
    )

    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return new_service


@router.get("/services")
def list_services():
    db = SessionLocal()
    services = db.query(Service).all()
    return services 

@router.delete("/services/{service_id}")
def delete_service(service_id: int):
    db = SessionLocal()

    service = db.query(Service).filter(Service.id == service_id).first()

    if not service:
        return {"error": "Service not found"}

    db.delete(service)
    db.commit()

    return {"message": "Service deleted"}       

@router.put("/services/{service_id}")
def update_service(service_id: int, updated_data: ServiceCreate):
    db = SessionLocal()

    service = db.query(Service).filter(Service.id == service_id).first()

    if not service:
        return {"error": "Service not found"}

    service.name = updated_data.name
    service.url = updated_data.url
    service.status = updated_data.status

    db.commit()
    db.refresh(service)

    return service

