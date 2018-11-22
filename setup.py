from setuptools import setup, find_packages
setup(
      name="conjugar",
      version = "0.2",
      description="handle....,APIs",
      author="dapeli",
      url="https://github.com/ihgazni2/conjugar",
      author_email='terryinzaghi@163.com', 
      license="MIT",
      long_description = "refer to .md files in https://github.com/ihgazni2/conjugar",
      classifiers=[
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Programming Language :: Python',
          ],
      packages= find_packages(),
      py_modules=['conjugar'], 
      )


# python3 setup.py bdist --formats=tar
# python3 setup.py sdist

