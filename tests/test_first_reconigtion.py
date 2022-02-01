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
        execution_path = "./tests"
        paths_management = Paths_Management(execution_path)
        paths_management.setup_directory_processed()
        inputs_and_paths = paths_management.get_input_output_paths()
        obtained_list = list(inputs_and_paths)
        expected_list = [
            (
                "./tests/data/resized/image3.jpg",
                "./tests/data/processed/no_cat_detected/image3_predicted.jpg",
                "./tests/data/processed/cat_detected/image3_predicted.jpg",
            )
        ]
        assert expected_list == obtained_list
