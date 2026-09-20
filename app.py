import streamlit as st
from PIL import Image
import numpy as np

from src.pipeline import CircuitLensPipeline

st.set_page_config(page_title="CircuitLens AI", page_icon="🔬", layout="wide")

st.title("🔬 CircuitLens AI")
st.caption("Local-first electronics component recognition and troubleshooting prototype")

@st.cache_resource
def get_pipeline():
    return CircuitLensPipeline()

pipeline = get_pipeline()

col1, col2 = st.columns([1, 1])

with col1:
    source = st.radio("Input", ["Upload image", "Camera"], horizontal=True)
    image = None

    if source == "Upload image":
        uploaded = st.file_uploader("Upload an electronics image", type=["jpg", "jpeg", "png"])
        if uploaded:
            image = Image.open(uploaded).convert("RGB")
    else:
        camera = st.camera_input("Capture an electronics image")
        if camera:
            image = Image.open(camera).convert("RGB")

    if image:
        st.image(image, caption="Input image", use_container_width=True)

with col2:
    st.subheader("Analysis")

    if image:
        result = pipeline.analyze(image)

        if result["detections"]:
            for d in result["detections"]:
                st.markdown(f"### {d['label']} — {d['confidence']:.0%}")
                info = pipeline.knowledge(d["label"])
                st.write(f"**Function:** {info['function']}")
                st.write(f"**Checks:** {info['checks']}")
                st.write(f"**Troubleshooting:** {info['troubleshooting']}")
        else:
            st.info("No compatible detector model was found or no supported component was detected.")
            st.write("You can still inspect the OCR text below.")

        if result["ocr_text"]:
            st.write("**Detected marking/text:**")
            st.code(result["ocr_text"])

        st.warning(
            "Manual verification required. This prototype is educational and must not "
            "be used as a substitute for electrical safety procedures."
        )
    else:
        st.info("Upload an image or capture one with the camera to begin.")

st.divider()
st.caption("Prototype status: Snapdragon deployment and NPU performance must be measured on target hardware before claiming acceleration.")
