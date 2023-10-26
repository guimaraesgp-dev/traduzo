from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel

translate_controller = Blueprint("translate_controller", __name__)


def get_translation_values():
    default_text = "O que deseja traduzir?"
    default_from = "pt"
    default_to = "en"
    default_translated = "What do you want to translate?"
    return default_text, default_from, default_to, default_translated


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()
    (
        text_to_translate,
        translate_from,
        translate_to,
        translated,
    ) = get_translation_values()

    if request.method == "POST":
        text_to_translate = request.form.get(
            "text-to-translate", text_to_translate
        )
        translate_from = request.form.get("translate-from", translate_from)
        translate_to = request.form.get("translate-to", translate_to)

        if text_to_translate:
            translator = GoogleTranslator(
                source=translate_from, target=translate_to
            )
            translated = translator.translate(text_to_translate)

    HistoryModel(
        {
            "languages": LanguageModel.list_dicts(),
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to,
            "translated": translated,
        }
    ).save()

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    languages = LanguageModel.list_dicts()
    (
        default_text,
        default_from,
        default_to,
        default_translated,
    ) = get_translation_values()

    text_to_translate = request.form.get("text-to-translate", default_text)
    translate_from = request.form.get("translate-from", default_from)
    translate_to = request.form.get("translate-to", default_to)

    translator = GoogleTranslator(source=translate_from, target=translate_to)
    translated = translator.translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
