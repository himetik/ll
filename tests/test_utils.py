import pytest
from unittest.mock import patch, MagicMock
from models import StandardResponse
from utils import check_url_status


def test_check_url_status_up():
    mock_response = MagicMock()
    mock_response.status_code = 200

    mock_client_instance = MagicMock()
    mock_client_instance.get.return_value = mock_response

    mock_client_class = MagicMock()
    mock_client_class.return_value.__enter__.return_value = mock_client_instance

    with patch('httpx.Client', return_value=mock_client_class.return_value):
        url = "http://example.com"
        result = check_url_status(url)

        assert isinstance(result, StandardResponse)
        assert result.success is True
        assert result.data.status == "up"
        assert result.data.code == 200
        assert result.error is None


@pytest.fixture
def mock_client():
    mock_response = MagicMock()
    mock_response.status_code = 200
    
    mock_client_instance = MagicMock()
    mock_client_instance.get.return_value = mock_response
    
    mock_client_class = MagicMock()
    mock_client_class.return_value.__enter__.return_value = mock_client_instance
    
    with patch('httpx.Client', return_value=mock_client_class.return_value) as mock:
        yield mock


def test_check_url_status_up_with_fixture(mock_client):
    url = "http://example.com"
    result = check_url_status(url)
    
    assert isinstance(result, StandardResponse)
    assert result.success is True
    assert result.data.status == "up"
    assert result.data.code == 200
    assert result.error is None