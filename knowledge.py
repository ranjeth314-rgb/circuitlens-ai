COMPONENT_KNOWLEDGE = {
    "resistor": {
        "function": "Limits or sets current and voltage in a circuit.",
        "checks": "Verify resistance value, physical condition, solder joints and continuity with power removed.",
        "troubleshooting": "Check whether the measured resistance matches the expected value and whether the resistor is correctly connected."
    },
    "capacitor": {
        "function": "Stores electrical charge and is commonly used for filtering, coupling and timing.",
        "checks": "Check value, voltage rating, polarity for polarized types, physical damage and solder joints.",
        "troubleshooting": "Verify polarity and rating; inspect for swelling or leakage and compare measured behavior with the circuit requirement."
    },
    "diode": {
        "function": "Primarily allows current to flow in one direction.",
        "checks": "Verify cathode/anode orientation and diode condition with power removed.",
        "troubleshooting": "Check polarity, forward/reverse behavior and whether the part is the correct type for the circuit."
    },
    "led": {
        "function": "Emits light when forward biased with appropriate current limiting.",
        "checks": "Verify anode/cathode orientation and the presence of an appropriate current-limiting resistor.",
        "troubleshooting": "Check polarity, supply voltage, resistor value and LED condition."
    },
    "transistor": {
        "function": "Used for switching or amplification.",
        "checks": "Verify transistor type, pinout, orientation, bias conditions and solder joints.",
        "troubleshooting": "Confirm the pin configuration from the datasheet before applying power and check expected bias voltages."
    },
    "ic": {
        "function": "Integrated circuit containing electronic functions in a semiconductor package.",
        "checks": "Verify part number, pin-1 orientation, supply voltage, grounding and connections.",
        "troubleshooting": "Confirm the exact datasheet pinout and supply requirements before diagnosing circuit behavior."
    },
}
