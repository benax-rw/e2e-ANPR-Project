# End-to-End ANPR Project
This project focuses on developing a fully functional Automatic Number Plate Recognition (ANPR) system. It includes steps from data collection to model deployment.

## Features
- **Data Collection**: Capturing raw video footage and extracting frames.
- **Data Annotation**: Labeling number plates using tools like LabelImg.
- **Model Training**: Training a YOLO-based object detection model.
- **Character Recognition**: Extracting plate characters with OCR tools like Tesseract.
- **Integration**: Combining hardware (cameras, microcontrollers) with AI software for access control.

## Data Processing
To Process Data, follow these steps:
```bash
git clone https://github.com/benax-rw/e2e-ANPR-project.git
cd e2e-ANPR-project

# Enter the directy harboring raw data and data processing tools
cd data_processing

# Start by turning the raw footages into images (frames)
python tool01__get_frames_from_video.py raw_footage_rag320p.mp4
python tool01__get_frames_from_video.py raw_footage_rah213t.mp4
python tool01__get_frames_from_video.py raw_footage_rah593c.mp4

# Review the created images (frames)
python tool02_review_images.py frames

# Label Images (if all the images look good now)
python tool03__labelImg_customized/labelImg.py

# Rearrange the dataset into Train and Val sets
python tool04__rearrange_dataset.py

The output of this stage is "e2e-ANPR-project/data_processing/dataset"
```
## Let the Training unfold!
The following line will do the job!
```bash
python train.py --img 640 --batch 8 --epochs 10 --data dataset.yaml
```

## Perform the Inference: 
```bash
python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.5 --source data/videos/test1.mov
```
## Talk to Arduino:
Let the model tell the Arduino when it recognizes a car. The arduino will then be program to trigger a mechanism that opens the gate.
```bash
python detect_and_talk_to_arduino.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.5 --source data/videos/test1.mov
```

## Usage
1. Collect raw video footage for number plates.
2. Use the provided scripts to extract frames and annotate them.
3. Train the YOLO model using the prepared dataset.
4. Perform inference on new video footage or images.
5. Integrate the trained model with hardware for automated access control.

## Contributing
Feel free to fork this repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
