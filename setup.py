import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trado",
    version="0.0.1",
    author="Anton Normelius",
    author_email="a.normelius@gmail.com",
    description="Simple file transfer between client and server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/normelius/trado",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
