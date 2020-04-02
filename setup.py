from setuptools import setup, find_packages


def read_reqs(filename):
    with open(filename) as f:
        return [z.strip() for z in f.readlines() if not z.startswith("#")]


setup(
    name="context_app",
    description="Context App",
    version="0.0.1",
    author="Russell Kirmayer",
    author_email="russellkir@gmail.com",
    packages=find_packages(),
    install_requires=read_reqs("requirements.txt"),
    extras_require={
        "prod": read_reqs("requirements.prod.txt"),
        "test": read_reqs("requirements.test.txt"),
    },
    entry_points={"console_scripts": ["context_app = context_app.app:main"]},
)
