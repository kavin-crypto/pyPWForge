class ApiBase:

    BASE_URL = "https://rahulshettyacademy.com"
    API_KEY = "qaclick123"

    def __init__(self, request):
        self.request = request

    def add_location(self, location_data):
        response = self.request.post(
            f"{self.BASE_URL}/maps/api/place/add/json",
            params={
                "key": self.API_KEY
            },
            data=location_data
        )

        return response

    def get_location(self, place_id):
        response = self.request.get(
            f"{self.BASE_URL}/maps/api/place/get/json",
            params={
                "place_id": place_id,
                "key": self.API_KEY
            }
        )

        return response

    def update_location(self,place_id,address):
        response = self.request.put(
            f"{self.BASE_URL}/maps/api/place/update/json",
            params={
                "key": self.API_KEY
            },
            data={
                "place_id": place_id,
                "address": address,
                "key": self.API_KEY
            }
        )

        return response

    def delete_location(self, place_id):
        response = self.request.post(
            f"{self.BASE_URL}/maps/api/place/delete/json",
            params={
                "key": self.API_KEY
            },
            data={
                "place_id": place_id
            }
        )

        return response