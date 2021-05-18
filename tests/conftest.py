import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


@pytest.fixture
def client():
    from app.main import app
    app.config["TESTING"] = True
    return app.test_client()
