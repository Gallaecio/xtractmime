import unittest
import pytest

from xtractmime.utils import _is_mp4_signature, _is_webm_signature

class TestUtils:

    file = open("tests/files/foo.mp4","rb")
    body_mp4 = file.read()
    file.close()

    file = open("tests/files/foo.webm","rb")
    body_webm = file.read()
    file.close()

    @pytest.mark.parametrize("input_bytes,expected",[
        (body_mp4,True),
        (b"\x00\x00\x00",False),
        (b"\x00\x00\x00 ftypmp4",False),
        (b"\x00\x00\x00 ftypmp42",False),
        (b"\x00\x00\x00 testmp42\x00\x00\x00\x00mp42mp41isomavc1",False),
        (b"\x00\x00\x00 ftyp2222\x00\x00\x00\x002222mp41isomavc1",True),
        (b"\x00\x00\x00 ftyp2222\x00\x00\x00\x0022222221isomavc1",False),
        ])
    def test_is_mp4_signature(self, input_bytes, expected):
        assert _is_mp4_signature(input_bytes) == expected


    def test_is_webm_signature(self):
        assert _is_webm_signature(self.body_webm) == True