from setuptools import setup

setup(
    name='AutoClean',
    version='0.0.1',
    description='pip install test',
    url='https://github.com/LucasChun/SSU_AutoData.git',
    author='chunhyeonu',
    author_email='hyeonu.chun@gmail.com',
    license='hyeonu',
    packages=['AutoClean'],
    zip_safe=False,
    install_requires=[
        'ujson',
        'datawig==0.2.0',
        'numpy==1.21.6',
        'pandas==1.3.0',
        'py-AutoClean',
        'torch'
    ]
)
