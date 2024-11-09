import os
from pathlib import Path

import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s') 

list_of_files=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "experiments/trials.ipynb"
    
]

for filepath in list_of_files:
    filepath=Path(filepath)        #to convert file path as per os automatically
    dir,name=os.path.split(filepath)   # will rerun the name of file and folder in name and dir variables
    
    if dir !="":                               #checking if folder exists
        os.makedirs(dir,exist_ok=True)          # if not create directory
        logging.info(f"creating directory; {dir} for the file {name}")  # log the info
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):   # checking if file exists and no code is written in file if exists
        with open (filepath,"w") as f:   # if true creating file
            pass
            logging.info(f"Creating Empty file {filepath}")
        
    else :
        logging.info(f"File Already Exists {name}")  
    


# once you are satisfied go and execute this file.. Command : python template.py


