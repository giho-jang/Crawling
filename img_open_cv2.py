# 수정

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('../Crawling/img/lena.png', 0)
image = image.astype(np.float32)

otsu_thr, otsu_mask = cv2.threshold(image, -1, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('Esti', otsu_thr,otsu_mask)

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()

plt.figure(figsize=(6, 3))
plt.subplot(121)
plt.axis('off')
plt.title('original')
plt.imshow(image, cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.title('Otsu threshold')
plt.imshow(otsu_mask, cmap='gray')
plt.tight_layout()
plt.show()
