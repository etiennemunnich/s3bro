from setuptools import setup, find_packages

setup(
    name='s3bro',
    version='1.6',
    package_dir={'s3bro': 's3bro'},
    packages=['s3bro'],
    author='Rubem de Lima Savordelli',
    author_email='rsavordelli@gmail.com',
    url='https://github.com/rsavordelli/s3bro',
    python_requires='>=2.6, <3',
    long_description=open( 'README.rst' ).read(),
    install_requires=[
        'click',
        'boto3',
        'termcolor'
    ],
    entry_points='''
        [console_scripts]
        s3bro=s3bro.cli:cli
    ''',
)
