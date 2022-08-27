import subprocess
from pathlib import Path
from tkinter.filedialog import askdirectory

conda_env_dir = Path("C:/Users/Viz3/Anaconda/envs/cellpose")

print("Please choose directory for images.")
image_dir = Path(askdirectory())
print("Please choose directory to save masks.")
save_dir = Path(askdirectory())

for file in image_dir.glob("*.tif"):
    subprocess.run(['python -m cellpose',
                    '--dir',  str(file.absolute()),
                    '--pretrained_model cyto',
                    '--use_gpu',
                    '--save_tif'])

