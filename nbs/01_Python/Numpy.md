```python
import numpy as np
np.random.seed(42)
a = np.random.randn(1,10)
print(a)
print(a.max())
print(a.dtype)
a = a.astype(np.uint8)
print(a)
print(a.max())
print(a.dtype)
print(a.shape)
a = a.squeeze()
print(a.shape)
print(np.expand_dims(a.astype(np.float32), 0).shape)
```

To scale tensor from 0, 255, convert to uint8
```python
b = (np.array(mask_tensor) / np.array(mask_tensor).max() * 255).astype(np.uint8).squeeze()
b.max()
```


```python
b = (np.array(mask_tensor) / np.array(mask_tensor).max()).astype(np.float32).squeeze()
b.max()
```

