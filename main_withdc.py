"""This runs main and outputs it to discord"""
import os
import sys
import pickle
import time
import logging
import datetime
import cv2
import face_recognition
import discord
import functions

# Logging levels affect many dependencies as well as current script.
# Change the verbosity of logs by changing the level to one of the following:
# CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
# Whatever level is set, that level and all levels more severe it will be logged.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CAMINDEX = 0
SAVE_FILE = "encodings.pickle"
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONTSCALE = 1
TEXTCOLOUR = (255, 0, 0)
TOLERANCE = 0.4
REPORT_UNKNOWNS = False
REPORT_NONE = False
SHOW_BOXES = True

if not os.path.exists(SAVE_FILE):
    data = {"encodings":[],"names":[]}
    logger.info("No encoding file exists running face detection only")
else:
    with open(SAVE_FILE, "rb") as f:
        data = pickle.load(f)
    knownencodings = data["encodings"]
    names = data["names"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():# pylint: disable=too-many-locals,too-many-branches,too-many-statements
    ''' runs the face recognition here'''
    prevmessage = ""
    logger.debug("%s logged in",client.user)

    cap = functions.camera_connection(CAMINDEX)
    logger.debug("Begin face detection...")
    while True:
        ret , frame = cap.read()
        if not ret:
            logger.info("couldnt get picture")
            sys.exit(1)

        boxes = face_recognition.face_locations(frame)
        encodings = face_recognition.face_encodings(frame, boxes)
        matches = []
        foundnames = []

        face_count = len(encodings)
        if face_count > 0:
            logger.debug("Faces detected: %s" , str(face_count))
        else:
            # No face detected, so save some CPU cycles
            time.sleep(0.01)

        for facenum,encoding in enumerate(encodings):
            matches = face_recognition.compare_faces(knownencodings,encoding, tolerance = TOLERANCE)
            logger.debug("Matches %s",matches)
            if not matches:
                for i in boxes:
                    matches.append(False)
            found = "Unknown"
            for matchnum,i in enumerate(matches):
                top,right,bottom,left = boxes[facenum]
                cv2.rectangle(frame, (left,top), (right,bottom) , (0,255,0), 4)

                if i:
                    found = names[matchnum]
                    if SHOW_BOXES:
                        frame = cv2.putText(frame, found, (left-20,top-20), FONT, FONTSCALE,
                        TEXTCOLOUR, 1, cv2.LINE_AA, False)
                elif True not in matches:
                    if SHOW_BOXES:
                        frame = cv2.putText(frame, "Unknown", (left-20,top-20), FONT, FONTSCALE,
                        TEXTCOLOUR, 1, cv2.LINE_AA, False)

            foundnames.append(found)
            if not REPORT_UNKNOWNS:
                foundnames = functions.removevalue(foundnames,"Unknown")
                
        logger.debug("Found: %s",foundnames)
        empty = True
        if len(foundnames) == 0:
            message = "No one"
            if not REPORT_NONE:
                prevmessage = ""

        else:
            message = foundnames[0]
            empty = False
            if len(foundnames) > 1:
                for i in foundnames:
                    message = message+f" And {i}"

        if prevmessage != foundnames:
            if (not REPORT_NONE and len(foundnames) > 0) or (REPORT_NONE):
                prevmessage = foundnames
            if (empty and REPORT_NONE) or not empty:
                date_time = datetime.datetime.now().strftime("%H:%M")
                await send_msg(f"{message} has arrived at the door at {date_time}.")
                
        cv2.imshow("window",frame) #remove once discord prints
        if cv2.waitKey(1) == ord("q"):
            logger.info("Q pressed. Exiting...")
            break
        time.sleep(0.1)

    cv2.destroyAllWindows()
    sys.exit()

@client.event
async  def on_message(message):
    '''reads messages from discord'''
    if not message.author.bot:
        logger.debug("recieved %s", message.content)

@client.event
async def send_msg(content="test",  channel = 1273223262213505058):
    '''outputs messages to discord'''
    channel = client.get_channel(channel)
    await channel.send(str(content))
with open("secretkey.txt", encoding ="utf-8") as f:
    key = f.read()

client.run(key)
