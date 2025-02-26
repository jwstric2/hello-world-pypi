from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='jonatstr-hello-world',
      version='0.0.1',
      description='The simplest Hello World PyPi package with a big file in it',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        'Topic :: Text Processing :: Linguistic',
      ],
      data_files=[('conf', ['conf/1MB.json', 'conf/5MB.json', 'conf/large-file.json'])],
      keywords='simplest hello world pypi package',
      url='http://github.com/ashahba/hello-world-pypi',
      author='Abolfazl Shahbazi',
      author_email='ashahba@example.com',
      license='MIT',
      packages=['hello_world'],
      entry_points={
          'console_scripts': ['hello-world=hello_world.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
