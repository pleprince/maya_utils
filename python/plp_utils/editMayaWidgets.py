# Copyright 2015 Autodesk, Inc. All rights reserved.
#
# Use of this software is subject to the terms of the Autodesk
# license agreement provided at the time of installation or download,
# or which otherwise accompanies this software in either electronic
# or hard copy form.

from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui
try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from shiboken2 import wrapInstance
except ImportError:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from shiboken import wrapInstance


def changeMayaBackgroundColor(background='black', color='yellow'):
    # Get the mainWindow widget
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(long(ptr), QWidget)

    # Change the cascading stylesheet
    widget.setStyleSheet(
        'background-color:%s;' % background +
        'color:%s;' % color
    )


def changeMayaMenuColors(fontStyle='italic', fontWeight='bold',
                         fontColor='cyan'):
    # Get the widget
    widgetStr = mel.eval('string $tempString = $gMainCreateMenu')
    ptr = omui.MQtUtil.findControl(widgetStr)
    widget = wrapInstance(long(ptr), QWidget)

    # Change the cascading stylesheet
    widget.setStyleSheet(
        'font-style:%s;' % fontStyle +
        'font-weight:%s;' % fontWeight +
        'color:%s;' % fontColor
    )


def changeMayaScriptEditorFont():
    # Get the widget
    # widgetStr = mel.eval('string $tempString = $gCommandReporter')
    widgetStr = mel.eval('string $tempString = $gCommandLayout')
    ptr = omui.MQtUtil.findControl(widgetStr)
    widget = wrapInstance(long(ptr), QWidget)

    # Change the cascading stylesheet
    widget.setStyleSheet('font-size:10px;font-family:Source Code Pro')


def main():
    # changeMayaBackgroundColor()
    # changeMayaMenuColors()
    changeMayaScriptEditorFont()

# if __name__ == '__main__':
#     main()
