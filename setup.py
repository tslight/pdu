import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdu",
    version="0.0.3",
    author="Toby Slight",
    author_email="tobyslight@gmail.com",
    description="Python Disk Usage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tslight/pdu",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'pdu = pdu.__main__:main',
        ],
    }
)
