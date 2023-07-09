import sys
import setuptools


long_description = '''
FT-RoboCode is an algorithm designed for hybrid classical-quantum text 
encoding into numerical values which are converted into binaries for 
constructing quantum circuits
'''

if sys.version_info < (3, 6):
    sys.exit('Python>=3.6 is required by Texar.')

setuptools.setup(
    name="ft_robocode",
    version="0.2.4",
    url="https://github.com/aipalbot/ft_robocode",

    description="Toolkit for Femi-Transform encoding algorithm",
    long_description=long_description,
    license='Apache License Version 2.0',

    packages=setuptools.find_packages(),
    platforms='any',

    install_requires=[
        'regex>=2018.01.10',
        'packaging'
    ],
    package_data={
        "ft_robocode": [
            "../bin/utils/multi-bleu.perl",
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)