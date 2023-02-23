docker run -itv $PWD:/workdir/data/raw/photos -v $PWD:/workdir/data islasgeci/cat_recognition:latest make detection_with_yolo
sudo chown --recursive $USER:$USER .
rm --force --recursive raw
rm --force --recursive resized