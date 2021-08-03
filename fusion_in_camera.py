import random
import time

import cv2
import numpy as np

import init
import utils


def draw(im, label, confidence, left, top, right, bottom):
    label_confidence = '%s:%.2f' % (label, confidence)
    rand = random.randint(0, 255)
    # 绘制bbox
    cv2.putText(im, label_confidence, (left, top - 7), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.rectangle(im, (left, top), (right, bottom),
                  (int(colours[rand % 32, 0]), int(colours[rand % 32, 1]), int(colours[rand % 32, 2])), 3)


def process_image(frame, det_conf_thresh, colours):
    # 计时开始
    s = time.time()

    # 当前帧检测结果
    result, labels = Detector.detect(frame, det_conf_thresh)

    # copy视频帧原图
    image = frame.copy()

    camera_frame, confidences, classes = [], [], []
    if len(result) > 0:
        for index in range(len(result)):
            left = int(result[index, 0])
            top = int(result[index, 1])
            right = int(result[index, 2])
            bottom = int(result[index, 3])
            confidence = result[index, 4]
            label = labels[index]
            # 过滤不想要的label
            if label != 'car':
                continue

            # 画图
            draw(image, label, confidence, left, top, right, bottom)
            camera_frame.append([left, top, right, bottom])
            confidences.append(confidence)
            classes.append(label)

    # 计算FPS
    fps = 1. / float(time.time() - s)
    cv2.putText(image, 'FPS: {:.1f}'.format(fps), (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    return image, camera_frame, confidences, classes


def process_radar(image, radar_all_in_world, factor, count):
    # copy视频帧原图
    im = image.copy()

    radar_count = int(count / factor)
    radar_frame = radar_all_in_world[radar_count, :, :]

    radar_frame_uv = []
    if len(radar_frame) > 0:
        for index in range(len(radar_frame)):
            radar_xyz = np.mat(radar_frame[index, 0:3])
            print('radar_xyz: ')
            print(radar_xyz)

            # 获取世界坐标
            redar_xyz_in_world = utils.convert_to_world(radar_xyz)
            print('redar_xyz_in_world: ')
            print(redar_xyz_in_world)

            # 获取像素坐标
            radar_uv = utils.convert_to_uv(redar_xyz_in_world)
            print('radar_uv: ')
            print(radar_uv)

            # 绘制
            cv2.circle(im, (radar_uv[0] % 1280, radar_uv[1] % 720), 6, (0, 0, 255), thickness=-1)
            radar_frame_uv.append(radar_uv)

    return im, radar_frame_uv


def fusion_in_image(camera_frame, confidences, classes, radar_frame):
    # TODO
    a = []


if __name__ == "__main__":
    args, Detector, colours, cap, outputFile, out, radar_all_in_world, factor = init.init()
    count = -1
    while True:
        count += 1
        # 从视频流中读取一张图像，ret为读取成功/失败标识，frame为当前视频帧
        ret, frame = cap.read()
        if ret:
            # 处理image
            im, camera_frame, confidences, classes = process_image(frame, args.det_conf_thresh, colours)

            # 模拟radar数据
            radar_all_in_world = np.random.randint(1, 100, size=[1000, 2, 4])

            # 处理radar
            im, radar_frame_uv = process_radar(im, radar_all_in_world, factor, count)
            # # fusion
            # fusion_in_image(camera_frame, confidences, classes, radar_frame_uv)

            # 显示当前帧的结果
            cv2.imshow("Detection", im)
            # 将检测结果写入视频流out
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
