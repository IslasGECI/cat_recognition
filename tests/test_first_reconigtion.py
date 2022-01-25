import os
import cat_recognition as cr
from cat_recognition.first_recognition import Paths_Management


class Test_Cat_Detector:
    def test_init(self):
        cr.Cat_Detector()


class Test_Paths_Management:
    def test_init(self):
        workdir = os.getcwd()
        cr.Paths_Management(workdir)

    def test_get_input_output_paths(self):
        execution_path = os.getcwd()
        paths_management = Paths_Management(execution_path)
        paths_management.setup_directory_processed()
        inputs_and_paths = paths_management.get_input_output_paths()
        assert inputs_and_paths.__class__ == type(zip())
