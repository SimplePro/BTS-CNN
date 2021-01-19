# BTS-CNN
-----------------------
#### 정확도 : 약 88%

사용
-----------
아래 링크에서 bts_cnn_model.h5 를 다운받고, pred_bts 와 같은 디렉토리에 위치하고 있어야 합니다.
https://drive.google.com/file/d/1ytDmAlJjgBhdCH7AVvMgRixl4FyTpdN-/view?usp=sharing


``` python
>>> from pred_bts import BTS_CNN
>>> from keras.preprocessing import image
>>> img = image.load_img("Jimin.jpg")
>>>
>>> bts_model = BTS_CNN()
>>> pred = bts_model.predict(img)
>>> print(pred)
>>> "Jimin"
```
