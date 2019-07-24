
from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='dns-dnspod',
    version='1.0.0',
    keywords='dns, dnspod',
    description='manage dnspod domain and records',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='zhanghe',
    author_email='x_hezhang@126.com',
    url='https://github.com/x-hezhang/pydnspod',
    license='GPLv3',
    packages=find_packages()
)
