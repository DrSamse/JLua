import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JLua-basic-DrSamse",
    version="0.1.1",
    author="Samuel Nösslböck",
    author_email="samuel.noesslboeck@gmail.com",
    description="A Package for Json-like Lua usement in python",
    install_requires = [
        "lupa"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrSamse/JLua",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)