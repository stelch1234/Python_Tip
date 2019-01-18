# 시각화
import matplotlib.pyplot as plt
# 워드클라우드
from wordcloud import WordCloud
# image masking
from PIL import Image

# mask할 이미지(png형식)
icon = Image.open('/~image_path .png').convert("RGBA")
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)

# 워드클라우드에 사용할 폰트를 파이썬이 있는 폴더에 넣어주세요
# data 우리가 보고자할 데이터 입력
tmp_data = dict(data)
wordcloud = WordCloud(font_path = '/~font_path .otf',
                      width = 800,
                      height = 800,
                      relative_scaling = 0.2,
                      background_color = 'white',
                      mask = mask).generate_from_frequencies(tmp_data)

# y, x축 제거
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()