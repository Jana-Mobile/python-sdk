from distutils.core import setup

setup(
    name='Jana_API',
    version='0.1.0',
    author='Jana Mobile',
    author_email='craig@jana.com',
    packages=['jana_api'],
    license='LICENSE.txt',
    description='SDK for the Jana API',
    install_requires=['requests'],
    long_description=open('README.txt').read(),
)