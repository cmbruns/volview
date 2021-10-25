# A) direct volume rendering
#   * absorption only
#   * emission only
#   * emission + absorption
#   * single scattering no shadows
#   * single scattering with shadows
#   * multiple scattering
#
#   Interpolation:
#     * nearest neighbor
#     * trilinear
#     * cubic
#
# B) isosurface from signed distance field
#
# Grid:
#   * rectilinear
#   * hexagonal
#   * rhombic dodecahedral
#
# Per-voxel lighting vs per-fragment lighting
#
# Windows:
#   * 3D view
#   * 2D horizontal slice view (for debugging)
#
# Example volumes:
#   * multiscale fly brain image
#   * electron density map
#   * MRI scan
#   * Toy 3x3x3
#
# Representations:
#   * voxel grid
#   * volume render or isosurface
#   * volume projection (1D projection in 2D case)
#   * ray under current mouse position
#

import sys
from PySide6 import QtWidgets


def main():
    from volview.main_window import VolViewWindow
    app = QtWidgets.QApplication(sys.argv)
    window = VolViewWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
