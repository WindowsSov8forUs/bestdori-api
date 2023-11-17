from setuptools import find_packages, setup

setup(
    name='bestdori_api',
    version='0.1.2',
    author='WindowsSov8',
    author_email='qwertyuiop2333@hotmail.com',
    description='Bestdori 的各种 API 调用整合，另外附带部分功能',
    url='https://github.com/WindowsSov8forUs/bestdori_api',
    include_package_data=False,
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.8',
)