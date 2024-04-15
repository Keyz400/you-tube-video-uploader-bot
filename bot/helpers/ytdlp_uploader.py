import yt_dlp
import os

class YTDLPUploader:
    def __init__(self, bot):
        self.bot = bot

    async def upload_from_ytdlp(self, url):
        try:
            # Download video using yt-dlp
            ytdl_opts = {
                'outtmpl': '%(id)s.%(ext)s',  # Output template
                'format': 'bestvideo+bestaudio/best',  # Video format
            }
            with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                video_file = f"{info['id']}.{info['ext']}"

            # Upload video to YouTube
            message = await self.bot.upload_video(video_file)

            # Clean up downloaded video file
            os.remove(video_file)

            return True, f"Video uploaded successfully: {message.link}"
        except Exception as e:
            return False, f"Error uploading video: {e}"
