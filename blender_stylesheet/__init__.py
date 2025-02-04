from Qt import QtCore, QtWidgets, QtGui
from pathlib import Path
import logging


STYLESHEET_PATH = Path(__file__).parent / "blender_stylesheet.qss"
ICON_FILEPATH = Path(__file__).parent / "images" / "blender_icon_16.png"


def apply_blender_stylesheet(qapp):
    # add image directory to Qt search path, else style icons (e.g. checkbox) don't show sometimes
    image_directory = str(Path(__file__).parent / "images")
    QtCore.QDir.addSearchPath('images', image_directory)  # todo this is generic, might clash with other qt scripts
    
    if STYLESHEET_PATH.exists():
        qapp.setStyleSheet(STYLESHEET_PATH.read_text())
    else:
        logging.warning(f"Stylesheet not found: {STYLESHEET_PATH}")


def get_blender_icon():
    icon = QtGui.QIcon()
    if ICON_FILEPATH.exists():
        image = QtGui.QImage(str(ICON_FILEPATH))
        if not image.isNull():
            icon =QtGui.QIcon(QtGui.QPixmap().fromImage(image))
    return icon


def setup(qapp=None):
    """Setup the existing QApplication with the blender stylesheet and icon"""
    qapp = qapp or QtWidgets.QApplication.instance()
    apply_blender_stylesheet(qapp)
    qapp.setWindowIcon(get_blender_icon())
    return qapp
