import cv2
import argostranslate.package
import argostranslate.translate
from webcam_ocr import webcam_ocr

language_dict = {
    "english": {
        "paddle": "en", 
        "argos": "en"
    },
    "japanese": {
        "paddle": "japan",
        "argos": "ja"
    },
    "chinese": {
        "paddle": "ch",
        "argos": "zh"
    },
    "spanish": {
        "paddle": "es",
        "argos": "es"
    }
}
available_langs = ", ".join(language_dict.keys())

if __name__ == "__main__":
    
    source_lang = input(f"Enter source language ({available_langs}): ").lower()
    target_lang = input(f"Enter target language ({available_langs}): ").lower()
    if source_lang not in language_dict or target_lang not in language_dict:
        print("Language not supported")
        exit()

    final_result, frame = webcam_ocr(language_dict[source_lang]["paddle"])

    if final_result is not None:
        print("\nResult:")
        print(final_result)

        cv2.imshow("frame", frame)
        cv2.waitKey(5000)

        # todo
        # will need to add a mechanism for choosing langauge later
        from_code = language_dict[source_lang]["argos"]
        to_code = language_dict[target_lang]["argos"]

        # argo installation
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = next(
            filter(
                lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
            )
        )
        argostranslate.package.install_from_path(package_to_install.download())

        # translation
        print("Translating")
        translation = argostranslate.translate.translate(final_result, from_code, to_code)
        print(translation)

    cv2.destroyAllWindows()