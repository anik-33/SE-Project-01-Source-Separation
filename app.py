import streamlit as st
import os
import subprocess

# random comment
def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join("uploaded_files", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except:
        return False

# Function to process audio file with demucs
def process_audio_with_demucs(audio_file_path):
    try:
        subprocess.run(['demucs',"--mp3", audio_file_path], check=True)
        return True
    except subprocess.CalledProcessError as e:
        st.error(f"Error executing demucs command: {e}")
        return False

# Create a directory to save uploaded files
if not os.path.exists('uploaded_files'):
    os.mkdir('uploaded_files')

st.title('SoundForge: Agile CI/CD for Improved Audio Separation')

uploaded_file = st.file_uploader("Choose an audio file", type=['mp3', 'wav'])

if uploaded_file is not None:
    # Display the file details
    file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}

    if save_uploaded_file(uploaded_file):
        st.success("File Saved Successfully")
        
        # Display audio player for original file
        audio_file_path = os.path.join("uploaded_files", uploaded_file.name)
        audio_bytes = open(audio_file_path, "rb").read()

        # Display side-by-side columns
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Original Audio")
            st.audio(audio_bytes, format='audio/mp3', start_time=0)

        with col2:
            st.markdown("### Processed Audio (Demucs)")
            if st.button("Process Audio with Demucs"):
                if process_audio_with_demucs(audio_file_path):
                    processed_audio_file_path = os.path.join("separated", "htdemucs", os.path.splitext(uploaded_file.name)[0], "vocals.mp3")
                    if os.path.exists(processed_audio_file_path):
                        processed_audio_bytes = open(processed_audio_file_path, "rb").read()
                        st.audio(processed_audio_bytes, format='audio/mp3', start_time=0)
                    else:
                        st.error("Processed audio file not found.")
                else:
                    st.error("Error processing audio with Demucs.")

