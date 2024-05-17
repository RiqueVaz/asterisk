from setuptools import setup

setup(name='asterisk',
    version='0.0.8',
    description='Tools for computing asset risk with respect to goals.',
    url='https://git.mps.com.br/ecm/python-asterisk',
    author='Henrique V.',
    author_email='henrique.vaz@mps.com.br',
    license='MIT',
    packages=['asterisk'],
    install_requires=[
        'requests'
    ],
    extras_require = {
    },
    zip_safe=False)