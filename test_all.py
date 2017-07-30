from graphene.test import Client
from flask import url_for
import pytest

from app import app as server
import osquery
import schema

def test_local_fabric():
    run = osquery.Instance()
    out = run.local('echo test')
    assert out == 'test'

def test_graphene():
    client = Client(schema.schema)
    executed = client.execute('{ test }')
    assert executed == {
        'data': {
            'test': 'test'
        }
    }


@pytest.fixture
def app():
    return server

class TestServer:

    def test_flask(self, client):
        res = client.get(url_for('graphql'))
        assert res.status_code == 400
