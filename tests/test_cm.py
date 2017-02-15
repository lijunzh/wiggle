import pytest

from wiggle.cm import bwr


class TestBwr:
    def test_input_check(self):
        with pytest.raises(ValueError):
            bwr(-1)