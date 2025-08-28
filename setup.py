from setuptools import setup, find_packages

setup(
    name="mlsa",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask==2.3.3',
        'gunicorn==21.2.0',
        'pandas==2.0.3',
        'numpy==1.24.3',
        'transformers==4.35.2',
        'torch==2.0.1',
        'google-generativeai==0.8.5',
        'langdetect==1.0.9',
        'python-dotenv==1.0.0',
        'requests==2.31.0',
        'Werkzeug==2.3.7',
        'Jinja2==3.1.2',
        'itsdangerous==2.1.2',
        'click==8.1.7',
        'sentencepiece>=0.1.99',
        'protobuf>=3.20.0,<4.0.0',
    ],
    python_requires='>=3.8',
)
