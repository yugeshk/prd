# setup.py
from setuptools import setup, find_packages

setup(
    name='prd_tools',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pypandoc'
    ],
    entry_points={
        'console_scripts': [
            'swent_prd=prd_tools.main:main',
        ],
    },
)
