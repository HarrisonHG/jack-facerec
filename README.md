# Face Recognition

The goal of this project is to be able to input and recognise faces.

# Installation

Install requirements with 
`sudo pip install -r requirements.txt --break-system-packages`
Alternatively setting up a virtual environment and using `sudo pip install -r requirements.txt` is recommended.

When running on Windows, you might need to clone the [face_recognition_models](https://github.com/ageitgey/face_recognition_models) and put into a folder called **face_recognition_models** for the `face_recognition` library to work.

# Configuration

In `main.py` and `take_pic.py`, change `CAMINDEX` to match the index of the camera according to your OS.
The default is **0**.

# Usage

Run `python main.py` to detect faces once all other steps have been done.

In both files change the CAMINDEX to be the index of camera you are using.

Run `python headshots.py` to compile a document of images in the file replace the value in name with the NAME of the person.

Run `python train_model.py` to format the data for the code to use.


