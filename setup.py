from distutils.core import setup

setup(
    name='scholar',
    version='0.1.0',
    author='Martin Maga',
    author_email='xmagam00@stud.fit.vutbr.cz',
    packages=['scholar'],
    url='https://github.com/KNOT-GIT/mGoogleScholar',
    license='LICENSE.txt',
    description='Python API module for scholar.gooogle.cz',
    long_description=open('README.md').read(),
    install_requires=[
        "beautifulsoup4 >= 4.0.1",
    ],
)
