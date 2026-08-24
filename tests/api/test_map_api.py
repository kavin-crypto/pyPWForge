import json
import allure

from utils.api_base import ApiBase

"""
 Test Scenario:
 - Add a new location using the Place API
 - Retrieve the created location using place_id
 - Verify the location details
 - Update the location address using PUT
 - Retrieve the location again and verify the updated address
 - Delete the location
 """
@allure.feature("Google Maps API")
@allure.story("Place Management")
@allure.title("Create, update and delete a place")
def test_location_api(api_request):

    # Load test data
    with open("testData/location_data.json", "r") as file:
        location_data = json.load(file)
    api = ApiBase(api_request)

    # 1. Add Place
    with allure.step("Add new place"):
        response = api.add_location(location_data["create_location"])
        assert response.ok
        body = response.json()
        assert body["status"] == "OK"
        assert response.status == 200
        place_id = body["place_id"]

    # 2. Get Place
    with allure.step("Get created place"):
        response = api.get_location(place_id)
        body = response.json()
        assert response.status == 200
        assert response.ok
        assert body["name"] == location_data["create_location"]["name"]
        assert body["address"] == location_data["create_location"]["address"]
        assert body["phone_number"] == location_data["create_location"]["phone_number"]

    # 3. Update Place
    with allure.step("Update place address"):
        updated_address = location_data["update_location"]["address"]
        response = api.update_location(place_id, updated_address)
        assert response.ok
        assert response.status == 200
        body = response.json()
        assert body["msg"] == "Address successfully updated"

    # 4. Verify updated Place
    with allure.step("Verify updated address"):
        response = api.get_location(place_id)
        assert response.ok
        assert response.status == 200
        body = response.json()
        assert body["address"] == updated_address

    # Delete Place
    with allure.step("Delete place"):
        response = api.delete_location(place_id)
        assert response.ok
        body = response.json()
        assert body["status"] == "OK"