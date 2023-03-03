from tqdm import tqdm
from os import listdir
import typer

from cat_recognition import Cat_Detector

app = typer.Typer()


@app.command()
def make_detections(cut_prob: float = 0.01):
    cd = Cat_Detector()
    root_path = "/workdir/data"
    resized_photos = listdir("data/resized/")
    all_paths = [f"/workdir/data/resized/{image}" for image in resized_photos]
    _ = [cd.move_if_detection_is_positive(image_path, root_path) for image_path in tqdm(all_paths)]


if __name__ == "__main__":
    app()
