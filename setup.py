import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__),
                             fname)).read()


setup(
    name='MoneyExchange',
    version='0.1',
    description='Library for moneylib operations',
    author='Kate Zabelava',
    author_email='katsiaryna_zabelava@epam.com',
    url='https://github.com/Tobichimaru/advanced_python',
    packages=['moneylib'],
    package_dir={'moneylib': 'src/moneylib'},
    long_description=read('README.md'),
)
