import pytest
import typecheck

from wiggle.cm import bwr


class TestBwr:
    def test_input_range(self):
        with pytest.raises(typecheck.typecheck_decorator.InputParameterError):
            bwr(-1.0)
