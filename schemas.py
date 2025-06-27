from pydantic import BaseModel
from typing import Optional

class HoaDonBase(BaseModel):
    thoi_gian: Optional[str] = None
    nguoi_gui: Optional[str] = None
    ten_khach: Optional[str] = None
    so_dien_thoai: Optional[str] = None
    type_dao_rut: Optional[str] = None
    ngan_hang: Optional[str] = None
    ngay_giao_dich: Optional[str] = None
    gio_giao_dich: Optional[str] = None
    tong_so_tien: Optional[str] = None
    so_the: Optional[str] = None
    tid: Optional[str] = None
    mid: Optional[str] = None
    so_lo: Optional[str] = None
    so_hoa_don: Optional[str] = None
    ten_may_pos: Optional[str] = None
    lich_canh_bao: Optional[str] = None
    tien_phi: Optional[str] = None
    batch_id: Optional[str] = None
    caption_goc: Optional[str] = None
    ket_toan: Optional[str] = None
    phi_pos: Optional[str] = None
    phi_thu_khach: Optional[str] = None
    ck_khach_rut: Optional[str] = None
    tien_ve_tk_cty: Optional[str] = None
    tinh_trang: Optional[str] = None
    lenh_treo: Optional[str] = None
    ly_do: Optional[str] = None

class HoaDonCreate(HoaDonBase):
    pass

class HoaDonUpdate(HoaDonBase):
    pass

class HoaDonOut(HoaDonBase):
    id: int
    class Config:
        from_attributes = True 