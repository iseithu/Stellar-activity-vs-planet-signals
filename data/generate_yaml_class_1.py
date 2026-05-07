import numpy as np
import os

# =====================
# SETTINGS
# =====================
N = 250
output_dir = "generated_yaml_class_1"
os.makedirs(output_dir, exist_ok=True)

np.random.seed(42)

# =====================
# PARAMETER RANGES (CLASS 1)
# =====================

# ID → 20000–20249
ids = np.arange(20000, 20000 + N)

# Stellar parameters
mag = np.random.uniform(9, 12, N)          # PLATO bright stars
rotation = np.random.uniform(5, 30, N)     # solar-like rotation
inclination = np.random.uniform(0, 90, N)  # no transit → full range

# =====================
# LOAD TEMPLATE YAML
# =====================
with open("templateclass1.yaml", "r") as f:
    template = f.read()

# =====================
# GENERATE YAML FILES
# =====================
for i in range(N):

    content = template.format(
        id=int(ids[i]),
        mag=round(mag[i], 3),
        rotation=round(rotation[i], 3),
        inclination=round(inclination[i], 3),
    )

    filename = f"config_{i:04d}.yaml"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w") as f:
        f.write(content)

print(" Class 1: 250 YAML files (with PySpot) generated successfully!")
