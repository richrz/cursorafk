from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="cursorafk",
    version="1.0.0",
    author="AI Community",
    author_email="",
    description="Keep your AI assistant awake and responsive with automatic periodic nudges",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cursorafk",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Communications :: Chat",
        "Topic :: Desktop Environment",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "cursorafk=cursorafk:main",
        ],
    },
    keywords="ai assistant automation nudge keep-alive chat claude chatgpt cursor afk",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/cursorafk/issues",
        "Source": "https://github.com/yourusername/cursorafk",
    },
)