# Face Recognition

The goal of this project is to be able to input and recognise faces.

# Installation

Install requirements with 
`sudo pip install -r requirements.txt --break-system-packages`
Alternatively setting up a virtual environment and using `sudo pip install -r requirements.txt` is recommended.

# Usage

Run `python main.py` to detect faces once all other steps have been done.

In both files change the CAMINDEX to be the index of camera you are using.

Create a folder called dataset in here you then make more folders named after each user.
Run `python headshots.py` to compile a document of images in the file replace the value in name with the name of the person added and the folder.

Run `python train_model.py` to format the data for the code to use.


