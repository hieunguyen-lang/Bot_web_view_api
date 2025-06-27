from sqlalchemy import Column, Integer, String, DateTime, Text
from database import Base

class HoaDon(Base):
    __tablename__ = "thong_tin_hoa_don"

    id = Column(Integer, primary_key=True, index=True)
    thoi_gian = Column(DateTime, nullable=True)
    nguoi_gui = Column(String, nullable=True)
    ten_khach = Column(String, nullable=True)
    so_dien_thoai = Column(String, nullable=True)
    type_dao_rut = Column(String, nullable=True)
    ngan_hang = Column(String, nullable=True)
    ngay_giao_dich = Column(String, nullable=True)
    gio_giao_dich = Column(String, nullable=True)
    tong_so_tien = Column(String, nullable=True)
    so_the = Column(String, nullable=True)
    tid = Column(String, nullable=True)
    mid = Column(String, nullable=True)
    so_lo = Column(String, nullable=True)
    so_hoa_don = Column(String, nullable=True)
    ten_may_pos = Column(String, nullable=True)
    lich_canh_bao = Column(String, nullable=True)
    tien_phi = Column(String, nullable=True)
    batch_id = Column(String, nullable=True)
    caption_goc = Column(Text, nullable=True)
    # Các trường bổ sung
    ket_toan = Column(String, nullable=True)
    phi_pos = Column(String, nullable=True)
    phi_thu_khach = Column(String, nullable=True)
    ck_khach_rut = Column(String, nullable=True)
    tien_ve_tk_cty = Column(String, nullable=True)
    tinh_trang = Column(String, nullable=True)
    lenh_treo = Column(String, nullable=True)
    ly_do = Column(String, nullable=True) 