from flask import Blueprint
from models.history_model import HistoryModel


history_controller = Blueprint("history_controller", __name__)


# Req. 8
@history_controller.route("/", methods=["GET"])
def history():
    history_list = HistoryModel.list_as_json()
    return history_list
