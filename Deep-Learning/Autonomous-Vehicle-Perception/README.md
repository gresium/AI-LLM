# Autonomous Vehicles (AV) and Intelligent Transport Systems (ITS) Detection

### Overview
This project implements a computer vision pipeline for **autonomous vehicle and intelligent transport system (ITS)** image detection using **MobileNetV3** on a custom dataset.  
It was developed and tested in Google Colab, optimized for real-world object recognition across multiple vehicle classes such as cars, buses, and trucks.
( for the images.zip file dm me personally , size to big) 
---

##  Model Pipeline

1. **Dataset Preparation**
   - All images were collected and structured into `/content/Images/default` for single-class testing.
   - Labels were managed in a `labels.csv` file containing filename–class mappings.
   - When multi-class detection was later introduced, images were automatically reorganized into `/Images/<class_name>/` subfolders using Python automation.

2. **Model Architecture**
   - Built with **MobileNetV3-Large**, pre-trained on ImageNet.
   - Final classifier layer replaced with a custom `Linear(num_features, num_classes)` head.
   - Supports GPU acceleration via PyTorch.

3. **Training**
   - Conducted in Google Colab using a clean, reproducible notebook workflow.
   - Loss monitored per epoch with Adam optimizer.
   - Final weights exported as `mobilenet_classifier_final.pth`.

4. **Troubleshooting & Debugging**
   - **Colab zip extraction errors** resolved by verifying file paths with `os.listdir()` and dynamically adjusting paths.
   - **FileNotFoundError** during training resolved by restructuring dataset folders.
   - **"Default-only" class bug** fixed by ensuring the label CSV matched real folder names.
   - **Visualization errors** (e.g., `bus` or `car` not found) resolved by normalizing class names and verifying folder creation logic.
   - Tested and validated image-by-image inference before batch processing.

5. **Visualization**
   - A 3×3 grid plot displays predictions on sample images.
   - Each subplot includes the true and predicted labels.
   - Class names (e.g., `bus`, `car`, `truck`) mapped dynamically from the dataset.

---

##  Evaluation
Model performance was validated using:
- **Confusion Matrix** for class-level accuracy assessment.
- **ROC Curves** for per-class AUC comparison.
- **Precision, Recall, and F1-score** planned for integration in next iteration.

These evaluations ensured model reliability and transparency during post-training analysis.

---

##  Tech Stack
- **Language:** Python 3.10  
- **Frameworks:** PyTorch, Torchvision  
- **Environment:** Google Colab  
- **Visualization:** Matplotlib, Seaborn, scikit-learn metrics  


---

##  How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/gresium/autonomous-vehicles-its-detection.git
   cd autonomous-vehicles-its-detection
   
2. Open the notebook in Google Colab:
   https://colab.research.google.com/github/gresium/autonomous_vehicles_its_detection/blob/main/autonomous_vehicles_its_detection.ipynb

3. Run all cells sequentially:
Dataset setup
Model training
Visualization
Evaluation
(Optional) Upload your own dataset to /content/Images/default to test the pipeline on new data

# Future Work
Expand dataset and retrain for multi-class detection.
Integrate bounding box detection for real-time AV analysis.
Deploy model for live ITS camera feeds.

 # Author
Developed by Gresa Hisa (@gresium)

AI & ML Engineer | Cybersecurity Engineer 
GitHub: github.com/gresium

