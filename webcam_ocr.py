import cv2
import pytesseract

if __name__ == "__main__":
    vidcap = cv2.VideoCapture(0)
    success, frame = vidcap.read()

    if success:
        print("webcam worked")
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        processed_image = cv2.adaptiveThreshold(
            gray_frame, 
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed_image, config=custom_config)
        
        if text.strip():
             print(text)
        else:
             print("ocr failed")

        cv2.imwrite("processed_image.png", processed_image)
        cv2.imshow("processed image", processed_image)
        cv2.waitKey(0)
    else:
        print("webcam failed.")

    vidcap.release()
    cv2.destroyAllWindows()