import numpy as np

# ฟังก์ชันสำหรับการยืนยันการเข้าร่วม
def recognize_attendee(frame):
    face_encodings = face_recognition.face_encodings(frame)
    if face_encodings:
        face_encoding = face_encodings[0]
        ref = db.reference('users')
        users = ref.get()
        for user_id, user_data in users.items():
            stored_face_encoding = np.array(user_data['face_encoding'])
            matches = face_recognition.compare_faces([stored_face_encoding], face_encoding)
            if matches[0]:
                print(f"Recognized {user_data['name']}")
                return user_data['name']
    return None

# เปิดกล้องสำหรับการจดจำใบหน้า
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # ตรวจจับใบหน้าและยืนยันการเข้าร่วม
    name = recognize_attendee(frame)
    if name:
        print(f"{name} is attending the ceremony.")

    # แสดงภาพจากกล้อง
    cv2.imshow('Video - Press "q" to quit', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิดการเชื่อมต่อกล้อง
video_capture.release()
cv2.destroyAllWindows()
