from setuptools import setup

setup(
    name='pyscramble',
    version='1.1.0',
    py_modules=['obfuscator'],
    entry_points={
        'console_scripts': [
            'pyscramble = obfuscator:main',
        ],
    },
    install_requires=[],
    author='Fahad Majidi',
    description='Advanced Python obfuscator with GUI and CLI',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
