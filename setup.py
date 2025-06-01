from setuptools import setup, find_packages

setup(
    name='ghostwhisper',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'ghostwhisper=cli.ghostwhisper:main',
        ],
    },
    python_requires='>=3.11',
)
