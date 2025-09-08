import cv2
from paddleocr import PaddleOCR

if __name__ == "__main__":
    vidcap = cv2.VideoCapture(0)
    success, frame = vidcap.read()

    if success:
        print("webcam worked")

        #only english
        ocr = PaddleOCR(lang='en')
        result = ocr.predict(frame)
        recognized_texts = result[0]['rec_texts']

        all_strings = []
        for text in recognized_texts:
            all_strings.append(text)

        final_result = " ".join(all_strings)
        print("\nResult:")
        print(final_result)

        cv2.imshow("frame", frame)
        cv2.waitKey(0)
    else:
        print("webcam failed.")

    vidcap.release()
    cv2.destroyAllWindows()
