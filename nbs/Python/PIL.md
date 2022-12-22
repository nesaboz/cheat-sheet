
```python
from PIL import Image
im = Image.open("some path")
im.show()
```

In jupyter one can use only:
```jupyter
im   # or display(im)
```

To create new image:
```python
width, height = 256, 256
mask = Image.new('L', (width, height), 0)
```

Example to draw a polygon:
```python
from PIL import ImageDraw
polygon = [(4, 1), (1, 54), (1, 222), (13, 1)]
ImageDraw.Draw(mask).polygon(polygon, outline=255, fill=255)
```

To load image from png, show bands (i.e. channels):
```python
im = Image.open('example.png')
print(im.getbands())
im.getchannel('R')
```

to convert to tensor:
```python
from torchvision.transforms import ToTensor
tensorizer = ToTensor()
im_tensor = tensorizer(im)
print(im_tensor.shape)
im_tensor[:, :3, :3]
```
