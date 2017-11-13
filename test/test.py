import youtube_dl

options = {
 'format': 'bestaudio[ext=mp3]/bestaudio[ext=m4a]/bestaudio'
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=XhzvgF-y6MA'])