# Гатальская Валерия, 26 когорта — Финальный проект. Инженер по тестированию плюс
from sender_stand_request import get_new_track
import sender_stand_request
import data

def positive_assert(body):
    data.params_get["t"] = get_new_track(body)
    track_response = sender_stand_request.get_order(data.params_get)
    assert track_response.status_code == 200

def test_order():
    positive_assert(data.order_body)

