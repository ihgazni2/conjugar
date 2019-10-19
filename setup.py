from setuptools import setup, find_packages
setup(
      name="conjugar",
      version = "0.66",
      description="handle,.in progressing..,APIs",
      author="dapeli",
      url="https://github.com/ihgazni2/conjugar",
      author_email='terryinzaghi@163.com', 
      license="MIT",
      long_description = "refer to .md files in https://github.com/ihgazni2/conjugar",
      entry_points = {
         'console_scripts': [
             'esconju=conjugar.bin.es_word_conjugar:main',
             'esverb=conjugar.bin.es_verb_list:main'
          ]
      },
      package_data = {
          'resources':["conjugar/data/*"]  #necessary for resources   ,must be used with MANIFEST.in
      },
      include_package_data=True, #necessary for resources   ,must be used with MANIFEST.in
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

