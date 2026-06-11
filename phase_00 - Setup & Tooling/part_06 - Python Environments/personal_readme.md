# What is a virtual environment?

Imagine working on two projects that require different version of `numpy` or `pandas`. Project A requires `Pandas 1.0` while Project B requires `Pandas 2.0`. When we installed `Pandas 1.0` for Project A, we can't run Project B properly because the library is in the wrong version. And if we upgrade the library, we can't run Project A. This is known as **dependency hell**. Virtual environment solves this problem by creating a *confinement* for each project.

By creating a `.venv` folder inside a project's directory, we can install whichever version of libraries for that project we want without them affecting any other project and the global system of our computer. This can be done by running 

```bash
cd project_path
uv venv
source .venv/bin/activate
```

where the last line is us telling the terminal: "For the rest of this session, ignore the global Python installation, and only use the Python and the installed packages within this `.venv` folder."

# Solving the "It runs on my computer!" problem. (pyproject.toml)

Sometimes, when we run our code, it works without any problem. But when we ship it out for others to test, errors came out. This could be because of the difference in systems of each computer. Sometimes people would create a `requirements.txt` so others can see what conditions must be met for the codes to run smoothly, or perhaps `setup.py`, etc. It was messy and hard to implement. The modern way is to use `pyproject.toml`. It is a single, standardized configuration file for all Python projects. The `.toml` stands for **Tom's Obvious Minimal Language**. Within the file, it may look like this:

```toml
[project]
name = "ai-project"
version = "0.1.0"
description = "A short project in understanding the mechanism of AI."
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "openai>=1.0.0",
    "python-dotenv>=1.0.0",
]

[tool.uv]
# This section tells your 'uv' package manager specific settings for your project.
```

This makes our project reproducible. When we work on a team or send a programming assignment to our professor, we don't send the `.venv` folder as it is a huge file and is tied to our specific operating system. Instead, we simply send our code and our `pyproject.toml`. The professor can then run 

```bash
uv pip install -r pyproject.toml
```

(or `uv sync`) and `uv` will automatically read the file, create a matching virtual environment, and download the exact correct versions of `openai` and `python-dotenv`. 

And instead of having different configuration files for a project, tools like a code formatter (Ruff or Black) and testing frame work (pytest) can store all their settings inside this one single file under sections like `[tool.ruff]` or `[tool.pytest]`. 

So, if you want to add a new library into your project, you should register the new library into `pyproject.toml` and let `uv` handle the work by running `uv pip install -r pyproject.toml`. Or if you don't want to manually open the `pyproject.toml` and type in the library, we can just run 

```bash
uv add matplotlib
```

This command will automatically download `matplotlib` into our `.venv` and update our `pyproject.toml` in one go!

# Snapshot in time (uv.lock)

Inside our `pyproject.toml` we might have 

```toml
dependencies = ["openai>1.0.0",]
```

The `>=1.0.0` part just means "Give me version 1.0.0 or any newer version that comes out." So, if you try to run `uv sync` months from when I send the project to you, you might be installing `openai 2.0.0` even though my project was using `openai 1.12.0` or `openai 1.0.0`. The code suddenly crashes even though `uv` followed the dependencies registered in `pyproject.toml`. 

`uv.lock` solves this problem! The moment you run `uv sync` or `uv add`, `uv` looks at the loose rules in `pyproject.toml`, figures out the exact versions of everything it downloaded today, and locks them down in a file called `uv.lock`. 

If you were to open `uv.lock`, you will see the exact version of `openai` and other libraries and packages. It even includes the **cryptographic hash** (a digital fingerprint) of the downloaded file to guarantee nobody has tampared with the code.

# My case

## My method 

Since I already have a `.venv` folder in my project, I can create a blank `pyproject.toml` in my project's folder. However, the `.venv` in my case covered the entirety of `my_ai` directory. I want a working virtual environment for each phase in this project. Before we can do that, we have to see the versions of the installed packages first.

```bash
uv pip freeze
```

This bash script prints out the current versions of the packages. We can put all the outputs into a single `req.txt` file. 

```bash
uv pip freeze > req.txt
cd phase_00/
```

Then we can create a blank `pyproject.toml` inside this `phase_00` directory now. (Note that `uv add` works by looking for a virtual environment to sync with. If it doesn't find one in the current folder, it might look upward or fail. To ensure the safety of our process, we should create and activate the new virtual environment BEFORE running `uv add`.)

```bash
# Initialize your blank blueprint here
uv init --bare
ls # We will see a file named pyproject.toml

# Create your brand new, phase-specific virtual environment FIRST
uv venv

# Activate it immediately so 'uv add' knows exactly where to put the packages
source .venv/bin/activate

# Now register the dependencies into pyproject.toml AND install them into the active .venv
uv add -r ../req.txt

# Clean up the temporary files and the old parent environment
rm ../req.txt
rm -rf ../.venv
```

# NOTES

After running the verification as per Rohit's course,

```bash
bash ../../ai-engineering-from-scratch/phases/00-setup-and-tooling/06-python-environments/code/env_setup.sh
```

the result told us to use the virtual environment

```bash
source ~/GitHub/creation_of_ai/ai-engineering-from-scratch/.venv/bin/activate
```

instead of our virtual environment in `creation_of_ai/my_ai/phase_00`. However, to ensure I fully understand everything, I will be using my own virtual environment!
