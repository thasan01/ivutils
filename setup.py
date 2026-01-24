import os
from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

with open("README.md") as fp:
    desc_text = fp.read()

setup(
    name="ivutils",
    version="0.0.7",
    license="MIT license",
    long_description=desc_text,
    long_description_content_type= "text/markdown",
    url="https://github.com/thasan01/ivutils",
    keywords=[
            "computer-vision", "opencv", "image-processing", "video-processing", 
            "imaging", "utilities",  "transformation", "automation", "task"
        ],    
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
    entry_points={
        'console_scripts': [
            'ivutils = ivutils.cli:run',
        ],
    },
)
