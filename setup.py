from setuptools import setup
import setuptools
setup(
    name="pycitrine",
    version='0.0.1',
    author="CintagramABP",
    description="[WIP] new data management in python",
    long_description="[WIP] new data management in python",
    url="",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[],
    include_package_data=True,
    extras_require={
        "testing": [
            "pytest",
            "pytest-cov",
        ],
    },
    package_data={"PyCitrine": ["py.typed"]}
)