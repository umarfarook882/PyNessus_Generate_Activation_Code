from distutils.core import setup

install_dependencies = (
    'requests == 2.8.14',
    'bs4 == 0.0.1'
)


setup(
    name='Tempmail',
    version='0.1',
    packages=[''],
    package_dir={'': 'Tempmail'},
    url='',
    license='MIT License',
    author='Umar Farook',
    author_email='Twitter: @umarfarook882',
    description='Generate Temporary Email Address  to register and get Nessus Activation Code'
)