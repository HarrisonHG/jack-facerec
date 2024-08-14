"""This runs main and outputs it to discord"""
import os
import sys
import pickle
import time
import datetime
import cv2
import face_recognition
import discord
import functions

CAMINDEX = 0
SAVE_FILE = "encodings.pickle"
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONTSCALE = 1
TEXTCOLOUR = (255, 0, 0)
TOLERANCE = 0.4
if not os.path.exists(SAVE_FILE):
    data = {"encodings":[],"names":[]}
    print("No encoding file exists running face detection only")
else:
    with open(SAVE_FILE, "rb") as f:
        data = pickle.load(f)
    Knownencodings = data["encodings"]
    names = data["names"]


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():# pylint: disable=too-many-locals,too-many-branches
    ''' runs the face recognition here'''
    prevmessage = ""
    print(f"{client.user} logged in")

    cap = functions.camera_connection(CAMINDEX)

    while True:
        ret , frame = cap.read()
        if not ret:
            print("couldnt get picture")
            sys.exit(1)

        boxes = face_recognition.face_locations(frame)
        encodings = face_recognition.face_encodings(frame, boxes)
        matches = []
        foundnames = []
        for facenum,encoding in enumerate(encodings):
            matches = face_recognition.compare_faces(Knownencodings,encoding, tolerance = TOLERANCE)
            #print(matches)
            if not matches:
                for i in boxes:
                    matches.append(False)
            found = "Unknown"
            for matchnum,i in enumerate(matches):
                top,right,bottom,left = boxes[facenum]
                cv2.rectangle(frame, (left,top), (right,bottom) , (0,255,0), 4)
                
                if i:
                    found = names[matchnum]
                    frame = cv2.putText(frame, found, (left-20,top-20), FONT, FONTSCALE,
                    TEXTCOLOUR, 1, cv2.LINE_AA, False)
                elif True not in matches:
                    frame = cv2.putText(frame, "Unknown", (left-20,top-20), FONT, FONTSCALE,
                    TEXTCOLOUR, 1, cv2.LINE_AA, False)
            foundnames.append(found)

        #print("Found:",foundnames)#
        if len(foundnames) == 0:
            message = "No one"
        elif len(foundnames) == 1:
            message = foundnames[0]
        else:
            message = foundnames[0]
            for i in foundnames:
                message = message+f" And {i}"
        if prevmessage != message:
            prevmessage = message
            message = message + " "+str(datetime.datetime.now())
            await send_msg(f"Found {message}")
        cv2.imshow("window",frame)
        if cv2.waitKey(1) == ord("q"):
            break
        time.sleep(0.1)

    cv2.destroyAllWindows()
    sys.exit()

@client.event
async  def on_message(message):
    '''reads messages from discord'''
    if not message.author.bot:
        print(f"recieved {message.content}")

@client.event
async def send_msg(content="test",  channel = 1273223262213505058):
    '''outputs messages to discord'''
    channel = client.get_channel(channel)
    await channel.send(str(content))
with open("secretkey.txt", encoding ="utf-8") as f:
    key = f.read()
client.run(key)
