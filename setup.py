from setuptools import setup

setup(name='uscisstatus',
      version='0.1',
      description='USCIS Status Checker',
      url='http://github.com/meauxt/uscisstatus',
      author='Mohamad Tarbin',
      author_email='mhed.t91@gmail.com',
      license='MIT',
      packages=['uscisstatus'],
       install_requires=[
          'requests',
          'lxml'
      ],
      zip_safe=False)
