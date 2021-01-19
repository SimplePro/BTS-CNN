# BTS-CNN
-----------------------
BTS 멤버인 뷔, 지민, 정국을 CNN 으로 구별하는 인공지능입니다.

### 정확도 : 약 88%

사용
-----------
# 아래 링크에서 bts_cnn_model.h5 를 다운받고, pred_bts 와 같은 디렉토리에 위치하고 있어야 합니다.  
(모델 크기가 커서 깃헙에는 업로드되지 않았습니다.ㅠㅠ)  
https://drive.google.com/file/d/1ytDmAlJjgBhdCH7AVvMgRixl4FyTpdN-/view?usp=sharing

# 이미지는 픽셀기준 100 x 100 이여야 합니다.

``` python
>>> from pred_bts import BTS_CNN
>>> from keras.preprocessing import image
>>> img = image.load_img("./Jimin.jpg")
>>>
>>> bts_model = BTS_CNN()
>>> pred = bts_model.predict(img)
>>> print(pred)
>>> "Jimin"
```
