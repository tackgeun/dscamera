![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dscamera)
![pytest](https://github.com/matsuren/dscamera/workflows/pytest/badge.svg?branch=master)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/matsuren/dscamera)](https://github.com/matsuren/dscamera/releases)
[![codecov](https://codecov.io/gh/matsuren/dscamera/branch/master/graph/badge.svg)](https://codecov.io/gh/matsuren/dscamera)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub](https://img.shields.io/github/license/matsuren/dscamera)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# Double Sphere Camera Model

Python library of Double Sphere Camera Model for Supporting [Leopard Imaging Owl fisheye camera](https://leopardimaging.com/product/automotive-cameras/cameras-by-interface/maxim-gmsl-2-cameras/li-ar0234cs-gmsl2-owl/li-ar0234cs-gmsl2-owl/).

Reference:

```
V. Usenko, N. Demmel, and D. Cremers, "The Double Sphere Camera Model", Proc. of the Int. Conference on 3D Vision (3DV), 2018.
```

## Requirements
Python >= 3.6 with numpy and opencv.

## Installation
Run the following command.
```bash
git clone https://github.com/matsuren/dscamera
cd dscamera
python setup.py install
```

## Example LI Owl Fisheye Camera
Please check `example-li-owl` folder for fisheye image rectifications.

Input fisheye image:

<img src="./example-li-owl/sample2.png" width="350px">

Output zoom-in perspective image:

<img src="./example-li-owl/zoomin_perspective2.png" width="300px">

Output zoom-out perspective image:

<img src="./example-li-owl/zoomout_perspective2.png" width="350px">


## Camera calibration
Please use [Basalt](https://vision.in.tum.de/research/vslam/basalt) for fisheye camera calibration. The detail instruction is available [here](https://gitlab.com/VladyslavUsenko/basalt/blob/master/doc/Calibration.md).


## Example
Please check `example` folder for fisheye image rectifications.

Input fisheye image:

<img src="./example/sample.jpg" width="300px">

Output perspective image:

<img src="./example/perspective.jpg" width="250px">

Output equirectangular image:

<img src="./example/equirect.jpg" width="500px">
