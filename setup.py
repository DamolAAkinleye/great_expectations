try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

#Parse requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''

exec(open('great_expectations/version.py').read())

config = {
    'description': 'Always know what to expect from your data.',
    'author': 'The Great Expectations Team',
    'url': 'https://github.com/great-expectations/great_expectations',
    'author_email': 'team@greatexpectations.io',
    'version': __version__,
    'install_requires': required,
    'packages': [
        'great_expectations',
        'great_expectations.dataset',
        'great_expectations.data_context'
    ],
    'scripts': [
        'bin/great_expectations',
    ],
    'name': 'great_expectations',
    'long_description': long_description,
    'license': 'Apache-2.0',
    'keywords': 'data science testing pipeline',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Other Audience',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
}

setup(**config)
