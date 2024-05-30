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
convert_mp4_to_gif_speedup('Gp_traj_outputs_label_scatter.mp4', 'Gp_traj_outputs_label_scatter.gif',1)
# convert_mp4_to_gif_speedup('eta_outputs_label_scatter.mp4', 'eta_outputs_label_scatter.gif',1)
# convert_mp4_to_gif_speedup('etas_outputs_label_scatter.mp4', 'etas_outputs_label_scatter.gif',1)