import os
from setuptools import setup, find_namespace_packages

here = os.path.abspath(os.path.dirname(__file__))
meta_info = {}
with open(os.path.join(here, 'workshopse', 'story_generator', '_meta.py'), 'r') as f:
    exec(f.read(), meta_info)

setup(
    name=meta_info['__title__'],
    version=meta_info['__version__'],
    description=meta_info['__description__'],
    author=meta_info['__author__'],
    author_email=meta_info['__author_email__'],
    url=meta_info['__url__'],
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'fastapi',
    ],
    python_requires='>=3.5',
    packages=find_namespace_packages(include=['workshopse.*'])  # Native namespace packaging, PEP420
)
