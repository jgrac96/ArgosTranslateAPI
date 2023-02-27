import argostranslate.package
import argostranslate.translate



# to be able to convert from input of API from Java to country codes needed by Argos Translate
languages = {"English":"EN", "German":"DE", "Italian":"IT", "French":"FR", "Spanish":"ES"}

# load packages
req = ["en_fr", "en_de", "en_es", "en_it", "fr_en", "de_en", "es_en", "it_en"]
argostranslate.package.install_from_path("builder/data/translate-de_en-1_0.argosmodel")
