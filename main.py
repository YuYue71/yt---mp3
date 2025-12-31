import yt_dlp
import os
import sys
from ffmpeg_mode import FFMPEG_PATH

def progress_hook(d):
    if d['status'] == 'downloading':
        # 取得進度百分比、下載速度與剩餘時間
        percent = d.get('_percent_str', '0.0%')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        
        # 顯示格式化的下載進度
        sys.stdout.write(f"\r[下載中] {percent} | 速度: {speed} | 剩餘時間: {eta}   ")
        sys.stdout.flush()
        
    # 下載完成後的訊息
    elif d['status'] == 'finished':
        sys.stdout.write("\n[完成] 下載完畢，正在進行 MP3 轉碼...\n")
        sys.stdout.flush()

def download_youtube_as_mp3(url):
    output_dir = 'mp3-OK'
    
    # 檢查資料夾是否存在，不存在則建立 (避免程式報錯)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"已建立資料夾: {output_dir}")
        
    # 設定 yt-dlp 參數
    ydl_opts = {
        'format': 'bestaudio/best',         # 選擇最佳音質
        'ffmpeg_location': FFMPEG_PATH,
        'restrictfilenames': True,          # 限制檔名使用安全字元
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'progress_hooks': [progress_hook],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',    # 提取音訊
            'preferredcodec': 'mp3',        # 轉為 mp3
            'preferredquality': '192',      # 音質 192kbps
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),     # 設定輸出檔名為「影片標題.mp3」
    }

    # 使用 yt-dlp 下載並轉換音訊
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("正在解析並下載...")
            ydl.download([url])
            print("下載完成！")
            print(f"檔案已儲存至: {os.path.abspath(output_dir)}")
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    print("歡迎使用 YouTube 轉 MP3 下載器")
    print("-# \"幽月YuYue\" 保有所有權利")
    video_url = input("請輸入 YouTube 網址: ")
    download_youtube_as_mp3(video_url)