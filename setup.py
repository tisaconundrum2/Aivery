from os import path

from setuptools import setup, find_packages

import chatter

VERSION = chatter.__version__
here = path.abspath(path.dirname(__file__))

setup(
    name="Aivery",
    version=VERSION,
    description="A Qt based AI",
    # long_description=long_description,
    author="tisaconundrum",
    author_email='ngf4@nau.edu',
    license="Public Domain",
    entry_points={
        'console_scripts': [
            'Aivery = chatter.__main__:main'
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: General",
        "Topic :: Chatbot",
        "License :: Public Domain",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords="chatbot AI",
    packages=find_packages(include=['brain']),
    include_package_data=True

)
