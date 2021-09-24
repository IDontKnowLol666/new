import face_recognition
import cv2
import numpy as np
import datetime
import pygame.mixer as mix
from message import message
# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from timezone import timezone as time, data


mail_content = ("Hello someone had appeared on the camera at, " + time + message)

#The mail addresses and password
sender_address = 'spinoshit@gmail.com'
sender_pass = 'B00fu123'
receiver_address = 'jolene5652@gmail.com'

# Setup the MIME
# message = MIMEMultipart()
# message['From'] = sender_address
# message['To'] = receiver_address
# message['Subject'] = 'Person Detected.'   #The subject line
# The body and the attachments for the mail
# message.attach(MIMEText(mail_content, 'plain'))

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
jolene_image = face_recognition.load_image_file("mebasically.png")
jolene_face_encoding = face_recognition.face_encodings(jolene_image)[0]

# Load a second sample picture and learn how to recognize it.
dad_image = face_recognition.load_image_file("dad.JPG")
dad_face_encoding = face_recognition.face_encodings(dad_image)[0]

mom_image = face_recognition.load_image_file("mom.jpg")
mom_face_encoding = face_recognition.face_encodings(mom_image)[0]

christine_image = face_recognition.load_image_file("christine1.jpg")
christine_face_encoding = face_recognition.face_encodings(christine_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    jolene_face_encoding,
    dad_face_encoding,
    mom_face_encoding,
    christine_face_encoding
]
known_face_names = [
    "Jolene",
    "Dad",
    "Mom",
    "Christine"
]

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"
        center_coordinates = top + right // 2, bottom + left // 2
        radius = top // 2  # or can be h / 2 or can be anything based on your requirements

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)


        def round_seconds(obj: time):
            if obj.microsecond >= 500_000:
                obj += datetime.timedelta(seconds=1)
            return obj.replace(microsecond=0)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            if name != 'w':
                mix.init()
                mix.music.load('annoyingashell.wav')
                mix.music.play()
                #engine.say("I see you" + name)
                #engine.runAndWait()
                #engine.stop()

                message = MIMEMultipart()
                message['From'] = sender_address
                message['To'] = receiver_address
                message['Subject'] = 'Person Detected ' + str(name) + "(" + data + ")"# The subject line
                # The body and the attachments for the mail
                message.attach(MIMEText(mail_content, 'plain'))
                # send message
                session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
                session.starttls()  # enable security
                session.login(sender_address, sender_pass)  # login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                session.quit()
                print('Mail Sent')





        # Draw a box around the face
        #cv2.rectangle(frame, (left, top - 50), (right, bottom + 55), (0, 255, 255), 2)

        cv2.rectangle(frame, (left - 10 , top - 50), (right + 10, bottom + 55), (0, 0, 255), 2)
        # Draw a label with a name below the face
        #cv2.rectangle(frame, (left, bottom), (right, bottom), (0, 255, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(frame, name, (left + 20, bottom), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
