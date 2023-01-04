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

For transpose convolution (which upsample there is also `output_padding` that fills only one-side (useful for those 'same' paddings). 
It is a non-symetric padding of the output image that enables us to get an even size image.
        

Fun fact: Conv2D `Module` initializes all parametres, [functional form](https://pytorch.org/docs/stable/generated/torch.nn.functional.conv2d.html) can take weight (i.e. kernel) as the input.

```python
torch.manual_seed(12)
x = torch.rand(2,2,2)
print(x)
print(x[x > 0.3])
```

Logical operations:
```python
torch.logical_and
```

Get unique values, convert to float values:
```python
some_tensor.unique()
some_tensor.float()
some_tensor.dtype
some_tensor.flatten()
some_tensor[:,(0,),:,:]  # slices but preserves length of original shape
some_tensor[:,0,:,:]  # reduces length of original shape
```

To cast tensor as different [type](https://pytorch.org/docs/stable/tensors.html):
```python
some_tensor.type(torch.uint8)
some_tensor.float()
some_tensor.int()
some_tensor.double()
some_tensor.long()
some_tensor.short()
```

```python
torch.all(input)  # boolean all operation
torch.argmax(input, dim, keepdim=False)  # argmax operation
torch.clone(input)
```
