# original code

# import cv2
# import time
# import numpy as np
# import HandTrackingModule as htm
# import math
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#
#
# ######################################
# wCam, hCam = 640, 480
#
# ######################################
#
# cap = cv2.VideoCapture(0)
# cap.set(3, wCam)
# cap.set(4, hCam)
# pTime = 0
#
# detector = htm.handDetector(detectionCon=0.7)
#
#
#
#
# # # device = AudioUtilities.GetSpeakers()
# # volume = device.EndpointVolume
# # # print(f"Audio output: {device.FriendlyName}")
# # # print(f"- Muted: {bool(volume.GetMute())}")
# # # print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
# # print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")
# # print(volume.GetVolumeRange())
# #
# # volume.SetMasterVolumeLevel(-20.0, None)
#
#
#
# # Inisialisasi Audio Device
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
#
# # Print volume range
# print(volume.GetVolumeRange())   # contoh: (-65.25, 0.0, 0.03125)
#
#
#
# while True:
#     success, img = cap.read()
#     img = detector.findHands(img)
#     lmList = detector.findPosition(img, draw=False)
#     if len(lmList) != 0:
#         # print(lmList[4], lmList[8])
#
#
#         x1, y1 = lmList[4][1], lmList[4][2]
#         x2, y2 = lmList[8][1], lmList[8][2]
#         cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
#
#
#         cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
#         cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
#         cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
#         cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
#
#
#         length = math.hypot(x2 - x1, y2 - y1)
#         print(length)
#
#         if length<50:
#             cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
#
#     cTime = time.time()
#     fps = 1 / (cTime - pTime)
#     pTime = cTime
#
#     cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1,(255,0,0), 3)
#
#     cv2.imshow("Img", img)
#     cv2.waitKey(1)
#







# original code





# -----------------------------------------------------------------------------------------------------------------








# import os
# import absl.logging
# absl.logging.set_verbosity(absl.logging.ERROR)
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#
# import cv2
# import time
# import numpy as np
# import HandTrackingModule as htm
# import math
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#
#
# ######################################
# wCam, hCam = 640, 480
# ######################################
#
# cap = cv2.VideoCapture(0)
# cap.set(3, wCam)
# cap.set(4, hCam)
# pTime = 0
#
# detector = htm.handDetector(detectionCon=0.7)
#
# # Inisialisasi Audio Device
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
#
# # Print volume range (dB)
# print("Volume range (dB):", volume.GetVolumeRange())   # contoh: (-65.25, 0.0, 0.03125)
#
# while True:
#     success, img = cap.read()
#     img = detector.findHands(img)
#     lmList = detector.findPosition(img, draw=False)
#     if len(lmList) != 0:
#         x1, y1 = lmList[4][1], lmList[4][2]   # Jempol
#         x2, y2 = lmList[8][1], lmList[8][2]   # Telunjuk
#         cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
#
#         cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
#         cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
#         cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
#         cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
#
#         length = math.hypot(x2 - x1, y2 - y1)  # Jarak antara jari
#         # print(length)
#
#         # Mapping panjang jari ke skala volume 0.0 - 1.0
#         volScalar = np.interp(length, [30, 200], [0.0, 1.0])
#         volume.SetMasterVolumeLevelScalar(volScalar, None)
#
#         print(f"Jarak: {int(length)} | Volume: {round(volScalar, 2)}")
#
#         if length < 50:
#             cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
#
#     cTime = time.time()
#     fps = 1 / (cTime - pTime)
#     pTime = cTime
#
#     cv2.putText(img, f'FPS: {int(fps)}', (40, 50),
#                 cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
#
#     cv2.imshow("Img", img)
#     cv2.waitKey(1)

























import os
import absl.logging
absl.logging.set_verbosity(absl.logging.ERROR)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


######################################
wCam, hCam = 640, 480
######################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

# Inisialisasi Audio Device
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Print volume range (dB)
print("Volume range (dB):", volume.GetVolumeRange())   # contoh: (-65.25, 0.0, 0.03125)

volBar = 400   # posisi awal bar
volPer = 0     # persentase volume

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]   # Jempol
        x2, y2 = lmList[8][1], lmList[8][2]   # Telunjuk
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)  # Jarak jari
        # print(length)

        # Mapping panjang jari ke volume
        volScalar = np.interp(length, [30, 200], [0.0, 1.0])
        volume.SetMasterVolumeLevelScalar(volScalar, None)

        # Mapping ke indikator bar
        volBar = np.interp(length, [30, 200], [400, 150])   # y posisi bar
        volPer = np.interp(length, [30, 200], [0, 100])     # persentase

        print(f"Jarak: {int(length)} | Volume: {int(volPer)}%")

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    # Gambar volume bar
    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)  # outline
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)  # isi bar
    cv2.putText(img, f'{int(volPer)} %', (40, 450),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    # FPS counter
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (500, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
