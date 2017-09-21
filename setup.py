from os import path

from setuptools import setup, find_packages

import chatter

VERSION = chatter.__version__
here = path.abspath(path.dirname(__file__))

# TODO PyPi requires a README.rst file, not a README.md
# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name="Aivery",
    version=VERSION,
    description="A Qt based AI",
    # long_description=long_description,
    author="Nicholas Finch",
    author_email='ngf4@nau.edu',
    license="Public Domain",
    entry_points={
        'console_scripts': [
            'Aivery = Aivery.__main__:main'
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
