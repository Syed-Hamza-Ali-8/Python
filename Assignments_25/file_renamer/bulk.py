import os

def bulk_rename(folder_path, prefix="", suffix="", new_extension=None):
    try:
        files = os.listdir(folder_path)
        
        for filename in files:
            file_path = os.path.join(folder_path, filename)
            
            if os.path.isfile(file_path):
                name, ext = os.path.splitext(filename)
                
                ext = new_extension if new_extension else ext
                
                new_name = f"{prefix}{suffix}{ext}"
                new_path = os.path.join(folder_path, new_name)
                
                os.rename(file_path, new_path)
                print(f"Renamed: {filename} → {new_name}")

        print("✅ All files renamed successfully!")

    except Exception as e:
        print("❌ Error occurred:", e)

folder = input("Enter folder path: ")
prefix = input("Enter prefix (leave blank for none): ")
suffix = input("Enter suffix (leave blank for none): ")
ext = input("Enter new extension (e.g., .txt) or leave blank to keep original: ")
ext = ext if ext.startswith('.') else f".{ext}" if ext else None

bulk_rename(folder, prefix, suffix, ext)
