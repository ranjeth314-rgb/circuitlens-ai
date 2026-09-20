# CircuitLens AI

**On-device electronics component recognition and troubleshooting assistant**

CircuitLens AI is a prototype designed for Snapdragon-powered HP Windows PCs. It uses a webcam/image as input, detects common electronics components when a compatible object-detection model is available, optionally extracts visible text/markings with OCR, and presents structured troubleshooting guidance.

> **Project status:** Prototype / submission-ready starter. Snapdragon hardware benchmarking is not claimed in this repository unless measurements are added by the developer.

## Features

- Webcam or image input
- Component detection pipeline
- Optional YOLO/Ultralytics model support
- Optional OCR support with Tesseract
- Local component knowledge base
- Structured troubleshooting guidance
- Confidence + manual-verification guardrail
- Local-first design; no image upload is required by the application

## Architecture

Camera/Image → Preprocessing → Component Detection → OCR → Local Knowledge Base → Troubleshooting Assistant → Result

## Supported prototype component classes

The starter knowledge base includes:
- resistor
- capacitor
- diode
- LED
- transistor
- IC

The detector only recognizes classes that exist in the loaded model. The repository does **not** claim that a custom electronics detector has already been trained.

## Quick start

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

If `ultralytics` is installed, you can place a compatible YOLO model at `models/best.pt` and the application will attempt detection. Without a model, the app still demonstrates the OCR/knowledge-base/troubleshooting workflow.

For OCR, install the Tesseract executable separately and set `TESSERACT_CMD` if it is not on PATH.

## Optional Qualcomm/Snapdragon deployment

The intended target is a Snapdragon-powered Windows PC. A production deployment can replace or augment the detector runtime with a Qualcomm AI Hub/QNN-compatible model and execution path.

This repository deliberately does not claim NPU acceleration until the model is actually converted, deployed and measured on target Snapdragon hardware.

## Safety

CircuitLens AI provides educational/troubleshooting guidance, not electrical safety certification. Always disconnect power before resistance measurements or physical inspection and follow appropriate lab safety procedures.

## Evaluation plan

Record only measured results:
- component detection precision/recall or mAP
- OCR accuracy
- end-to-end latency
- model size
- CPU/NPU utilization where available
- usability feedback

## Suggested GitHub evidence

Add screenshots/GIFs of the working UI under `assets/demo/`, and add measured benchmark results to the README after testing.

## License

MIT License. See `LICENSE`.
