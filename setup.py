from setuptools import setup

from ps2cpcdata.version import __version__

setup(
    name="ps2cpcdata",
    version=__version__,
    description="This is the first stable release of the package.",
    author="ecss11",
    maintainer="ecss11",
    url="https://github.com/PlanetSide2-CPC/PS2-DatabaseSync",
    packages=["ps2cpcdata"],
    install_requires=[
        "mysql-connector-python==8.0.28",
        "websockets==10.1"
    ]
)