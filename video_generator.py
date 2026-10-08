import subprocess
from pathlib import Path
from gtts import gTTS


def create_video(title, output="output.mp4"):
    output_path = Path(output)
    audio_path = Path("voice.mp3")

    # Hindi test narration
    narration = (
        "नमस्ते दोस्तों। "
        "आज की कहानी बहुत मजेदार है। "
        "एक दिन गणेश जी के साथ एक मजेदार घटना हुई। "
        "आइए सुनते हैं यह छोटी सी मजेदार कहानी।"
    )

    # Create Hindi voice
    tts = gTTS(text=narration, lang="hi")
    tts.save(str(audio_path))

    # Create video + add voice
    command = [
        "ffmpeg",
        "-y",
        "-f", "lavfi",
        "-i", "color=c=black:s=1080x1920:d=10",
        "-i", str(audio_path),
        "-vf",
        (
            "drawtext="
            "fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:"
            "text='Kahani Duniya':"
            "fontcolor=white:"
            "fontsize=80:"
            "x=(w-text_w)/2:"
            "y=(h-text_h)/2"
        ),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-shortest",
        str(output_path)
    ]

    subprocess.run(command, check=True)

    print(f"VIDEO CREATED: {output_path}")


if __name__ == "__main__":
    create_video("Kahani Duniya")
