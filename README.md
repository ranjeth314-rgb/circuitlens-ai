# Models

Place your trained electronics-component detector here as:

`best.pt`

The application will load it automatically if the Ultralytics-compatible model exists.

Recommended custom classes:
`resistor`, `capacitor`, `diode`, `led`, `transistor`, `ic`.

For Qualcomm deployment, convert/optimize a supported model using the appropriate Qualcomm AI Hub/QNN workflow and document the exact model and measured target-hardware results.
