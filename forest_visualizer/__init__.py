from setuptools import setup, find_packages

setup(
    name='forest-visualizer',  # Name of your package
    version='0.1',  # Initial version
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=['turtle'],  # Any dependencies your package needs
    description='A Python package for visualizing forest data structures using Turtle Graphics',
    long_description=open('README.md').read(),  # Long description from README.md
    long_description_content_type='text/markdown',  # README file format
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    url='https://github.com/yourusername/forest-visualizer',  # Replace with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)