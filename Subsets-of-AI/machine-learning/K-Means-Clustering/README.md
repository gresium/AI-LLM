# Color Compression with K-Means Clustering
A Python notebook that uses K-Means clustering to reduce image colors, compress file size, and preserve visual quality. It demonstrates how unsupervised learning can simplify image data by grouping similar colors.

# Objectives
Compress images by reducing color diversity
Demonstrate clustering on pixel RGB values
Compare original and compressed results visually
Experiment with different cluster counts (K)

# Methods
Algorithm: K-Means Clustering (sklearn.cluster.KMeans)
# Steps
Load image and reshape pixels into a 2D RGB array
Apply K-Means to cluster color values
Replace each pixel with its cluster centroid
Rebuild and display the compressed image
Key Parameters
K — number of color clusters (e.g., 8, 16, 32)
max_iter — iteration limit for convergence
random_state — ensures reproducibility

# Repository Contents
Color Compression with KMeans Clustering.ipynb — main notebook
input_image/ — original images
output_image/ — compressed images
README.md — documentation
QuickStart
Create environment
python -m venv .venv
Activate environment
macOS/Linux: source .venv/bin/activate
Windows: .venv\Scripts\activate
Install packages
pip install numpy matplotlib scikit-learn pillow
Open notebook
jupyter lab or jupyter notebook
Set input image path and run all cells to view compression output.

# Author
Developed by Gresa Hisa (@gresium) — AI & Cybersecurity Engineer
