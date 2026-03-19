# Stellar-activity-vs-planet-signals
ML project to detect exoplanet signals under stellar variability (spots, flares, rotation).

## 📖 Overview
This project aims to simulate stellar variability (star spots, rotation, flares) and develop machine learning models to detect exoplanet signals despite stellar noise.

## 🎯 Objectives
- Simulate stellar activity
- Inject planetary signals (transits)
- Train ML models to distinguish signals vs noise

## 🧪 Methods
- Synthetic data generation
- Signal processing
- Machine Learning (Random Forest / Neural Networks)

## 📂 Project Structure
stellar-activity-vs-planet-signals/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── data_simulation.py
│   ├── preprocessing.py
│   ├── model.py
│   └── evaluation.py
│
├── results/
│   ├── plots/
│   └── metrics/
│
├── README.md
├── requirements.txt
└── main.py

## 🚀 Future Work
- Use real NASA Kepler data
- Improve deep learning models
- Noise reduction techniques

## 🛠️ Tech Stack
- Python
- NumPy, Pandas
- Scikit-learn
- Matplotlib
