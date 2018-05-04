# Tensorflow Custom Object Detection Training
Training Custom object detection in Tensorflow object Detection API


## Installation and Setup:
1. Download Tensorflow Repository models:
   https://github.com/tensorflow/models


2. Download model:
   https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

3. Download Anaconda3 for Python3.6:
   https://www.anaconda.com/download/#linux


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
