import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whatsapptojson",
    version="1.0",
    author="Ankush Choubey",
    author_email="ankushchoubey@outlook.com",
    description="Converts Whatsapp chat files to dictionary or save it in JSON format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ankschoubey/whatsapptojson",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


