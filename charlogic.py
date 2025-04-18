# charlogic.py

# ฐานข้อมูลตัวละครจำลอง
characters_db = {
    "GmEvent": {"lv": 300, "exp": 1279, "str": 0, "dex": 0},
    # สามารถเพิ่มตัวละครอื่นๆ ได้ที่นี่
}

def get_character(charname: str):
    """ดึงข้อมูลตัวละครจากฐานข้อมูลโดยใช้ charname"""
    return characters_db.get(charname)

def update_character(charname: str, new_data: dict):
    """อัปเดตข้อมูลตัวละครในฐานข้อมูล"""
    if charname in characters_db:
        characters_db[charname].update(new_data)
        return True
    return False

def change_charname_for_search(old_name: str, new_name: str):
    """ เปลี่ยนชื่อในการค้นหา แต่ไม่กระทบกับฐานข้อมูล """
    if old_name in characters_db:
        # เปลี่ยนแค่ชื่อที่ใช้ในการค้นหา ไม่เปลี่ยนในฐานข้อมูล
        characters_db[new_name] = characters_db.pop(old_name)
        return True
    return False
