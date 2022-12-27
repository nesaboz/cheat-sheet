```python
a = torch.Tensor([1])
b = torch.Tensor([2])
c = torch.stack([a,b], dim=0)
d = torch.stack([a,b], dim=1)
print(c)
print(d)
```

```python
x = torch.randn([32,3,256,256])
```

Formula for output size for Convolutions:
$[(W−K+2P)/S]+1$

For transpose convolution (which upsample there is also `output_padding` that fills only one-side (useful for those 'same' paddings)

Fun fact: Conv2D `Module` initializes all parametres, [functional form](https://pytorch.org/docs/stable/generated/torch.nn.functional.conv2d.html) can take weight (i.e. kernel) as the input.
