# Tensorflow Custom Object Detection Training
Training Custom object detection in Tensorflow object Detection API

## Installation and Setup:
1. Download Tensorflow Repository models:
   https://github.com/tensorflow/models


2. Download model:
   https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

3. Download Anaconda3 for Python3.6:
   https://www.anaconda.com/download/#linux
   
4. Clone the following Repo:
   https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10


```bash
conda create -n tensorflow1 pip
source activate tensorflow1

pip install --ignore-installed --upgrade tensorflow-gpu

conda install -c anaconda protobuf
pip install pillow
pip install lxml
pip install jupyter
pip install matplotlib
pip install pandas
pip install opencv-python

export PYTHONPATH=~/Desktop/tf_training/models:$PYTHONPATH
export PYTHONPATH=~/Desktop/tf_training/models/research:$PYTHONPATH
export PYTHONPATH=~/Desktop/tf_training/models/research/slim:$PYTHONPATH

# Run the following from models/research:
protoc object_detection/protos/*.proto --python_out=.

python setup.py build
python setup.py install

# Open the default object detector and verify the process
cd object_detection
jupyter notebook object_detection_tutorial.ipynb

# labelImg  (Python2)
sudo apt-get install pyqt4-dev-tools
sudo pip install lxml
make qt4py2
python labelImg.py
```
### Steps:
1. Extract contents of models in ~Deskop/tf_training
2. Extract "faster_rcnn_inception_v2_coco" in models/research/object_detection
3. Extract the contents of "TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10" to object_detection
4. Empty the following directories:
   a) training
   b) inference_graph
   c) images/test
   d) images/train
5. Create xml annotations using label_image/program/labelImg.py
6. Convert xml annotations to csv by running the following in reference_code:
```bash
python xml_to_csv.py
```
7. Generate tf.record files for both test and train labels:
```bash
python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record
python generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=test.record
```

 
