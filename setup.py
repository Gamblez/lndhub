from os import path
from setuptools import setup


with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()


setup(
    name='lndhub',
    version='0.0.2',
    url='https://github.com/eillarra/lndhub',
    author='eillarra',
    author_email='eneko@illarra.com',
    license='MIT',
    description='',
    long_description=long_description,
    keywords='bitcoin lightning-network lndhub lnurl',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ],
    packages=['lndhub'],
    install_requires=[
        'requests',
    ],
    zip_safe=False
)
