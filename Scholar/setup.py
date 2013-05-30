from distutils.core import setup

setup(
    name='Scholar',
    version='0.1.0',
    author='Martin Maga',
    author_email='xmagam00@stud.fit.vutbr.cz',
    packages=['scholar'],
    scripts=['bin/API_GoogleScholar_PEP8.py'],
    url='http://pypi.python.org/pypi/Scholar/',
    license='LICENSE.txt',
    description='Useful scripts',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.1.1",
        "caldav == 0.1.4",
    ],
)
