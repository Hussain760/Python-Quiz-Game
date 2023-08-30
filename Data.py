from requests import get
from json import loads


def Data(questions, difficulty):
    request_Api = get(
        f"https://opentdb.com/api.php?type=multiple&amount={questions}&difficulty={difficulty}"
    )

    data = loads(request_Api.text)["results"]

    return data
