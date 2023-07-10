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


def preprocessing_color(image: str) -> str:
    """
    画像の前処理をする。カラーで出力
    Args:
        image : 前処理する画像(ndarray)
    """
    # 適用的ヒストグラム平坦化（CLAHE）
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    lab_planes = cv2.split(lab_image)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_planes = [clahe.apply(plane) for plane in lab_planes]
    clahe_image = cv2.merge(clahe_planes)
    clahe_image = cv2.cvtColor(clahe_image, cv2.COLOR_LAB2BGR)

    return clahe_image


def preprocessing_gray(image: str) -> str:
    """
    画像の前処理をする。グレースケールで出力。
    Args:
        image : 前処理する画像(ndarray)
    """
    # 適用的ヒストグラム平坦化（CLAHE）
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(gray_image)
    clahe_image = cv2.cvtColor(clahe_image, cv2.COLOR_GRAY2BGR)

    return clahe_image


def emotion_estimate(base64_data: str) -> str:
    """
    画像から感情推定する
    Args:
        base64_data : 感情推定する画像(base64)
    """
    # バイナリーデータをndarrayに変換
    emo_detector = FER(mtcnn=True)
    image = convert_to_ndarray(base64_data)
    clahe_image = preprocessing_color(image)
    # clahe_image = preprocessing_gray(image)
    captured_emotions = emo_detector.detect_emotions(clahe_image)
    # cv2.imwrite("data/clahe_image2.jpeg", clahe_image)
    if len(captured_emotions) == 0:
        return None

    return captured_emotions[0]["emotions"]


if __name__ == "__main__":
    dst_path = "data/baby_sad.jpeg"
    with open(dst_path, "rb") as image_file:
        data = base64.b64encode(image_file.read())
    print(emotion_estimate(data))
