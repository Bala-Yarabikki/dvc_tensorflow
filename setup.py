from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="bala",
    description="A small package for dvc dl pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bala-Yarabikki/dvc_tensorflow",
    author_email="balachowdary777@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'tensorflow',
        'matplotlib',
        'numpy',
        'pandas',
        'tqdm',
        'PyYaml',
        'boto3'
    ]
)
