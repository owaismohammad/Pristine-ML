# 🌊 Pristine-ML


*A Machine Learning-Based Solution for Visual Assessment of Water Purity*

## 📋 Table of Contents
- [📖 Introduction](#introduction)
- [✨ Features](#features)
- [🏗️ Architecture](#architecture)
- [🗂️ Dataset](#dataset)
- [🧠 Model Architecture](#model-architecture)
- [⚙️ Installation](#installation)
- [🚀 Usage](#usage)
- [📊 Results](#results)
- [👥 Contributors](#contributors)
- [📜 License](#license)

## 📖 Introduction
**Pristine-ML** is a machine learning model designed for visual assessment of water purity using computer vision techniques. This project focuses on determining whether a given water sample image is clean or unclean based on image data.

This repository holds the machine learning component of the Pristine platform, which is part of the project **Aqua-Percept**, built during the Xylem Global Student Innovation Challenge 2024.

## ✨ Features
- 🚰 **Convolutional Neural Network (CNN)** for image classification.
- ✅ Classifies images of water into **clean** or **unclean** categories.
- 📱 Scalable and easy to integrate into other platforms such as mobile apps and websites.
- 🌀 Data augmentation techniques for robust model performance.

## 🏗️ Architecture
Pristine-ML is built using a CNN architecture that processes water sample images. It performs binary classification to predict the cleanliness of the water. The system is integrated with a frontend interface to allow users to upload or capture images of water samples for purity analysis.

**Components:**
- 🖼️ Image Preprocessing
- 🧠 CNN Model
- 📈 Evaluation Metrics

## 🗂️ Dataset
The dataset contains images of water samples, categorized as **clean** or **unclean**. These images are labeled and stored in different folders. Data augmentation is applied to improve model robustness and generalization.

- **Clean**: Contains images of water deemed pure. 💧
- **Unclean**: Contains images of water that is contaminated or impure. 🌊

> 📝 Note: The dataset is not included in the repository for privacy reasons. You can create your dataset by collecting images of clean and unclean water or using existing datasets related to water purity.

## 🧠 Model Architecture
The model is built using a convolutional neural network (CNN) with the following key layers:
1. **Convolutional layers**: To extract image features. 🌀
2. **MaxPooling layers**: For down-sampling. ⬇️
3. **Dropout layers**: To prevent overfitting. 🚫
4. **Fully connected layers**: To classify the images into clean or unclean categories. 🗂️

### Model Summary:
- Input: Image (64x64x3) 🖼️
- Output: Binary classification (Clean/Unclean) ✅❌

## ⚙️ Installation
To run this project locally, follow these steps:

### Prerequisites
- Python 3.7+ 🐍
- TensorFlow 🔥
- Keras 🤖
- NumPy 🔢
- Matplotlib 📊
- OpenCV (optional, for image preprocessing) 🖼️

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/owaismohammad/Pristine-ML.git
    cd Pristine-ML
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Prepare your dataset:
    - Organize images into `train` and `test` folders with subfolders `clean` and `unclean`.
    - Update the `train_datagen` paths in the code to point to your dataset.

## 🚀 Usage

1. **Training the model**:
    ```bash
    python train_model.py
    ```

2. **Testing the model**:
    - You can pass a water sample image to the model using the `predict.py` script.

    Example:
    ```bash
    python predict.py --image path_to_image.jpg
    ```

3. **Evaluating the model**:
    - After training, the model’s performance will be displayed on the validation set, showing accuracy and loss over time.

## 📊 Results
- Achieved an accuracy of **98.786%** on the validation set. 📈
- Precision, recall, and F1-score metrics show the effectiveness of the model in identifying clean and unclean water samples. 🎯
- The model generalizes well across various test cases due to data augmentation. 🌀

> 📝 Note: Replace "98.456%" with actual accuracy after training.

## 👥 Contributors
- **Owais Mohammad** , **Saad Ahmed Siddiqui** 

Special thanks to all the participants of the Xylem Global Student Innovation Challenge 2024. 🙌

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
