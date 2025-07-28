import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# load known faces
vishvas_image = face_recognition.load_image_file("faces/vishvas.jpg")
vishvas_encoding = face_recognition.face_encodings(vishvas_image)[0]

chris_image = face_recognition.load_image_file("faces/chris.jpeg")
chris_encoding = face_recognition.face_encodings(chris_image)[0]

ryan_image = face_recognition.load_image_file("faces/ryan.jpeg")
ryan_encoding = face_recognition.face_encodings(ryan_image)[0]

known_face_encodings = [vishvas_encoding, chris_encoding, ryan_encoding]
known_face_names = ["Vishvas", "Chris", "Ryan"]

# list of expected students

students = known_face_names.copy()
face_locations = []
face_encodings = []

# get current date and time

now = datetime.now()
current_date = now.strftime("%m-%d-%y")

# csv writer
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)
    # Convert the Frame to RGB
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    #  Find Face Locations and Encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Compare Detected Faces with Known Faces
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if (matches[best_match_index]):
            name = known_face_names[best_match_index]

        # Add text if person present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_COMPLEX
            bottemLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " is present", bottemLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M%S")
                lnwriter.writerow([name, current_time])

    # show image
    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# free camera
video_capture.release()
# destroy al windows
cv2.destroyAllWindows()
f.close()


