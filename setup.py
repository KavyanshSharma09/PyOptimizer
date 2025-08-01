from setuptools import setup, find_packages

setup(
    name='code-optimizer',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project to detect computation-heavy programs and optimize them using GPU acceleration.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'cupy',
        'flask'  # or any other web framework you plan to use for the API
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)