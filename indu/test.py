from ascii_studio import AsciiStudio
from image_file import ImageFile

import pytest
import mock


def test_quit():
    ascis = AsciiStudio()
    returend_value = ascis.parse("quit")
    assert returend_value is False

def test_render():
    ascis = AsciiStudio()
    with mock.patch.object(ImageFile, "render") as mock_render:
        ascis.parse("render")
        # Since not loaded we shall not excute the method
    assert not mock_render.called

    ascis = AsciiStudio()
    ascis.parse("load image slalom.jpg as slalom")
    assert ascis.image_alias_DB["slalom"] is not None

    with mock.patch.object(ImageFile, "render") as mock_render:
        ascis.parse("render")

    assert mock_render.assert_called_once


def test_info():
    ascis = AsciiStudio()
    
    with mock.patch.object(ascis, "info_command") as mock_info:
        ascis.parse("info")

    assert mock_info.assert_called_once

def test_save():
    ascis = AsciiStudio()
    with mock.patch.object(ascis, "save_command") as mock_info:
        ascis.parse("save")

    assert mock_info.assert_called_once

def test_set():
    ascis = AsciiStudio()
    with mock.patch.object(ascis, "set_command") as mock_info:
        ascis.parse("set")

    assert mock_info.assert_called_once



