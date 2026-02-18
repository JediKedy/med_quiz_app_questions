import os
import json
import hashlib

def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def generate():
    base_dir = "." # Sual fayllarının olduğu əsas qovluq
    metadata = {
        "last_update": "2025-05-20T15:00:00",
        "broadcast": {"id": 1, "message": "Xoş gəlmisiniz! Yeni suallar əlavə edildi."},
        "files": {}
    }

    # Bütün .json fayllarını skan et (banks.json daxil)
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".json") and file != "metadata.json":
                full_path = os.path.relpath(os.path.join(root, file), base_dir)
                # Windows-da yollar \ olur, onları GitHub üçün / edirik
                clean_path = full_path.replace("\\", "/")
                metadata["files"][clean_path] = get_file_hash(os.path.join(root, file))

    with open("metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)
    print("metadata.json uğurla yaradıldı!")

if __name__ == "__main__":
    generate()