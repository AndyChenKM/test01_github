import numpy as np
import matplotlib.pyplot as plt


# IOU
# box[x1, y1, x2, y2, c]
def iou(box, boxes, isMin=False):
    # 1.两个框的面积
    box_area = (box[2] - box[0]) * (box[3] - box[1])
    boxes_area = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
    # 2.交集
    xx1 = np.maximum(box[0], boxes[:, 0])
    yy1 = np.maximum(box[1], boxes[:, 1])
    xx2 = np.minimum(box[2], boxes[:, 2])
    yy2 = np.minimum(box[3], boxes[:, 3])
    # 3.是否相交
    w = np.maximum(0, xx2-xx1)
    h = np.maximum(0, yy2-yy1)
    # 4.计算交集面积
    inter = w * h
    # 5.计算IOU（两种情况）
    if isMin:
        # 分母为较小的面积
        ovr = np.true_divide(inter, np.minimum(box_area, boxes_area))
    else:
        ovr = np.true_divide(inter, (box_area + boxes_area - inter))

    return ovr


# NMS
def nms(boxes, thresh=0.3, isMin=False):
    # 1.判断框是否为空
    if boxes.shape[0] == 0:
        return np.array([])
    # 2.排序
    _boxes = boxes[(-boxes[:, 4]).argsort()]
    # 3.储存列表
    r_boxes = []
    # 4.循环，筛选
    while _boxes.shape[0] > 1:
        # 4.1 取出第一个框
        box_a = _boxes[0]
        # 4.2 取出剩余的框
        boxes_b = _boxes[1:]
        # 4.3 储存第一个框
        r_boxes.append(box_a)
        # 4.4 筛选
        index = np.where(iou(box_a, boxes_b, isMin) < thresh)
        # 4.5 条件控制
        _boxes = boxes_b[index]
    # 5.储存最后一个框
    if _boxes.shape[0] > 0:
        r_boxes.append(_boxes[0])

    return np.stack(r_boxes)


# 可视化
def show_rect(bs):
    fig, ax = plt.subplots()

    for i in bs:
        rect = plt.Rectangle((i[0], i[1]), i[2] - i[0], i[3] - i[1], fill=False, color='red',
                      linewidth=3)
        ax.add_patch(rect)
    plt.axis("equal")
    plt.show()

if __name__ == '__main__':
    # a = np.array([1,1,11,11])
    # b = np.array([[1,1,11,11],[1,1,10,10],[11,11,20,20]])
    # print(iou(a, b,isMin=True))
    # show_rect(b)

    bs = np.array([[1, 1, 10, 10, 40], [1, 1, 9, 9, 10], [9, 8, 13, 20, 15], [6, 11, 18, 17, 13]])
    show_rect(bs)
    print(nms(bs))
    show_rect(nms(bs, thresh=0.1))