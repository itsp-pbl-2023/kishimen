import base64
from typing import Any
from fer import FER
import numpy as np
import cv2


def capture_image(dst_path: str) -> None:
    """
    OpenCVを用いて、カメラで画像をキャプチャ
    Args:
        dst_path : 画像の出力パス
    """
    deviceid = 0  # it depends on the order of USB connection.
    capture = cv2.VideoCapture(deviceid)

    ret, frame = capture.read()
    cv2.imwrite(dst_path, frame)


def convert_to_ndarray(base64_data: str) -> Any:
    """
    base64をデコードし、そのバイナリーデータをndarray型に変換する
    """
    png_bytes = base64.b64decode(base64_data)
    image_ndarray = np.frombuffer(png_bytes, dtype=np.uint8)
    img = cv2.imdecode(image_ndarray, flags=cv2.IMREAD_COLOR)
    return img


def emotion_estimate(base64_data: str) -> str:
    """
    画像から感情推定する
    Args:
        image : 感情推定する画像のパス
    """
    # バイナリーデータをndarrayに変換
    emo_detector = FER(mtcnn=True)
    image = convert_to_ndarray(base64_data)
    captured_emotions = emo_detector.detect_emotions(image)
    print(captured_emotions)
    if len(captured_emotions) == 0:
        return None

    return captured_emotions[0]["emotions"]


if __name__ == "__main__":
    dst_path = "data/test.jpeg"
    capture_image(dst_path)
    emotion_estimate(dst_path)
