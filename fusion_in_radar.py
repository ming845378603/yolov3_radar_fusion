import random
import time

import cv2
import matplotlib.pyplot as plt
import numpy as np

import init
import utils


def draw(im, label, confidence, left, top, right, bottom, distance):
    label_confidence = '%s:%.2f' % (label, confidence)
    rand = random.randint(0, 255)
    # 绘制bbox
    cv2.putText(im, label_confidence, (left, top - 7), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.rectangle(im, (left, top), (right, bottom),
                  (int(colours[rand % 32, 0]), int(colours[rand % 32, 1]), int(colours[rand % 32, 2])), 3)

    # 绘制bbox下沿中心坐标
    y = int(bottom)
    x = (left + right) // 2
    cv2.circle(im, (x, y), 4, (255, 178, 50), thickness=-1)

    # 绘制竖直线
    cv2.line(im, (640, 0), (640, 720), (0, 0, 255), thickness=1)

    # 绘制distance
    cv2.putText(im, distance + 'm', (left, bottom + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)


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

            # 获取相机坐标
            rect_roi = [left, top, right, bottom]
            camera_xyz, distance = utils.calculate_depth(rect_roi)
            print('camera_xyz: ')
            print(camera_xyz)

            # 获取世界坐标
            camera_xyz_in_world = utils.convert_to_world(camera_xyz)
            print('camera_xyz_in_world: ')
            print(camera_xyz_in_world)

            # 画图
            draw(image, label, confidence, left, top, right, bottom, distance)
            camera_frame.append([camera_xyz_in_world[0, 0], camera_xyz_in_world[0, 1], camera_xyz_in_world[0, 2]])
            confidences.append(confidence)
            classes.append(label)

            # 计算FPS
            fps = 1. / float(time.time() - s)
            cv2.putText(image, 'FPS: {:.1f}'.format(fps), (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    return image, np.array(camera_frame), confidences, classes


def process_radar(radar_all_in_world, factor, count):
    radar_count = int(count / factor)
    radar_frame = radar_all_in_world[radar_count, :, :]

    return radar_frame


def fusion_in_radar(camera_frame, confidences, classes, radar_frame):
    # 画图
    plt.cla()
    plt.xlabel('x')
    plt.ylabel('z')
    plt.xlim(xmax=50, xmin=-50)
    plt.ylim(ymax=100, ymin=0)
    colors1 = '#00CED1'  # 点的颜色
    colors2 = '#DC143C'
    area = np.pi * 4 ** 2  # 点面积
    print('camera_frame:', camera_frame)
    print('radar_frame:', radar_frame)
    plt.ion()
    plt.scatter(camera_frame[:, 0], camera_frame[:, 2], s=area, c=colors1, alpha=0.4, label='camera')
    plt.scatter(radar_frame[:, 0], radar_frame[:, 2], s=area, c=colors2, alpha=0.4, label='radar')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    args, Detector, colours, cap, outputFile, out, radar_all_in_world, factor = init.init()
    count = -1
    while True:
        count += 1
        # 从视频流中读取一张图像，ret为读取成功/失败标识，frame为当前视频帧
        ret, frame = cap.read()
        if ret:
            # 处理camera
            im, camera_frame, confidences, classes = process_image(frame, args.det_conf_thresh, colours)
            # 模拟radar数据
            radar_all_in_world = np.random.randint(1, 50, size=[1000, 2, 4])
            # 处理radar
            radar_frame = process_radar(radar_all_in_world, factor, count)
            # fusion
            fusion_in_radar(camera_frame, confidences, classes, radar_frame)

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
