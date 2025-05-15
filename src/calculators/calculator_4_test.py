from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def median(self, numbers: List[float]) -> float:
        return sum(numbers) / len (numbers)
        
def test_calculate():
    mock_request = MockRequest({"numbers": [10, 10, 10, 10]})
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'Calculator': 4, 'value': 10.0, 'Success': True}}

    
