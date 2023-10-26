from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
import json


def test_history_delete(app_test):
    # Criar um histórico de tradução
    history_entry = {
        "text_to_translate": "Do you love music?",
        "translate_from": "en",
        "translate_to": "pt",
    }
    history = HistoryModel(history_entry)
    history.save()

    # Obter o histórico de tradução antes da exclusão
    original_history_data_json = HistoryModel.list_as_json()
    original_history_data = json.loads(original_history_data_json)

    # Criar um usuário
    user = UserModel({"name": "um nome", "token": "um token"})
    user.save()

    # Excluir a entrada do histórico criada
    response = app_test.delete(
        f"/admin/history/{history._id}",
        headers={
            "Authorization": "um token",
            "User": "um nome",
        },
    )

    # Obter o histórico de tradução após a exclusão
    new_history_data_json = HistoryModel.list_as_json()
    new_history_data = json.loads(new_history_data_json)

    # Verificar os resultados
    assert response.status_code == 204
    assert len(new_history_data) == len(original_history_data) - 1
