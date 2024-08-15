# Face Recognition

The goal of this project is to be able to input and recognise faces.

# Installation

Install requirements with 
`sudo pip install -r requirements.txt --break-system-packages`
Alternatively setting up a virtual environment and using `sudo pip install -r requirements.txt` is recommended.

When running on Windows, you might need to clone the [face_recognition_models](https://github.com/ageitgey/face_recognition_models) and put into a folder called **face_recognition_models** for the `face_recognition` library to work.

In order to run with discord notifications please create a bot and save the token to a file called secretkey.txt in the directory.

# Configuration

In `main_withdc.py` and `take_pic.py`, you can find the configuration variables, such as cam index and window dimensions at the top of each file.

# Usage

## Enrollment
To allow your guests to be recognised when they come to your door they must first be enrolled into the system.
This is done by taking pictures using `headshots.py` with a connected camera which will take many different angles of the guest's face to build a biometric profile of the guest.

To begin the proccess open terminal and run `python headshots.py`.
Press **space** to take a picture. Do this **at least 5 times** positioning your head at different angles each time. You can do this as many times as you like to improve your chances of recognition.
When you are finished, press **Esc** to build your biometric profile.
When this is complete the program will exit and you will be ready to sign in with face recognition.
_________________________________________________
Run `python train_model.py` to format the data for the code to use.

## Recognition
When you are expecting your enrolled guest open terminal once more and run `python main_withdc.py`.
Leave this in the background and continue on with your work.

When your guest arrives they just need to look at the camera and you will recieve a notification via the [Facerecognition discord](https://discord.gg/YVC8CTpg).









