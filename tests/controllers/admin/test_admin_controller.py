import json
from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def create_sample_history_entry():
    entry = HistoryModel(
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        }
    )
    entry.save()
    return entry


def test_history_delete(app_test):
    # Cria uma entrada no histórico
    create_sample_history_entry()

    # Obtém os dados do histórico antes da exclusão
    history_data_json = HistoryModel.list_as_json()
    history_data = json.loads(history_data_json)

    UserModel({"name": "um_nome", "token": "um_token"}).save()

    history_count = len(history_data)
    # Exclui a entrada do histórico
    response = app_test.delete(
        f"/admin/history/{history_data[0]['_id']}",
        headers={
            "Authorization": "um_token",
            "User": "um_nome",
        },
    )

    # Obtém os dados atualizados do histórico
    new_history_data_json = HistoryModel.list_as_json()
    new_history_data = json.loads(new_history_data_json)

    new_history_count = len(new_history_data)

    assert (
        history_count - new_history_count == 1
    ), "A exclusão não removeu com sucesso o registro do histórico."
    assert (
        response.status_code == 204
    ), "A exclusão não retornou o código de status esperado."
