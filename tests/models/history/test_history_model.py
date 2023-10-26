import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    historyJson = HistoryModel.list_as_json()
    historyData = json.loads(historyJson)

    assert historyData[0]["text_to_translate"] == "Hello, I like videogame"
    assert historyData[0]["translate_from"] == "en"
    assert historyData[0]["translate_to"] == "pt"
