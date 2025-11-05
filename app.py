import streamlit as st
import pipeline

st.set_page_config(page_title="EfficientNetV2 DeepFake Detector", layout="wide")

st.title("🎭 EfficientNetV2 DeepFakes Detector")
st.write("Detect DeepFake Images and Videos using frame-by-frame detection.")

tab1, tab2 = st.tabs(["🖼️ Image Inference", "🎥 Video Inference"])

with tab1:
    st.header("Upload Image to Detect DeepFake")
    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
        with st.spinner("Analyzing Image..."):
            result = pipeline.deepfakes_image_predict(uploaded_image)
        st.success(result)

with tab2:
    st.header("Upload Video to Detect DeepFake")
    uploaded_video = st.file_uploader("Upload a Video", type=["mp4", "mov", "avi"])
    if uploaded_video:
        st.video(uploaded_video)
        with st.spinner("Analyzing Video..."):
            result = pipeline.deepfakes_video_predict(uploaded_video)
        st.success(result)
