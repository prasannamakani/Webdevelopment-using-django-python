from django.shortcuts import render, HttpResponse
import yt_dlp


def video_downloader(request):
    if request.method == "POST":
        url = request.POST.get('link')
        options = {
        
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        try:
            with yt_dlp.YoutubeDL(options) as yt:
                yt.download([url])
            return HttpResponse('Video downloaded successfully.')
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

    return render(request, "second.html")
