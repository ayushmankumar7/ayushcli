from setuptools import setup
setup(
    name = 'pycli',
    version = '0.1.0',
    packages = ['ayushcli'],
    entry_points = {
        'console_scripts': [
            'ayushcli = ayushcli.__main__:main'
        ]
    })