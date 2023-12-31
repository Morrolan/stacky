import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stacky-Morrolan",  # Replace with your own username
    version="0.0.1",
    author="Ian Havelock",
    author_email="ian@morrolan.com",
    description="A small humorous package which automatically searches stack overflow for any exception specified",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Morrolan/stacky",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
