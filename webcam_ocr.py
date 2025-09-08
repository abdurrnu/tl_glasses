import cv2
from paddleocr import PaddleOCR

def webcam_ocr(source_lang):
    vidcap = cv2.VideoCapture(0)
    success, frame = vidcap.read()

    final_result = None

    if success:
        print("webcam worked")
        
        ocr = PaddleOCR(lang=source_lang)
        result = ocr.predict(frame)
        recognized_texts = result[0]['rec_texts']

        all_strings = []
        for text in recognized_texts:
            all_strings.append(text)

        final_result = " ".join(all_strings)

    else:
        print("webcam failed.")

    vidcap.release()
    return final_result, frame