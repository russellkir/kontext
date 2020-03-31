from setuptools import setup

setup(
    name="context_app",
    description="Context App",
    version="0.0.1",
    author="Russell Kirmayer",
    author_email="russellkir@gmail.com",
    packages=["context_app"],
    include_package_data=True,
    install_requires=["zoomus==1.1.1"],
    extras_require={
        "test": ["codecov", "pytest==3.8.2", "pytest-cov==2.6.0"],
        "dev": ["black", "pylint==2.2.2", "pep8==1.7.1"],
    },
    entry_points={
        "console_scripts": ["context_app = context_app.__main__:main"]
    },
)
