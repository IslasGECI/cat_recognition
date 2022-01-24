import os
import cat_recognition as cr


def test_return_one():
    expected = 1
    obtained = cr.return_one()
    assert expected == obtained


class Test_Cat_Detector:
    def test_init(self):
        cat_detector = cr.Cat_Detector()


class Test_Paths_Management:
    def test_init(self):
        workdir = os.getcwd()
        cat_detector = cr.Paths_Management(workdir)
