import argparse

import cv2
import numpy as np

from yolo import YOLO


def init():
    # 参数
    args = parse_args()
    # 初始化YOLOv3
    Detector = YOLO(args.cfg, args.weights, args.image_resize)
    # 生成32行，3列的随机数矩阵，用于绘制检测框和跟踪轨迹
    colours = np.random.rand(32, 3) * 255
    # 读取视频文件
    cap = cv2.VideoCapture(args.video)
    # 定义输出文件，源文件名 + '_Out.avi'
    outputFile = 'output/' + args.video[6:-4] + '_Out.avi'
    # 输出文件编码参数：该参数是MPEG-4编码类型，文件名后缀为.avi
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    # 创建视频流，写入对象，30为播放帧率，后面两个参数为视频帧的大小
    out = cv2.VideoWriter(outputFile, fourcc, 30.0,
                          (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    # 读取雷达数据
    radar_all_in_world = read_radar_data(args.radar_data_path)
    # 时间标尺
    radar_data_len = len(radar_all_in_world)
    camera_data_len = cap.get(7)
    print('radar_data_len:', radar_data_len)
    print('camera_data_len:', camera_data_len)
    # TODO
    # if camera_data_len == 0 or radar_data_len == 0:
    #     print('camera_data or radar_data is empty!')
    #     sys.exit(0)
    # factor = (camera_data_len + 1) / radar_data_len
    factor = 1
    return args, Detector, colours, cap, outputFile, out, radar_all_in_world, factor


def parse_args():
    """
    参数设置
    """
    parser = argparse.ArgumentParser()
    # yolov3配置文件
    parser.add_argument('--cfg', default='model/yolov3.cfg')
    # yolov3权重文件
    parser.add_argument('--weights', default='model/yolov3.weights')
    # 图片尺寸
    parser.add_argument('--image_resize', default=(608, 480), type=int)
    # 置信度阈值
    parser.add_argument('--det_conf_thresh', default=0.5, type=float)
    # 输入视频数据
    parser.add_argument('--video', default="input/7_1.mp4")
    # 输入雷达数据 TODO
    parser.add_argument('--radar_data_path', default="input/...")

    return parser.parse_args()


def read_radar_data(dataPath):
    radar_all_in_world = []
    # TODO
    return radar_all_in_world
