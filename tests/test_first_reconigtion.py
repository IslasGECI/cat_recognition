import os
import cat_recognition as cr
from cat_recognition.first_recognition import Paths, Paths_Management


class Test_Cat_Detector:
    def test_init(self):
        cr.Cat_Detector()


class Test_Paths_Management:
    def test_init(self):
        workdir = os.getcwd()
        cr.Paths_Management(workdir)

    def test_get_input_output_paths(self):
        execution_path = "/workspaces/cat_recognition/tests"
        paths_management = Paths_Management(execution_path)
        paths_management.setup_directory_processed()
        inputs_and_paths = paths_management.get_input_output_paths()
        obtained_list = list(inputs_and_paths)
        expected_list = [('/workspaces/cat_recognition/tests/data/resized/image3.jpg',
                          '/workspaces/cat_recognition/tests/data/processed/no_cat_detected/image3_predicted.jpg',
                          '/workspaces/cat_recognition/tests/data/processed/cat_detected/image3_predicted.jpg')]
        assert expected_list == obtained_list
        
class Test_Paths:
    def test_PATHS(self):
        paths = Paths()
        print(paths.PROCESSED_IMAGE_AS_NEGATIVE)
        assert paths.PROCESSED_IMAGE_AS_NEGATIVE == "processed_image_as_negative"
        assert paths.PROCESSED_IMAGE_AS_POSITIVE == "processed_image_as_positive"
