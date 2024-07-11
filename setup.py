from setuptools import setup, find_packages

setup(
    name='flask_project_generator',
    version='0.1',
    packages=find_packages(),
    entry_points={
      'console_scripts': [
          'generate-flask-project=flask_project_generator.generator:main',
      ],
    },
    install_requires=[
      'Flask',
      'colorama',
    ],
    author='Romain Doyen',
    author_email='',
    description='A simple Flask project generator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RomainDoyen/flask_project_generator',
    classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
