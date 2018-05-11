# Tensorflow Custom Object Detection Training
Training Custom object (knife) detection in Tensorflow object Detection API

## Installation and Setup:
1. Download Tensorflow Repository models:
   https://github.com/tensorflow/models


2. Download model:
   https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

 
3. Clone the following Repo:
   https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10


```bash
# labelImg  (Python2)
sudo apt-get install pyqt4-dev-tools
sudo pip install lxml
make qt4py2
python labelImg.py

# Run the following in Paperspace VM
sudo pip2 install tensorflow==1.5.0
sudo apt-get install protobuf-compiler python-pil python-lxml python-tk

export PYTHONPATH=~/Desktop/tf_training/models:$PYTHONPATH
export PYTHONPATH=~/Desktop/tf_training/models/research:$PYTHONPATH
export PYTHONPATH=~/Desktop/tf_training/models/research/slim:$PYTHONPATH

# Run the following from models/research:
protoc object_detection/protos/*.proto --python_out=.
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
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
7. Generate tf.record files for both test and train labels by running the following in reference_code:
   ```bash
   python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record
   python generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=test.record
   ```
8. Create labelmap-"labelmap.pbtxt" and training configuration file-"faster_rcnn_inception_v2_pets.config"

9. Copy training_files contents to object_detection directory and start training by using following command:
   ```bash
   python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config
   ```

10. Export the inference_graph (trained model):
   ```bash
   python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph
   ```
