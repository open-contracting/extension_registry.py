from setuptools import find_packages, setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='ocdsextensionregistry',
    version='0.0.19',
    author='Open Contracting Partnership',
    author_email='data@open-contracting.org',
    url='https://github.com/open-contracting/extension_registry.py',
    description="Eases access to information from the extension registry of the Open Contracting Data Standard",
    license='BSD',
    packages=find_packages(exclude=['tests', 'tests.*']),
    long_description=long_description,
    install_requires=[
        'json-merge-patch',
        'requests',
        'requests-cache',
    ],
    extras_require={
        'test': [
            'pytest',
        ],
        'docs': [
            'Sphinx',
            'sphinx-autobuild',
            'sphinx_rtd_theme',
        ],
        'cli': [
            'Babel',
            'docutils',
            'ocds-babel[markdown]>=0.2.0',
            # See https://ocds-babel.readthedocs.io/en/latest/api/translate.html
            # 'recommonmark',
            'Sphinx',
        ]
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'ocdsextensionregistry = ocdsextensionregistry.cli.__main__:main',
        ],
    },
)
