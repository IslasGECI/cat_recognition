import os
import cat_recognition as cr


class Test_Cat_Detector:
    def test_init(self):
        cr.Cat_Detector()


class Test_Paths_Management:
    def test_init(self):
        workdir = os.getcwd()
        cr.Paths_Management(workdir)
