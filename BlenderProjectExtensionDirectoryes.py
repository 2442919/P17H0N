import os

def create_blender_project_directories(project_name):
    # Define lista extensiilor comune utilizate în proiectele Blender
    extensions = [
        "blend",  # Fișiere Blender principale
        "obj",    # Obiecte 3D exportate
        "fbx",    # Fișiere pentru schimb de modele
        "png",    # Texturi sau randări
        "jpg",    # Imagini texturi sau referință
        "tiff",   # Imagini de înaltă calitate
        "exr",    # Fișiere HDR pentru iluminare
        "mp4",    # Videoclipuri randate
        "wav",    # Fișiere audio
        "scripts" # Scripturi Python folosite în Blender
    ]

    # Creează directorul principal pentru proiect
    root_dir = os.path.join(os.getcwd(), project_name)
    os.makedirs(root_dir, exist_ok=True)
    print(f"Directorul principal creat: {root_dir}")

    # Creează subdirectoare pentru fiecare tip de fișier
    for ext in extensions:
        if ext == "scripts":
            sub_dir = os.path.join(root_dir, "scripts")  # Director special pentru scripturi
        else:
            sub_dir = os.path.join(root_dir, f"{ext}_files")
        os.makedirs(sub_dir, exist_ok=True)
        print(f"Subdirector creat: {sub_dir}")

# Exemplu de utilizare
if __name__ == "__main__":
    project_name = input("Introdu numele proiectului Blender: ").strip()
    create_blender_project_directories(project_name)
