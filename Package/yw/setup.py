from setuptools import setup

setup(
    name="td3fd",
    version="0.0",
    description="TD3fD through Shaping using Generative Models",
    author="Yuchen Wu",
    author_email="cheney.wu@mail.utoronto.ca",
    license="MIT",
    packages=["yw"],
    install_requires=["matplotlib", "tensorflow==1.15.2", "tensorflow_probability==0.7.0", "pandas"],
    zip_safe=False,
)
