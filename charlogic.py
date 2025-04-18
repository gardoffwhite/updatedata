
import json

# Dummy in-memory data for demonstration
characters = {
    "GmEvent": {
        "lv": "300",
        "exp": "1279",
        "eclv": "150",
        "ecexp": "31",
        "str": "0",
        "lvpoint": "9",
        "dex": "0",
        "skpoint": "192",
        "esp": "13000",
        "lic": "6",
        "spt": "13000",
        "money": "996571000",
        "int": "200",
        "bankmoney": "0",
        "cmap": "1",
        "hero": "1",
        "x": "7130",
        "y": "0",
        "z": "8130"
    }
}

def get_character(charname):
    return characters.get(charname)

def update_character(charname, new_data):
    if charname in characters:
        characters[charname].update(new_data)
        return True
    return False
