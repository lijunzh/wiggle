"""Wiggle plot for seismic data section visualization."""

from __future__ import annotations

from typing import TYPE_CHECKING

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def insert_zeros(
    trace: NDArray[np.floating],
    tt: NDArray[np.floating] | None = None,
) -> tuple[NDArray[np.floating], NDArray[np.floating]]:
    """Insert zero-crossing locations into a data trace via linear interpolation.

    Parameters
    ----------
    trace : NDArray[np.floating]
        1-D seismic trace.
    tt : NDArray[np.floating] | None
        Time/depth axis. Generated as ``np.arange(len(trace))`` when *None*.

    Returns
    -------
    trace_zi : NDArray[np.floating]
        Trace with interpolated zeros inserted.
    tt_zi : NDArray[np.floating]
        Corresponding time axis with zero-crossing positions.
    """
    if tt is None:
        tt = np.arange(len(trace))

    zc_idx = np.where(np.diff(np.signbit(trace)))[0]
    x1, x2 = tt[zc_idx], tt[zc_idx + 1]
    y1, y2 = trace[zc_idx], trace[zc_idx + 1]
    tt_zero = x1 - y1 / ((y2 - y1) / (x2 - x1))

    tt_split = np.split(tt, zc_idx + 1)
    trace_split = np.split(trace, zc_idx + 1)

    tt_zi = tt_split[0]
    trace_zi = trace_split[0]
    for i in range(len(tt_zero)):
        tt_zi = np.hstack((tt_zi, tt_zero[i : i + 1], tt_split[i + 1]))
        trace_zi = np.hstack((trace_zi, np.zeros(1), trace_split[i + 1]))

    return trace_zi, tt_zi


def _validate_inputs(
    data: NDArray[np.floating],
    tt: NDArray[np.floating] | None,
    xx: NDArray[np.floating] | None,
    ax: Axes | None,
    sf: float,
    *,
    verbose: bool,
) -> tuple[NDArray[np.floating], NDArray[np.floating], NDArray[np.floating], float]:
    """Validate and normalise inputs for :func:`wiggle`.

    Returns the rescaled *data*, *tt*, *xx*, and trace spacing *ts*.
    """
    if not isinstance(verbose, bool):
        raise TypeError("verbose must be a bool")

    if ax is not None and not isinstance(ax, matplotlib.axes.Axes):
        raise TypeError("ax must be a matplotlib Axes instance")

    # --- data ---
    if not isinstance(data, np.ndarray):
        raise TypeError("data must be a numpy array")
    if data.ndim != 2:
        raise ValueError("data must be a 2D array")

    # --- tt ---
    if tt is None:
        tt = np.arange(data.shape[0], dtype=float)
        if verbose:
            print("tt is automatically generated.")
    else:
        if not isinstance(tt, np.ndarray):
            raise TypeError("tt must be a numpy array")
        if tt.ndim != 1:
            raise ValueError("tt must be a 1D array")
        if tt.shape[0] != data.shape[0]:
            raise ValueError("tt length must match data row count")

    # --- xx ---
    if xx is None:
        xx = np.arange(data.shape[1], dtype=float)
        if verbose:
            print("xx is automatically generated.")
    else:
        if not isinstance(xx, np.ndarray):
            raise TypeError("xx must be a numpy array")
        if xx.ndim != 1:
            raise ValueError("xx must be a 1D array")
        if xx.shape[0] != data.shape[1]:
            raise ValueError("xx length must match data column count")

    # --- sf ---
    if not isinstance(sf, (int, float)):
        raise TypeError("Stretch factor (sf) must be a number")

    ts: float = float(np.min(np.diff(xx)))
    data_max_std = np.max(np.std(data, axis=0))
    data = data / data_max_std * ts * sf

    return data, tt, xx, ts


def wiggle(
    data: NDArray[np.floating],
    tt: NDArray[np.floating] | None = None,
    xx: NDArray[np.floating] | None = None,
    ax: Axes | None = None,
    color: str = "k",
    sf: float = 0.15,
    *,
    verbose: bool = False,
) -> Axes:
    """Create a wiggle plot of a seismic data section.

    Parameters
    ----------
    data : NDArray[np.floating]
        2-D array of shape ``(n_samples, n_traces)``.
    tt : NDArray[np.floating] | None
        Time/depth axis of length ``n_samples``.
    xx : NDArray[np.floating] | None
        Trace position axis of length ``n_traces``.
    ax : Axes | None
        Matplotlib axes to draw on. Uses ``plt.gca()`` when *None*.
    color : str
        Matplotlib colour string (default ``'k'``).
    sf : float
        Stretch factor controlling trace amplitude (default ``0.15``).
    verbose : bool
        Print debug information when *True*.

    Returns
    -------
    Axes
        The matplotlib axes containing the plot.
    """
    data, tt, xx, ts = _validate_inputs(data, tt, xx, ax, sf, verbose=verbose)
    n_traces = data.shape[1]

    if ax is None:
        ax = plt.gca()

    for i in range(n_traces):
        trace = data[:, i]
        offset = xx[i]
        if verbose:
            print(offset)

        trace_zi, tt_zi = insert_zeros(trace, tt)
        ax.fill_betweenx(
            tt_zi,
            offset,
            trace_zi + offset,
            where=trace_zi >= 0,
            facecolor=color,
        )
        ax.plot(trace_zi + offset, tt_zi, color)

    ax.set_xlim(xx[0] - ts, xx[-1] + ts)
    ax.set_ylim(tt[0], tt[-1])
    ax.invert_yaxis()
    return ax


if __name__ == "__main__":
    rng = np.random.default_rng()
    sample_data = rng.standard_normal((1000, 100))
    wiggle(sample_data)
    plt.show()
