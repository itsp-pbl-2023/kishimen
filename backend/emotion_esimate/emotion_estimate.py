from fer import FER
import matplotlib.pyplot as plt

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
    # cv2.imshow("test", frame)
    cv2.imwrite(dst_path, frame)


def emotion_estimate(image: str) -> None:
    """
    画像から感情推定する
    Args:
        image : 感情推定する画像のパス
    """
    test_image_one = plt.imread(image)
    emo_detector = FER(mtcnn=True)
    # Capture all the emotions on the image
    captured_emotions = emo_detector.detect_emotions(test_image_one)
    # Print all captured emotions with the image
    print(captured_emotions)
    plt.imshow(test_image_one)

    dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
    print(dominant_emotion, emotion_score)


if __name__ == "__main__":
    dst_path = "data/test.jpeg"
    capture_image(dst_path)
    emotion_estimate(dst_path)
