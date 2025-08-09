# Building Machine Learning Models in HPC Environments

[![Check links](https://github.com/UPPMAX/HPC-python/actions/workflows/check_links.yaml/badge.svg?branch=main)](https://github.com/UPPMAX/HPC-python/actions/workflows/check_links.yaml)
[![Check spelling](https://github.com/UPPMAX/HPC-python/actions/workflows/check_spelling.yaml/badge.svg?branch=main)](https://github.com/UPPMAX/HPC-python/actions/workflows/check_spelling.yaml)


## Course Overview

This course provides a **practical, hands-on introduction** to using Python for **Machine Learning** in **High-Performance Computing (HPC)** environments.
By the end of the course, you will know how to:

* Load Python modules and explore available site-installed packages
* Install your own Python packages efficiently
* Set up and manage virtual environments
* Write and submit batch scripts for running Python jobs
* Use Python for **parallel computing** and **GPU-accelerated workloads**
* Apply Python for **Machine Learning** tasks at scale


## Target HPC Systems

The course is a collaboration between:

* **UPPMAX** – Rackham, Snowy, Bianca
* **LUNARC** – Cosmos
* **HPC2N** – Kebnekaise

For site-specific sessions, you’ll be grouped based on your target HPC system, as configurations and workflows differ slightly between centers.


## Building Locally

To build the course material locally:

```bash
# Clone the repository
git clone https://github.com/yourusername/your-repo.git
cd your-repo

# Install requirements
pip install -r requirements.txt

# Build HTML output
sphinx-build -b html ./source ./docs
````

To preview the generated site in your browser:

```bash
python -m http.server --directory ./docs

Then open in your browser:

```
http://localhost:8000/
```

````


##  Contributors & Acknowledgements

This course is jointly developed by **UPPMAX**, **LUNARC**, and **HPC2N** to support researchers and students in leveraging HPC for advanced Python and Machine Learning workflows.

