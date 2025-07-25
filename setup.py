from setuptools import setup, find_packages

setup(
    name="PyDCSL",
    version="0.2",
    author="Pari Malam",
    description="A compact Python tool to check if a Widevine device certificate (DCSL) is revoked or valid.",
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