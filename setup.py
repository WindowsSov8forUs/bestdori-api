from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='bestdori-api',
    version='1.0.1',
    author='WindowsSov8',
    author_email='qwertyuiop2333@hotmail.com',
    description='Bestdori 的各种 API 调用整合，另外附带部分功能',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/WindowsSov8forUs/bestdori-api',
    include_package_data=False,
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.8',
)