from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import SessionLocal, engine, Base
from collections import defaultdict

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Cho phép CORS cho mọi origin (dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/hoa-don")
def get_hoa_don_grouped(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1),
    db: Session = Depends(get_db)
):
    batch_ids_query = db.query(models.HoaDon.batch_id).distinct()
    total = batch_ids_query.count()
    batch_ids = (
        batch_ids_query
        .order_by(models.HoaDon.batch_id)
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )
    batch_ids = [b[0] for b in batch_ids]

    records = (
        db.query(models.HoaDon)
        .filter(models.HoaDon.batch_id.in_(batch_ids))
        .all()
    )

    grouped = defaultdict(list)
    for r in records:
        grouped[r.batch_id].append(schemas.HoaDonOut.from_orm(r))

    data = [
        {"batch_id": batch_id, "records": grouped[batch_id]}
        for batch_id in batch_ids
    ]
    return {"total": total, "data": data}

@app.post("/api/hoa-don", response_model=schemas.HoaDonOut)
def create_hoa_don(hoa_don: schemas.HoaDonCreate, db: Session = Depends(get_db)):
    db_hoa_don = models.HoaDon(**hoa_don.dict())
    db.add(db_hoa_don)
    db.commit()
    db.refresh(db_hoa_don)
    return db_hoa_don

@app.put("/api/hoa-don/{hoa_don_id}", response_model=schemas.HoaDonOut)
def update_hoa_don(hoa_don_id: int, hoa_don: schemas.HoaDonUpdate, db: Session = Depends(get_db)):
    db_hoa_don = db.query(models.HoaDon).filter(models.HoaDon.id == hoa_don_id).first()
    if not db_hoa_don:
        raise HTTPException(status_code=404, detail="Hóa đơn không tồn tại")
    for k, v in hoa_don.dict(exclude_unset=True).items():
        setattr(db_hoa_don, k, v)
    db.commit()
    db.refresh(db_hoa_don)
    return db_hoa_don

@app.delete("/api/hoa-don/{hoa_don_id}")
def delete_hoa_don(hoa_don_id: int, db: Session = Depends(get_db)):
    db_hoa_don = db.query(models.HoaDon).filter(models.HoaDon.id == hoa_don_id).first()
    if not db_hoa_don:
        raise HTTPException(status_code=404, detail="Hóa đơn không tồn tại")
    db.delete(db_hoa_don)
    db.commit()
    return {"ok": True} 