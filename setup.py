import setuptools

with open("README.md") as file:
    read_me_description = file.read()

with open("requirements.txt") as file:
    requirements = file.read()

setuptools.setup(
    name="RWLock",
    version="0.1",
    author="egor.bakharev",
    author_email="progr18@pancir.it",
    description="Read-Write Lock Python implementation",
    long_description=read_me_description,
    install_requires=requirements.splitlines(),
    long_description_content_type="text/markdown",
    url="https://git.pancir.it/egor.bakharev/DTKLP-wrapper",
    packages=['rwlock'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)