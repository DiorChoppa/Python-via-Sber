import setuptools
setuptools.setup(
    name="python-course-package-demo",
    version="0.0.1",
    author="DiorChoppa",
    long_description="test package",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requiers='>=3.8',
)