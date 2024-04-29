from moviepy.editor import VideoFileClip
from moviepy.video.fx.speedx import speedx

def convert_mp4_to_gif_speedup(source_file, target_file, speed_factor):
    # 加载视频文件
    video = VideoFileClip(source_file)
    # 加速视频
    video = speedx(video, factor=speed_factor)
    print("视频已加速\n")
    print("正在写入GIF文件...\n")
    # 写入新的视频文件
    video.write_gif(target_file)
    print("GIF文件已写入\n")
# 使用函数
convert_mp4_to_gif_speedup('D:\\Lab\\组会\\组会记录\\2024年组会\\20240427组会\\output_label.mp4', 'output.gif',1)