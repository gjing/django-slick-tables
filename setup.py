import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='django-slick-tables',
    version='0.1',
    packages=['slick_tables'],
    description='A line of description',
    long_description=README,
    author='yourname',
    author_email='yourname@example.com',
    url='https://github.com/gjing/django-slick-tables',
    license='MIT',
    install_requires=[
        'Django>=1.6,<1.7',
    ]
)
