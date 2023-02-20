import requests
import json


class MakeApiCall:
    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("----sucessfully fetched the data")
            # self.formatted_print(response.json())
            print(response.json()['value'])
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")

    # def get_user_data(self, api):
    #     response = requests.get(f"{api}")
    #     if response.status_code == 200:
    #         print("-----sucessfully fetched the data with parameters provided")
    #         # self.formatted_print(response.json())
    #         joke = response.json()
    #         print(joke.get('value'))
    #     else:
    #         print(f"Hello person, there's a {response.status_code} error with your request")

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self, api):
        self.get_data(api)
        # self.get_user_data(api)


if __name__ == "__main__":
    api_call = MakeApiCall("https://api.chucknorris.io/jokes/random")
