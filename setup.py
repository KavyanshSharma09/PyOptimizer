from setuptools import setup, find_packages

setup(
    name='PyOptimizer',
    version='0.1.0',
    author='Kavyansh',
    author_email='Kavyanshsharma2004@gmail.com',
    description='A project to detect computation-heavy programs and optimize them using GPU acceleration.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'cupy',
        'flask'  
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
       
    ],
    python_requires='>=3.6',
)
