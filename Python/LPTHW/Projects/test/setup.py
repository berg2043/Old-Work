from setuptools import setup

config = {
'descritpion': 'This is a practice module for the book',
'author': 'Phillip Berg',
'url': 'URL to get it at.',
'download_url': 'Where to download it.',
'author_email': 'phillipb1991@msn.com',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['practice_module'],
'scritps': ['sciptx.py'],
'name': 'practicemodule'
}

setup(**config)