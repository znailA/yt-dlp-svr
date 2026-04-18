from fastapi import FastAPI, Query
import yt_dlp

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/dl")
def dl(url: str = Query(...)):
    ydl_opts = {
        "quiet": True,
        "nocheckcertificate": True,
        "format": "best",
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        return {
            "title": info.get("title"),
            "direct_url": info.get("url"),
            "ext": info.get("ext")
        }

    except Exception as e:
        return {"error": str(e)}
