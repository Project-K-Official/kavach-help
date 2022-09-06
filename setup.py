from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


VERSION = '0.0.1'
DESCRIPTION = 'Demo version of xhelp'
LONG_DESCRIPTION = 'Demo version of xhelp'

# Setting up
setup(
    name="xedu",
    version=VERSION,
    author="VIT Bhopal",
    author_email="kabirdhruw24@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['PyQt5'],
    keywords=['PyQt5'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        ],
        entry_points={
            'console_scripts': ['xhelp=xhelp.main:main']
        },
        include_package_data=True,
)
