## JSON

To dump data to json file:
```python
output_path = <some_dir> / "some_file.json"  
params = {'a': 1, 'b': 2}
with output_path.open('w') as f:  
    json.dump(params, f, indent=4)
```

to load from json file:
```python
with input_path.open() as f:  
    result = json.load(f)
```


## shutil

```python
shutil.copy(src_path, dst_path)
```
