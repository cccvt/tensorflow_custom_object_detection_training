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
activate tensorflow1

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
protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto

python setup.py build
python setup.py install

# Open the default object detector and verify the process
cd object_detection
jupyter notebook object_detection_tutorial.ipynb
```

