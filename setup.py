from setuptools import setup, find_packages


setup(
    name="memoris-client",
    version='0.1.0',
    url='http://github.com/relekang/memoris-client',
    author='Rolf Erik Lekang',
    author_email='me@rolflekang.com',
    description='',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['memoris = memoris.client:main']
    },
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ]
)
