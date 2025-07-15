import os
from gtts import gTTS
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from moviepy import ImageClip, AudioFileClip, TextClip, CompositeVideoClip
import streamlit as st

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key="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",
    model_name="llama3-70b-8192"
)

st.title("Vedantu Educational Video Generator")
topic = st.text_input("Enter your educational topic (e.g., Class 10 Algebra Basics):")

if topic and st.button("Generate Script + Video"):
    with st.spinner("Generating script..."):
        prompt = f"Write a student-friendly YouTube video script explaining the topic: {topic} in 200-300 words."
        script = llm.invoke([HumanMessage(content=prompt)]).content

        with open("script.txt", "w", encoding="utf-8") as f:
            f.write(script)

        st.success("Script Generated!")
        st.text_area("Video Script", script, height=250)

        st.info("Generating voiceover...")
        tts = gTTS(text=script, lang='en')
        tts.save("voiceover.mp3")

        st.info("Creating video with overlay text...")

        if not os.path.exists("background.jpg"):
            st.error("'background.jpg' is missing. Please add it to the project folder.")
        else:
            audio_clip = AudioFileClip("voiceover.mp3")

            image_clip = (
                ImageClip("background.jpg")
                .with_duration(audio_clip.duration)
                .with_audio(audio_clip)
                .with_fps(24)
            )

            try:
                txt_clip = (
                    TextClip(
                        text=topic,
                        text_config={
                            "font": "DejaVu-Sans",
                            "font_size": 60,
                            "color": "white",
                            "stroke_color": "black",
                            "stroke_width": 2,
                        }
                    )
                    .with_duration(audio_clip.duration)
                    .with_position("center")
                )
            except Exception as e:
                st.error(f"Text rendering failed: {e}")
                txt_clip = None

            # Combine clips
            if txt_clip:
                final_video = CompositeVideoClip([image_clip, txt_clip])
            else:
                final_video = image_clip

            final_video.write_videofile("final_video.mp4", codec="libx264", audio_codec="aac")

            st.video("final_video.mp4")
            st.success("Video created successfully!")

        st.info("Generating YouTube metadata...")
        meta_prompt = f"Based on the script below, write a YouTube video title, a 100-word description, and 10 hashtags:\n\n{script}"
        metadata = llm.invoke([HumanMessage(content=meta_prompt)]).content

        with open("metadata.txt", "w", encoding="utf-8") as f:
            f.write(metadata)

        st.success("Metadata Generated!")
        st.text_area("YouTube Metadata", metadata, height=200)
