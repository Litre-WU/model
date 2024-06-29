# -*- coding: utf-8 -*-
# Author: Litre WU
# E-mail: litre-wu@tutanota.com
# Software: PyCharm
# File: train
# Date: 2024-4-26
from ultralytics import YOLO, settings

settings.update({'runs_dir': 'runs', 'tensorboard': False})


def main(*arg, **kwargs):
    model = YOLO('yolov8n.pt')
    model.train(data='capture_slide/capture_slide.yaml', epochs=100, workers=32, cache=False, exist_ok=True, val=True)


if __name__ == '__main__':
    main()
