from setuptools import setup, find_packages

setup(
    name="viutils",
    version="0.0.1",
    license="MIT license",
    packages=find_packages(),
    install_requires=["opencv-python~=4.10.0.84",
                      "numpy~=2.1.3",
                      "pillow~=11.0.0"
                      ]
)
