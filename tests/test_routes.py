import unittest
from fastapi.testclient import TestClient
from app.main import app 
from app.models.schema import *

client = TestClient(app)

class TestDummyRoutes(unittest.TestCase):
    
    def test_dummy_route(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "HomePage"})
    
    def test_predict_route(self):
        data = UserInfo(
            name="John Doe",
            email="johndoe@gmail.com",
            age=30,
            bmi=22.5,
            height=175.0,
            weight=70.0,
            diabetes=False,
            overweight=False,
            heart_disease=False,
            family_history="No family history",
            smoking=False,
            alcohol=False
            )
        
        user_request = UserRequest(
            user_id=1,
            user_info=data,
            question="Is my BMI normal?"
        )

        response2 = client.post("/predict", json=user_request.model_dump())

        self.assertEqual(response2.json(), {"recommendation": "Dummy response from LLM"})

    def test_history_route(self):
        
    
        # Assuming the user_id is 1 and we want to check the history for this user
        response3 = client.get("/history/1")
        self.assertEqual(response3.json(), 
            {'history': [{'_id': '68147a514b4ba5ac8faa59db', 'question': 'Is my BMI normal?', 
                'response': {'recommendation': 'Dummy response from LLM'},
                'timestamp': '2025-05-02T03:54:57.074000',
               'user_id': 1}]})


if __name__ == "__main__":
    unittest.main()