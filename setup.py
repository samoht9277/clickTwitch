import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clickTwitch",
    version="1.3.3-1",
    author="samoht9277",
    author_email="totobighouse@gmail.com",
    description="clickTwitch is an automation tool that claims your twitch reward while watching a stream",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samoht9277/clickTwitch",
    packages=setuptools.find_packages(),
    install_requires=[
        'mouse',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0'
)
