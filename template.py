import os
from pathlib import Path
import logging
from time import asctime


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s:%(levelname)s]:%(message)s"
    )

while True:
    projectname=input("Enter project name ")
    if projectname !='':
        break

logging.info(f"Creating project with name {projectname}")

list_files=[
    ".github/workflows/.gitkeep",
    f"src/{projectname}/__init__.py",
    "init_setup.sh",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "setup.py",
    "project.toml",
    "setup.cfg",
    "tox.ini",
    "requirements.txt",
    "requirements_dev.txt"
]

for filepath in list_files:
    filepath=Path(filepath)
    filedir , filename = os.path.split(filepath)
    if filedir!='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating file directory at {filedir}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating file {filename} at {filepath}")

    else:
        logging.info(f"file is already present at {filepath}")






