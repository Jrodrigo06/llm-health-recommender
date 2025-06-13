import unittest
from fastapi.testclient import TestClient
from app.api.routes import app
from app.models.schema import *
from app.services.mongo_service import log_prediction, get_user_history, create_user, login_user, get_user_info

client = TestClient(app)



class TestDummyRoutes(unittest.TestCase):
    
    def test_dummy_route(self):
        response = client.get("/api/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "HomePage"})
    
    def test_predict_route(self):
        
       
        user_request = UserRequest(
            user_id=1,
            question="Is my BMI normal?"
        )

        response2 = client.post("/api/predict", json=user_request.model_dump())

        self.assertEqual(response2.json(), {"recommendation": "Dummy response from LLM"})

    def test_history_route(self):
        
    
        # Assuming the user_id is 1 and we want to check the history for this user
        response3 = client.get("api/history/1")
        self.assertEqual(response3.status_code, 200) 


if __name__ == "__main__":
   unittest.main()