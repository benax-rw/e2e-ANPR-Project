# End-to-End ANPR Project
This project focuses on developing a fully functional Automatic Number Plate Recognition (ANPR) system. It includes steps from data collection to model deployment.

## Features
- **Data Collection**: Capturing raw video footage and extracting frames.
- **Data Annotation**: Labeling number plates using tools like LabelImg.
- **Model Training**: Training a YOLO-based object detection model.
- **Character Recognition**: Extracting plate characters with OCR tools like Tesseract.
- **Integration**: Combining hardware (cameras, microcontrollers) with AI software for access control.

## Installation
To set up the project, follow these steps:
```bash
git clone https://github.com/benax-rw/e2e-ANPR-project.git
cd e2e-ANPR-project
pip install -r requirements.txt
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
