import yt_dlp
import re

async def search_youtube(query: str) -> str:
    ydl_opts = {'format': 'bestaudio/best'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        return f"https://www.youtube.com/embed/{info['id']}"
