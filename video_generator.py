import subprocess
from pathlib import Path


def create_video(title, output="output.mp4"):
    output_path = Path(output)

    # Simple vertical 9:16 test video
    command = [
        "ffmpeg",
        "-y",
        "-f", "lavfi",
        "-i", "color=c=black:s=1080x1920:d=10",
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
        "-t", "10",
        str(output_path),
    ]

    subprocess.run(command, check=True)

    print(f"VIDEO CREATED: {output_path}")


if __name__ == "__main__":
    create_video("Kahani Duniya")
