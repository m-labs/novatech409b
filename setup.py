from setuptools import setup, find_packages

setup(
    name="novatech409b",
    install_requires=["sipyco", "asyncserial"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "aqctl_novatech409b = novatech409b.aqctl_novatech409b:main",
        ],
    },
)
