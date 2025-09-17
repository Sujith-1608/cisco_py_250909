import pytest
from hms.app import batch_calc

def test_threaded_avg_age():
    """Test threaded batch average age calculation."""
    patients = [
        {"id": 1, "name": "John Doe", "age": 45, "disease": "Flu"},
        {"id": 2, "name": "Jane Smith", "age": 32, "disease": "Diabetes"},
        {"id": 3, "name": "Michael Johnson", "age": 60, "disease": "Hypertension"},
    ]
    expected_avg = (45 + 32 + 60) / 3
    avg_age = batch_calc.calculate_average_age_threaded(patients, batch_size=2)
    assert round(avg_age, 2) == round(expected_avg, 2)

@pytest.mark.asyncio
async def test_async_avg_age():
    """Test asyncio batch average age calculation (native async style)."""
    patients = [
        {"id": 1, "name": "John Doe", "age": 45, "disease": "Flu"},
        {"id": 2, "name": "Jane Smith", "age": 32, "disease": "Diabetes"},
        {"id": 3, "name": "Michael Johnson", "age": 60, "disease": "Hypertension"},
    ]
    expected_avg = (45 + 32 + 60) / 3
    avg_age = await batch_calc.calculate_average_age_async(patients, batch_size=2)
    assert round(avg_age, 2) == round(expected_avg, 2)

