# Calculate BMI from a nested dictionary

d = {
    "ali": {"height": 1.8, "weight": 80},
    "mina": {"height": 1.7, "weight": 90},
    "tina": {"height": 1.6, "weight": 76},
}

for name, info in d.items():
    bmi = info["weight"] / (info["height"] ** 2)
    print(f"{name} BMI: {bmi:.2f}")
