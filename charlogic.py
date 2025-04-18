# ตัวอย่างของฟังก์ชันที่ใช้ในการดึงข้อมูลและอัปเดตข้อมูลตัวละคร

# ตัวแปรเก็บข้อมูลตัวละคร
characters_db = {
    "GmEvent": {"lv": 300, "exp": 1279, "str": 0, "dex": 0},
    # เพิ่มข้อมูลตัวละครอื่นๆ ที่นี่
}

def get_character(charname: str):
    """ดึงข้อมูลตัวละครจากฐานข้อมูล"""
    return characters_db.get(charname)

def update_character(charname: str, new_data: dict):
    """อัปเดตข้อมูลตัวละครในฐานข้อมูล"""
    if charname in characters_db:
        characters_db[charname].update(new_data)
        return True
    return False
