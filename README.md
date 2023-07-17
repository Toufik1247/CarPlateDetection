# CarPlateDetection

A YOLOv5-lite based program using a custom model fine-tuned to detect French car plates, with added Optical Character Recognition (OCR) to read plates characters.

## Credits

This project is based on [YoloV5-lite](https://github.com/ppogg/YOLOv5-Lite).

## Demonstration

Here is a short video demonstrating the program detecting and reading a french licence plate:

[CarPlateDetection.webm](https://github.com/Toufik1247/CarPlateDetection/assets/127116915/d30dfaa2-0979-4f5b-b116-d337041f657d)

## Requirements

- Python 3.10
- pip

## Installation 

1. Clone the repository:

```bash
git clone https://github.com/Toufik1247/CarPlateDetection.git
```

2. Install Tesseract-OCR

```
sudo apt update
sudo apt install tesseract-ocr
```

3. Create your virtual environment:

```
python -m venv venvcarplatedetection
```

4. Activate your virtual environment:

```
source venvcarplatedetection/bin/activate
```


5. Install dependencies:

```
cd CarPlateDetection
pip install -r requirements.txt
```

6. Open upsampling.py in file editor:

```
cd ..
nano venvcarplatedetection/lib/python3.10/site-packages/torch/nn/modules/upsampling.py
```

7. Replace the following function:

```
def forward(self, input: Tensor) -> Tensor:
    return F.interpolate(input, self.size, self.scale_factor, self.mode, self.align_corners,
                         recompute_scale_factor=self.recompute_scale_factor)

```

with (be careful to indent correctly)

```
def forward(self, input: Tensor) -> Tensor:
    return F.interpolate(input, self.size, self.scale_factor, self.mode, self.align_corners,
                         # recompute_scale_factor=self.recompute_scale_factor
                         )
```

## Usage

Run the program using your webcam:

```
cd CarPlateDetection
python detect.py --source 0
```
