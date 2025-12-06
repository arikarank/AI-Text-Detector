# AI-Text-Detector

Simple Flask app and LSTM model to detect AI-generated vs human-generated text.

## Contents
- `app.py` — Flask application
- `templates/` — HTML templates for UI
- `static/` — CSS and JS
- `model_training/` — training scripts
- `ai_detection_lstm_model.h5` — trained model (excluded from repo by `.gitignore`)
- `tokenizer.pkl` — tokenizer file (excluded from repo by `.gitignore`)

## Setup

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Place the trained model and tokenizer in the project root:

 - `ai_detection_lstm_model.h5`
 - `tokenizer.pkl`

Those files are typically large and are intentionally excluded from the repository. If you don't have them, see `model_training/` for training scripts.

## Run

```powershell
python app.py
```

The app runs on `http://127.0.0.1:5000` by default.

## Notes
- If VS Code reports `Import "tensorflow.keras.models" could not be resolved`, ensure you selected the correct Python interpreter (the one with TensorFlow installed) in the status bar or via `Python: Select Interpreter`.
- For production, do not use `debug=True` and consider serving the model separately or using a smaller API surface.

## License
MIT-style (add your preferred license)
