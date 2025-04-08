import shutil

# Use the correct directory path for macOS (e.g., "/")
total, used, free = shutil.disk_usage("/")

print(f"Total: {total // (2**30)} GiB")
print(f"Used: {used // (2**30)} GiB")
print(f"Free: {free // (2**30)} GiB")