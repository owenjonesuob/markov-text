try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'MarkovText',
    'author': 'Owen Jones',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'olj23@bath.ac.uk',
    'version': '0.1.0',
    'install_requires': ['nose'],
    'packages': ['MarkovText'],
    'scripts': [],
    'name': 'MarkovText' 
 }
 
 setup(**config)