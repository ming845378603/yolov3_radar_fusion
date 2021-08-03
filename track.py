import argparse
import time

import cv2
import numpy as np

from sort import Sort
from yolo import YOLO


def parse_args():
    """
    参数设置
    """
    parser = argparse.ArgumentParser()
    # yolov3配置文件
    parser.add_argument('--cfg', default='model/yolov3.cfg')
    # yolov3权重文件
    parser.add_argument('--weights', default='model/yolov3.weights')
    # 图片尺寸设置
    parser.add_argument('--image_resize', default=(608, 480), type=int)
    # 置信度阈值设置
    parser.add_argument('--det_conf_thresh', default=0.3, type=float)  # car:0.3,car2:0.4
    # 最大允许丢失帧数
    parser.add_argument('--sort_max_age', default=5, type=int)
    #
    parser.add_argument('--sort_min_hit', default=3, type=int)
    # 输入文件
    parser.add_argument('--video', default="input/1225_17.mp4")

    return parser.parse_args()


tol_obj_num = 0  # 当前目标个数
cur_obj_num = 0  # 累计目标个数
all_pts = {}  # 记录目标的中心坐标
all_ids = []  # 记录所有出现过的目标ID


def track(frame, det_conf_thresh, colours):
    """
    跟踪算法核心
    """
    # 计时开始
    s = time.time()
    # 当前帧检测结果
    result, labels = Detector.detect(frame, args.det_conf_thresh)
    # copy视频帧原图
    im = frame.copy()
    # 当前帧成功跟踪的ID数
    keep_line_idx = []

    if len(result) > 0:
        det = result[:, 0:5]
        print(result)
        print(det)
        trackers = mot_tracker.update(det)
        global cur_obj_num
        cur_obj_num = len(trackers)
        for d in trackers:
            xmin = int(d[0])
            ymin = int(d[1])
            xmax = int(d[2])
            ymax = int(d[3])
            id = int(d[4])
            print("ID:", id)
            keep_line_idx.append(id)

            global tol_obj_num
            if id not in all_ids:
                tol_obj_num += 1
                all_ids.append(id)

            if id in all_pts:
                all_pts[id].append(((xmin + xmax) // 2, (ymin + ymax) // 2))
            else:
                all_pts[id] = [((xmin + xmax) // 2, (ymin + ymax) // 2)]
            cv2.putText(im, 'ID:%d' % d[4], (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.rectangle(im, (xmin, ymin), (xmax, ymax),
                          (int(colours[id % 32, 0]), int(colours[id % 32, 1]), int(colours[id % 32, 2])), 3)

    # 画轨迹跟踪线
    for l, pts in all_pts.items():
        if l in keep_line_idx:
            for i in range(1, len(pts)):
                if pts[i - 1] is None or pts[i] is None:
                    continue
                # thickness = int(np.sqrt(64 / float(i + 1)) * 2.5)
                cv2.line(im, pts[i - 1], pts[i],
                         (int(colours[l % 32, 0]), int(colours[l % 32, 1]), int(colours[l % 32, 2])), 2)
    # 计算FPS
    fps = 1. / float(time.time() - s)
    # 绘制左上角
    cv2.putText(im, 'FPS: {:.1f}'.format(fps), (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
    cv2.putText(im, 'Current Obj Num: {}'.format(cur_obj_num), (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0),
                2)
    cv2.putText(im, 'Total Obj Num: {}'.format(tol_obj_num), (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
    return im


def trackOut():
    # 参数设置
    args = parse_args()
    # 初始化YOLOv3检测算法
    Detector = YOLO(args.cfg, args.weights, args.image_resize)
    # 初始化Sort匹配算法
    mot_tracker = Sort(args.sort_max_age, args.sort_min_hit)
    # 生成32行，3列的随机数矩阵，用于绘制检测框和跟踪轨迹
    colours = np.random.rand(32, 3) * 255
    # 读取视频文件
    cap = cv2.VideoCapture(args.video)
    # 定义输出文件，源文件名 + '_Out.avi'
    outputFile = 'output/' + args.video[6:-4] + '_Out.avi'
    # 输出文件编码参数：该参数是MPEG-4编码类型，文件名后缀为.avi
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter(outputFile, fourcc, 30.0,
                          (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))


if __name__ == "__main__":
    # 参数设置
    args = parse_args()
    # 初始化YOLOv3检测算法
    Detector = YOLO(args.cfg, args.weights, args.image_resize)
    # 初始化Sort匹配算法
    mot_tracker = Sort(args.sort_max_age, args.sort_min_hit)
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

    # 跟踪处理
    while True:
        # 从视频流中读取一张图像，ret为读取成功/失败标识，frame为当前视频帧
        ret, frame = cap.read()
        if ret == True:
            im = track(frame, args.det_conf_thresh, colours)  # 跟踪处理
            # 显示当前帧的跟踪结果
            cv2.imshow("Tracking", im)
            # 将跟踪结果写入视频流out
            out.write(im.astype(np.uint8))
            # 间隔1ms，播放下一帧。或者按'esc'键退出，它的ASCII码为27
            if cv2.waitKey(1) & 0xff == 27:
                break
        else:
            print("Done processing !!!")
            print("Output file is stored as ", outputFile)
            break

    # 释放视频流
    cap.release()
    # 关闭所有窗口
    cv2.destroyAllWindows()
