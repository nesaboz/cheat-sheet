
```
pip install pytest
```

You will need `pytest.ini` in the root:
```
[pytest]
pythonpath = ''
```
`pythonpath` adds a path to `sys.path` relative to the root so the imports in test files work.

To discover and run all tests run in terminal:
```zsh
pytest
```

To run only specific tests:
```zsh
pytest filename.py
```

[docs](https://docs.pytest.org/en/7.1.x/example/pythoncollection.html)