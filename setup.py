from distutils.core import setup

setup(
    name='DataDomainFairness',
    version='0.1.0',
    author='N. Quadrianto, V. Sharmanska, O. Thomas',
    packages=['ddf'],
    description='Model for learning fair representations in the data domain',
    python_requires=">=3.6",
    install_requires=[
        "numpy >= 1.14.2",
        "pandas >= 0.22.0",
        "scikit_learn >= 0.20.1",
        "tensorflow ~= 1.15"
    ],
)
