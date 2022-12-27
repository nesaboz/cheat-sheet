
```python
torch.nn.BatchNorm2d(
_num_features_,
_eps=1e-05_,
_momentum=0.1_,
_affine=True_,
_track_running_stats=True_,
_device=None_,
_dtype=None_
)
```


One must define all layers in the `__init__` in order to initialize them. Remeber that `forward` method will be called during `training` so **no layers with parameters** should be defined there. 