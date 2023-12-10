# Additional information

## Roadmap

See [ROADMAP](ROADMAP.md) file.

## Deployment

```shell
rm -rf dist/ build/
rm -rf */*.egg-info *.egg-info

python3 -m pip install –-user –-upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
pip3 install twine

twine upload --repository testpypi dist/*

PKG_VERSION_PYPI=1.1.0
pip3 install --index-url https://test.pypi.org/simple/ \
             --extra-index-url https://pypi.org/simple earnings==${PKG_VERSION_PYPI}
```

## Miscellaneous snippets

```shell
tree -L 3 -F -I 'venv|__pycache__|.DS_Store'
```

```shell
openssl dgst -sha256 dist/*.tar.gz
```
