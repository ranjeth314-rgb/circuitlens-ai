# CircuitLens AI Architecture

## Pipeline

Camera/Image
→ preprocessing
→ component detection
→ OCR
→ local component knowledge
→ troubleshooting response
→ confidence/manual-verification guardrail

## Snapdragon deployment direction

The application is intentionally separated into UI, detection and OCR modules so the detector can later be replaced by a Qualcomm AI Hub/QNN-compatible implementation.

No Snapdragon NPU performance is claimed by the starter repository.

## Privacy

The prototype processes the supplied image locally. It does not contain a cloud upload endpoint.
