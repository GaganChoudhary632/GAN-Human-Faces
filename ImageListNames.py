import os

folder = "Images"  # change if needed
files = os.listdir(folder)

with open("image_list.txt", "w") as f:
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            f.write(file + "\n")

print("image_list.txt created with", len(files), "files.")
