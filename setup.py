from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    author='Natalia Chepurna',
    license='MIT',
    packages=find_namespace_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],

    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean=clean_folder.clean:start']}
    )
