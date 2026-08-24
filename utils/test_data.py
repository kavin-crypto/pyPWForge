import json


def get_user_credentials():
    with open("testData/userCredentials.json") as file:
        data = json.load(file)

    return data["UserCredentials"]