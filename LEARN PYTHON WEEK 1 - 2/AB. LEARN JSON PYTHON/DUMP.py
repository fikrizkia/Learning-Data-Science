import json

data_config = {
    "model_name": "Random Forest Classifier",
    "n_estimators": 100,
    "max_depth": 10,
    "use_gpu": False,
}

teks = json.dumps(data_config, indent=1)

print(teks)