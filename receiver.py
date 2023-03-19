import cv2
import urllib.request

# MJPEGストリームのURL
stream_url = "http://localhost:5001/cam.mjpg"

# OpenCVのVideoCaptureオブジェクトを作成
cap = cv2.VideoCapture(stream_url)

while True:
    # MJPEGストリームからフレームを取得
    ret, frame = cap.read()

    if not ret:
        break

    # フレームを表示
    cv2.imshow('frame', frame)

    # 'q'キーでプログラムを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
cv2.destroyAllWindows()