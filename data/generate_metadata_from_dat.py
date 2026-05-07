import os
import numpy as np
import pandas as pd

rows = []

# =====================
# CLASS CONFIG
# =====================
classes = {
    0: {"dir": "output_class0", "planet": 0, "activity": 0},
    1: {"dir": "output_class1", "planet": 0, "activity": 1},
    2: {"dir": "output_class2", "planet": 1, "activity": 1},
    3: {"dir": "output_class3", "planet": 1, "activity": 1},
}

# =====================
# LOOP THROUGH FILES
# =====================
for cls, info in classes.items():
    folder = info["dir"]

    for file in os.listdir(folder):
        if file.endswith(".dat"):

            filepath = os.path.join(folder, file)

            try:
                data = np.loadtxt(filepath)

                time = data[:, 0] / 86400.0
                flux = data[:, 1]

                # Basic features
                flux_mean = np.mean(flux)
                flux_std = np.std(flux)
                amplitude = np.max(flux) - np.min(flux)
                n_points = len(flux)
                duration = time[-1] - time[0]

                rows.append({
                    "filename": filepath,
                    "class": cls,
                    "has_planet": info["planet"],
                    "has_activity": info["activity"],
                    "flux_mean": flux_mean,
                    "flux_std": flux_std,
                    "amplitude": amplitude,
                    "n_points": n_points,
                    "duration": duration
                })

            except Exception as e:
                print(f"Error reading {filepath}: {e}")

# =====================
# SAVE CSV
# =====================
df = pd.DataFrame(rows)
df.to_csv("metadata_from_dat.csv", index=False)

print("metadata_from_dat.csv created!")
