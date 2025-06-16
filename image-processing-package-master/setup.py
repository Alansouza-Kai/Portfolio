from setuptools import setup, find_packages

setup(
    name="image-processing",
    version="0.1.0",
    description="Pacote para processamento de imagens - projeto DIO",
    author="Alan de Souza Bezerra",
    author_email="seuemail@example.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "opencv-python"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7'
)
