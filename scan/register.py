import cv2
import face_recognition
import json

# ฟังก์ชันสำหรับการลงทะเบียนผู้เข้าร่วม
def register_attendee(name, frame):
    face_encodings = face_recognition.face_encodings(frame)
    if face_encodings:
        face_encoding = face_encodings[0]
        user_data = {
            'name': name,
            'face_encoding': face_encoding.tolist()
        }
        register_user(user_data)
        print(f"Registered {name} successfully!")

# ฟังก์ชันสำหรับการบันทึกข้อมูลผู้ใช้งาน
def register_user(user_data):
    with open('registered_users.json', 'a') as f:
        json.dump(user_data, f)
        f.write('\n')

# เปิดกล้องสำหรับการลงทะเบียน
video_capture = cv2.VideoCapture(0)
name = input("Enter the name of the attendee: ")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # แสดงภาพจากกล้อง
    cv2.imshow('Video - Press "s" to save', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        register_attendee(name, frame)
        break

# ปิดการเชื่อมต่อกล้อง
video_capture.release()
cv2.destroyAllWindows()
