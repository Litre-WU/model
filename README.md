# 我的模型
个人常用的模型(滑块验证码暂用京东滑块验证码训练，英文数字验证码识别针对了两个平台训练而成)

# 食用方法

```bash
pip install ultralytics
```

# 英文数字验证码
```python
from ultralytics import YOLO

model = YOLO('capture.pt')

results = model.predict('test.jpg')

results = [[r.names[int(_[-1])] for _ in sorted(r.boxes.data.tolist(), key=lambda x: x[0])] for r in results]

print(results)
```

# 滑块验证码
```python
from ultralytics import YOLO

model = YOLO('slideCaptcha.pt')

results = model.predict('test.jpg')

results = [r.boxes.data.tolist() for r in results]

print(results)
```
