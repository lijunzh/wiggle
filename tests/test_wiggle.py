import numpy as np
import matplotlib.pyplot as plt
import pytest

from wiggle.wiggle import wiggle

class TestWiggle:
    def test_input_check_invalid_data(self):
        # Invalid type for data should raise TypeError.
        with pytest.raises(TypeError):
            wiggle("not a numpy array")

        # 1D array should raise ValueError.
        with pytest.raises(ValueError):
            wiggle(np.array([1, 2, 3]))

    def test_input_check_invalid_tt(self):
        # Create valid data and invalid tt (2D instead of 1D)
        data = np.random.randn(10, 5)
        tt = np.arange(10).reshape(10, 1)
        with pytest.raises(ValueError):
            wiggle(data, tt=tt)

    def test_input_check_invalid_xx(self):
        # Create valid data and create invalid xx shape
        data = np.random.randn(10, 5)
        tt = np.arange(10)
        xx = np.arange(5).reshape(5, 1)
        with pytest.raises(ValueError):
            wiggle(data, tt=tt, xx=xx)

    def test_wiggle_returns_axes(self):
        # Test that valid call returns an axes with expected plot elements.
        data = np.array([[1, -1], [-1, 1]])
        ax = wiggle(data, verbose=False)
        # Check that plot lines exist.
        assert len(ax.lines) > 0
        # Check that filled collections exist.
        assert len(ax.collections) > 0
        # Check axis limits are set (non-zero range)
        xlims = ax.get_xlim()
        ylims = ax.get_ylim()
        assert xlims[0] < xlims[1]
        assert ylims[0] < ylims[1]

    def test_wiggle_with_custom_ax(self):
        # Test using a provided matplotlib axis
        fig, ax = plt.subplots()
        data = np.random.randn(20, 3)
        ret_ax = wiggle(data, ax=ax, verbose=False)
        # Returned axis should be the same as provided one.
        assert ret_ax is ax
        plt.close(fig)
