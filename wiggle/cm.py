import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


def bwr(alpha: float = 0) -> LinearSegmentedColormap:
    """
    Create a Blue-White-Red colormap given transparency value (alpha,
    default=0 for seismic cmap) in the middle.

    :param alpha: Transparency value in the middle between 0 and 1 (default=0).
    :type alpha: float
    :return: Blue-White-Red colormap
    :rtype: matplotlib.colors.LinearSegmentedColormap object
    """

    # Input check
    if alpha < 0 or alpha > 1:
        raise ValueError("Alpha value is between 0 and 1.")

    # Construct cmap dictionary
    cdict = {
        'red': ((0, 0, 0),
                (0.25, 0, 0),
                (0.5, 1, 1),
                (0.75, 0.8314, 0.8314),
                (1, 0.5, 0.5)),

        'green': ((0, 0, 0),
                  (0.25, 0.375, 0.375),
                  (0.5, 1, 1),
                  (0.75, 0.375, 0.375),
                  (1, 0, 0)),

        'blue': ((0, 0.5, 0.5),
                 (0.25, 0.8314, 0.8314),
                 (0.5, 1, 1),
                 (0.75, 0, 0),
                 (1, 0, 0)),

        'alpha': ((0, 1, 1),
                  (0.5, alpha, alpha),
                  (1, 1, 1))
    }

    return LinearSegmentedColormap('BlueWhiteRed', cdict)


if __name__ == '__main__':
    # Show colormap gradient
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    fig, ax = plt.subplots()
    ax.imshow(gradient, interpolation='none', aspect='auto', cmap=bwr())
    ax.set_axis_off()
    plt.show()
