from setuptools import setup, find_packages

setup(
    name="PyDCSL",
    version="0.1",
    author="Pari Malam",
    description="A Widevine DCSL Revocation Checker CLI library",
    packages=find_packages(),
    install_requires=[
        "requests",
        "colorama",
        "coloredlogs",
        "argparse",
        "rich"
    ],
    entry_points={
        'console_scripts': [
            'pydcsl=PyDCSL.__main__:main',
        ],
    },
    python_requires='>=3.7',
)