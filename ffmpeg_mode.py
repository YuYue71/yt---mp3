import os
import sys

# 取得 ffmpeg 可執行檔的路徑
def get_ffmpeg_path():
    # 判斷是否為打包後的執行檔
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
        path = os.path.join(base_path, "bin", "ffmpeg.exe")
    # 否則為原始碼執行環境
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_path, "ffmpeg-master-latest-win64-gpl-shared", "bin", "ffmpeg.exe")
    
    return path

FFMPEG_PATH = get_ffmpeg_path()

# 除錯用：啟動時檢查一下路徑對不對
if __name__ == "__main__":
    print(f"測試路徑: {FFMPEG_PATH}")
    print(f"檔案是否存在: {os.path.exists(FFMPEG_PATH)}")