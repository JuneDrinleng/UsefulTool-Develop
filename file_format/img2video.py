from moviepy.editor import ImageSequenceClip, TextClip, CompositeVideoClip
from natsort import natsorted
import os

img_path='D:\\GitHubStorage\\AnalysisChemistry_WorkCode\\SPTT\\deeplearning_regression\\figure2\\outputs-labels'
output_path='D:\\Lab\\组会\\组会记录\\2024年组会\\20240427组会\\output_label.mp4'
def make_video(image_folder, output_video, fps=24):
    
    # 获取指定文件夹内的所有图片，假设图片是按顺序命名的
    image_files = [os.path.join(image_folder, img) for img in natsorted(os.listdir(image_folder)) if img.endswith((".png", ".jpg", ".jpeg"))]
    
    clips = []
    for i, filename in enumerate(image_files):
        # 每一帧的图片剪辑
        img_clip = ImageSequenceClip([filename], fps=fps)
        
        # 创建文本剪辑，显示帧编号
        txt_clip = TextClip(f"Frame {i + 1}", fontsize=24, color='white', bg_color='black')
        txt_clip = txt_clip.set_position('bottom').set_duration(img_clip.duration)
        
        # 将文本剪辑叠加到图片剪辑上
        video_clip = CompositeVideoClip([img_clip, txt_clip])
        clips.append(video_clip)
    
    # 将所有剪辑组合为单个视频
    final_clip = concatenate_videoclips(clips, method="compose")
    # 创建视频剪辑
    # clip = ImageSequenceClip(image_files, fps=fps)
    
    # 写出视频文件
    clips.write_videofile(output_video, codec='libx264')

# 使用函数
make_video(img_path, output_path, fps=10)