#  Tag Corner Detection (Classical + Deep Learning)

##  Overview

This project focuses on detecting the **four corner coordinates of a tag** in an image.

Unlike bounding box detection (YOLO), this task predicts:

```
x1 y1 x2 y2 x3 y3 x4 y4
```

We implemented:

*  Classical Computer Vision approach (OpenCV)
*  Deep Learning model (CNN-based corner regression)
*  Confidence-based tag presence detection
*  Evaluation using IoU and Homography Error

---

##  Dataset Structure
Download Training data from https://drive.google.com/drive/folders/1Gz30BJaROU9MR2R4T1I_qJ-CUl-WlUO1

```
dataset/
│── images/
│── train_corners.csv
│── val_corners.csv
```

##  Setup (Google Colab Recommended)


### Install Dependencies

```bash
pip install opencv-python-headless torch torchvision albumentations
```

##  Approach

###  Classical Method

* Grayscale → Blur → Canny Edge Detection
* Contour detection
* Polygon approximation (4 corners)

---

### 🔹 Deep Learning Model

* CNN-based regression model
* Input: Image (256×256)
* Output: 8 values (4 corners)


##  Performance Tips

* Copy images to `/content` for faster training
* Reduce dataset size for quick testing
* Use GPU in Colab

---

##  Results

* Low MSE loss (~0.0001)
* Accurate corner prediction (~few pixel error)
* Robust compared to classical method

---

##  Key Learnings

* Corner regression vs bounding box detection
* Importance of normalization
* Multi-task learning (corners + confidence)
* Geometric evaluation (homography)

---

##  Future Improvements

* Use ResNet / EfficientNet backbone
* Switch to YOLOv8 keypoint detection
* Deploy as API (FastAPI)
* Convert to ONNX / TorchScript

---

##  Author

Haseeb Khan 
---
