import pytest

from wiggle.wiggle import wiggle


class TestWiggle:
    def test_input_check(self):
        with pytest.raises(TypeError):
            wiggle(0)
