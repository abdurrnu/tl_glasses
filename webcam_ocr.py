import cv2
from paddleocr import PaddleOCR
import argostranslate.package
import argostranslate.translate

if __name__ == "__main__":
    vidcap = cv2.VideoCapture(0)
    success, frame = vidcap.read()

    if success:
        print("webcam worked")

        #only english
        ocr = PaddleOCR(lang='japan')
        result = ocr.predict(frame)
        recognized_texts = result[0]['rec_texts']

        all_strings = []
        for text in recognized_texts:
            all_strings.append(text)

        final_result = " ".join(all_strings)
        print("\nResult:")
        print(final_result)

        cv2.imshow("frame", frame)
        cv2.waitKey(3000)

        #temp, will need to add something for choosing langauge later
        from_code = "ja"
        to_code = "en"

        #argo installation
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = next(
            filter(
                lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
            )
        )
        argostranslate.package.install_from_path(package_to_install.download())

        #translation
        print("Translating")
        translation = argostranslate.translate.translate(final_result, from_code, to_code)
        print(translation)

    else:
        print("webcam failed.")

    vidcap.release()
    cv2.destroyAllWindows()
