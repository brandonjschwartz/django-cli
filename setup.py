from distutils.core import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

setup(name='django-cli',
      packages=['django-cli'],
      version='0.0.1',
      description='Command line interface for sensible Django projects.',
      long_description=README + '\n\n' + CHANGES,
      author='Brandon J. Schwartz',
      author_email='brandon@boomajoom.com',
      url='https://github.com/brandonjschwartz/django-cli',
      download_url='https://github.com/brandonjschwartz/django-cli/tarball/0.0.1',
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python 3.5',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Utilities'
      ],
      )
