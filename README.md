
# 🎓 Vedantu Educational Video Generator

Generate student-friendly YouTube videos from just a topic — including script, voiceover, visuals, and metadata — all in one click.

---

## Problem Solved

Creating quality educational videos is time-consuming:
- Writing a script
-  Recording narration
-  Editing with visuals
-  Generating metadata

This app automates the full process for teachers, tutors, and ed-tech creators.

---

## 💡 Why It Matters

-  Scales content creation
-  Powered by LLaMA3-70B (Groq)
-  Saves hours of manual work
-  Multilingual potential with gTTS
-  Ideal for syllabus-based or explainer content

---

## 🧰 Tech Stack

| Layer          | Technology                         |
|----------------|------------------------------------ |
|  LLM           | LangChain + Groq (LLaMA3-70B)       |
|  TTS           | gTTS (Google Text-to-Speech)        |
|  Video Editing | MoviePy v2.2.1                      |
|  Frontend UI   | Streamlit                           |
|  Output Files  | MP4 Video + Metadata Text           |

---

##  How to Run

1. Clone or download this repo
2. Place a `background.jpg` in the same folder
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run vedantu_video_generator.py
```


##  Example Use Cases

- Class 10 NCERT topics
- Quick explainers (e.g., Photosynthesis, Algebra)
- Coaching institute video production
