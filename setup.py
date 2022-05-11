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
        'loguru',
        'ujson',
        'torch',
        'numpy==1.16.6',
        'scikit-learn[alldeps]==0.22.1',
        'typing==3.6.6',
        'pandas==1.0.0',
        'mxnet==1.7.0.post2',
        'wheel'
    ]
)
