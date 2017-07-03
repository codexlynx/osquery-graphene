import pytest
import osquery

def test_local_fabric():
    run = osquery.Instance()
    out = run.local('echo test')
    assert out == 'test'
