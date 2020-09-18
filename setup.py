from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='ashahba-hello-world-001',
      version='0.0.1',
      description='The simplest Hello World PyPi package',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        'Topic :: Text Processing :: Linguistic',
      ],
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
