from setuptools import setup, find_packages

setup(
    name='PyCitrine',
    version='1.0.0',
    description='A package for handling Citrine data format and conversions',
    author='CintagramABP',
    author_email='support@bcpulse.net',
    url='https://github.com/cintagram/PyCitrine',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.9',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)