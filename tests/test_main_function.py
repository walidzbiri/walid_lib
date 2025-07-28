from unittest.mock import Mock, patch

import pytest

from walid_lib import main


class TestMainParametrized:
    @pytest.mark.parametrize(
        "response_data,expected",
        [
            ({"id": 1, "title": "Test"}, {"id": 1, "title": "Test"}),
        ],
    )
    @patch("requests.get")
    def test_main_various_responses(self, mock_get, response_data, expected):
        """Test various response formats"""
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = response_data
        mock_get.return_value = mock_response

        # Act
        result = main()

        # Assert
        assert result == expected
