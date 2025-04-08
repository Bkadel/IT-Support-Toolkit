import os
import shutil
import tempfile

temp_dir = tempfile.gettempdir()
deleted = 0

for root, dirs, files in os.walk(temp_dir):
    for file in files:
        try:
            os.remove(os.path.join(root, file))
            deleted += 1
        except:
            pass

print(f"Deleted {deleted} temporary files.")