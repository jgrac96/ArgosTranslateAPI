"""
        from https://www.educative.io/blog/python-fastapi-tutorial
        https://github.com/argosopentech/argos-translate
    Date: 20/11/2022
    Translation API based off ArgosTranslate (offline)
"""
from fastapi import FastAPI, APIRouter
import argostranslate.package
import argostranslate.translate

# setup API
app = FastAPI(
    title="TranslationAPI - Wrapper for ArgosTranslate",
    openapi_url="/openapi.json"
)

# to be able to convert from input of API from Java to country codes needed by Argos Translate
languages = {"English":"EN", "German":"DE", "Italian":"IT", "French":"FR", "Spanish":"ES"}

# load packages
req = ["en_fr", "en_de", "en_es", "en_it", "fr_en", "de_en", "es_en", "it_en"]
for lang_package in req: argostranslate.package.install_from_path("translate-"+lang_package+"-1_0.argosmodel")

api_router = APIRouter()  # setup api router

@api_router.get("/")
def translate(source_lang: str, target_lang: str, word: str):
    try:
        source_lang = languages.get(source_lang)
        target_lang = languages.get(target_lang)
        installed_languages = argostranslate.translate.get_installed_languages() # get installed languages
        from_lang = list(filter(   # get the correct translation direction through comparing the given source/target
            # language with installed languages
            lambda x: x.code == source_lang.lower(),
            installed_languages))[0]
        to_lang = list(filter(
            lambda x: x.code == target_lang.lower(),
            installed_languages))[0]
        translated_text = from_lang.get_translation(to_lang).translate(word)
        return {
            "translation": translated_text,
            "success": True
        }
    except:
        return {
            "translation": "",
            "success": False
        }
app.include_router(api_router)

