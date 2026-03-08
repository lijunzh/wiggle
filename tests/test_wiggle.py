"""Tests for the wiggle plot module."""

import matplotlib.pyplot as plt
import numpy as np
import pytest

from wiggle import wiggle


@pytest.fixture(autouse=True)
def _close_figures():
    """Close all matplotlib figures after each test to prevent leaks."""
    yield
    plt.close("all")


class TestInputValidation:
    """Ensure invalid inputs are rejected with clear errors."""

    def test_rejects_non_array_data(self):
        with pytest.raises(TypeError, match="numpy array"):
            wiggle("not a numpy array")

    def test_rejects_1d_data(self):
        with pytest.raises(ValueError, match="2D"):
            wiggle(np.array([1, 2, 3]))

    def test_rejects_2d_tt(self):
        data = np.random.default_rng(0).standard_normal((10, 5))
        tt = np.arange(10).reshape(10, 1)
        with pytest.raises(ValueError, match="1D"):
            wiggle(data, tt=tt)

    def test_rejects_2d_xx(self):
        data = np.random.default_rng(0).standard_normal((10, 5))
        xx = np.arange(5).reshape(5, 1)
        with pytest.raises(ValueError, match="1D"):
            wiggle(data, tt=np.arange(10, dtype=float), xx=xx)

    def test_rejects_non_bool_verbose(self):
        data = np.random.default_rng(0).standard_normal((10, 5))
        with pytest.raises(TypeError, match="bool"):
            wiggle(data, verbose="yes")  # type: ignore[arg-type]

    def test_rejects_non_axes_ax(self):
        data = np.random.default_rng(0).standard_normal((10, 5))
        with pytest.raises(TypeError, match="Axes"):
            wiggle(data, ax="not_an_axes")  # type: ignore[arg-type]

    def test_rejects_non_numeric_sf(self):
        data = np.random.default_rng(0).standard_normal((10, 5))
        with pytest.raises(TypeError, match="number"):
            wiggle(data, sf="big")  # type: ignore[arg-type]


class TestWigglePlot:
    """Verify correct plotting behaviour."""

    def test_returns_axes(self):
        data = np.array([[1.0, -1.0], [-1.0, 1.0]])
        ax = wiggle(data)
        assert isinstance(ax, plt.Axes)

    def test_plot_has_lines_and_fills(self):
        data = np.array([[1.0, -1.0], [-1.0, 1.0]])
        ax = wiggle(data)
        assert len(ax.lines) > 0
        assert len(ax.collections) > 0

    def test_axis_limits_inverted(self):
        data = np.array([[1.0, -1.0], [-1.0, 1.0]])
        ax = wiggle(data)
        xlims = ax.get_xlim()
        ylims = ax.get_ylim()
        assert xlims[0] < xlims[1]
        assert ylims[0] > ylims[1], "y-axis should be inverted"

    def test_uses_provided_axes(self):
        _fig, ax = plt.subplots()
        data = np.random.default_rng(42).standard_normal((20, 3))
        ret_ax = wiggle(data, ax=ax)
        assert ret_ax is ax

    def test_verbose_output(self, capsys):
        data = np.random.default_rng(0).standard_normal((10, 3))
        wiggle(data, verbose=True)
        captured = capsys.readouterr()
        assert "automatically generated" in captured.out
