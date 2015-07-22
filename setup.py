import setuptools

classifiers = ['Development Status :: 3 - Alpha',
               'Intended Audience :: System Administrators',
               'License :: OSI Approved :: BSD License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 2',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.2',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: Implementation :: CPython',
               'Programming Language :: Python :: Implementation :: PyPy',
               'Topic :: System :: Clustering',
               'Topic :: System :: Installation/Setup',
               'Topic :: System :: Networking',
               'Topic :: System :: Systems Administration']

setuptools.setup(name='formulary',
                 version='0.3.4',
                 description='Easy management of AWS Cloud Formation stacks',
                 long_description=open('README.rst').read(),
                 author='Gavin M. Roy',
                 author_email='gavinr@aweber.com',
                 url='http://formulary.readthedocs.org',
                 packages=['formulary',
                           'formulary.builders',
                           'formulary.resources'],
                 package_data={'': ['LICENSE',
                                    'README.rst',
                                    'requirements.txt']},
                 include_package_data=True,
                 install_requires=open('requirements.txt', 'r').read(),
                 license='BSD',
                 classifiers=classifiers,
                 entry_points={'console_scripts':
                                   ['formulary=formulary.cli:run']},
                 zip_safe=True)
