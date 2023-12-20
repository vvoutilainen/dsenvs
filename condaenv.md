# `conda` data science environments

**By Ville Voutilainen, updated 2023-12-20.**

**MIT license, usage at one's own risk!**

## Introduction

This article provides my "cookbook recipes" on how to build tailored `conda` environments for everyday data science work in Python and R. The article covers the following topics:

 - How to install `conda` environments containing fresh Python and R installations;
 - How to install packages into the environments;
 - How to run Python and R instances, separately and together, in Jupyter Lab, VSCode, and RStudio.

The instructions are written for a **Windows 10 machine**. They might be applicable to other operating systems as well, but no guarantees are made.

### What are Anaconda, `conda`, and `conda` environments?

[Anaconda](https://www.anaconda.com/) is a popular data science platform for several programming languages, most notably Python and R. Anaconda is also a company pursuing many ends, but here we focus on the software it provides. Anaconda lets you run Python and R in virtual **environments**, which constitute logically separable playing fields for data science experiments. The environments can be loaded up with different versions of Python and R programs, as well as bundles of **packages** that power your work. Both environments and packages are managed by `conda`, the package manager of Anaconda.

### Why use tailored `conda` environments for data science work?

Python and R are great tools for data science. The web is full of discussion about which one is better, but in my opinion, these conversations often miss the mark. Each language has its own merits, and there are huge benefits to being able to flexibly change between the two.

For example, Python is great for machine learning as well as for general infrastructure around the data science workflow. On the other hand, R offers a much broader set of statistical tools. The goal of this article is to build an environment where one can employ the best parts of both worlds on the fly!

A clear advantage of `conda` comes with its dependency management capabilities. Maintaining Python or R packages and versions can be a hazzle, let alone doing the same for both. `conda` environments are, according to my knowledge, the best way to manage package and program versions over time and across each other. It offers reproducible data science environments that one can spin up whenever needed. Being diligent about the software versions will make life much easier and may save you from the cardinal sin of producing irreproducible science and code.

With custom `conda` environments one can

 - Run Python in VSCode or Jupyter Lab;
 - Run R in RStudio or Jupyter Lab;
 - Call R code from a Python instance with *rpy2*;
 - Use typical Python data science packages such as *pandas* and *scikit learn*;
 - Use typical R data science packages such as *tidyverse*.

### When **not** to use custom `conda` environments?

The custom environments described here are neither perfect nor suited for every occasion. They have evolved based on the personal preferences of someone who does most of the work in Python but every now and then needs R for running statistical analyses.

Custom `conda` environments proposed in this article may not be for you if:

 - **You solely use R**. R environment dependency management as itself might be easier with other tools, such as *packrat*. The power of `conda` environments comes from Python package management and combining that with R or even Julia. Also, `conda` often does not offer the latest R packages.
 - **You are afraid of getting your hands dirty**. Installing and managing `conda` environments can be time-consuming, although in the long run. I believe the cost is well compensated by reproducibility. If you do not like the extra work that comes with being able to fully customize the tools for your needs, then custom `conda` environments might not be your cup of tea.

## Building tailored `conda` environments

### Download and install Anaconda

First, we need to install Anaconda. One could also download a stripped version of Anaconda, called Miniconda, but in this article we focus on Anaconda. Anaconda distributions can be installed from [here](https://repo.anaconda.com/archive/). Miniconda distributions can be installed from [here](https://repo.anaconda.com/miniconda/).

**\<optional\>**

If there have been previous Anaconda installations on your machine, check that no previous specification files are lurking in the directories. Typical suspects outside the *~/Anaconda/* folder are:

 - Anaconda-related
    - C:\Users\<my_user_name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3
 - Jupyter related
   - C:\Users\<my_user_name>\.jupyter
   - C:\Users\<my_user_name>\.ipynb_checkpoints
   - C:\Users\<my_user_name>\.ipython
   - C:\ProgramData\jupyter
   - C:\Users\<my_user_name>\AppData\Roaming\jupyter
 - `conda` related
   - C:\Users\<my_user_name>\.conda
 - Python packages-related
   - C:\Users\<my_user_name>\.matplotlib
   - C:\Users\<my_user_name>\.keras
   - etc.
 - Windows environment variables: remove all Anaconda related paths.

**\</optional\>**

In this article, we use Anaconda version *2020.02-Windows-x86_64*. Download and run the installer. Install the software at the preferred path. When installing, uncheck *"Register Anaconda3 as my default Python"* (we don't want to use Python in the `base` environment as our default). Also check the *"add to path"* checkbox (although it is not recommended by the wizard). The following window paths added are:

  - *~/Anaconda3*
  - *~/Anaconda3/Library/mingw-w64/bin*
  - *~/Anaconda3/Library/usr/bin*
  - *~/Anaconda3/Library/bin*
  - *~/Anaconda3/Scripts*

### Installing environments

Now open the Anaconda prompt. This is where most of the commands will be given.

We start by telling `conda` to add one extra channel to the list of [default channels](https://docs.anaconda.com/free/anaconda/reference/default-repositories/) from where to look for packages: *conda-forge*. Packages tend to be faster available in *conda-forge* than in the default channels.

The below commands do two things: 1) Set channel priority to 'flexible' and 2) appends *conda-forge* as a lower priority channel compared to default channels. See [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html) for more. You can check your *.condarc* file to make sure that *conda-forge* comes as the last channel.

Notice, however, that *conda-forge* packages are not per se curated by Anaconda. If you prefer to minimize the use of *conda-forge*, skip this part! Below, we will give an example of an environment where almost all of the packages come from Anaconda default channels.

```
conda config --set channel_priority flexible
conda config --append channels conda-forge
```

Next, install [mamba](https://github.com/TheSnakePit/mamba) in the `base` conda environment. `mamba` is a faster, drop-in replacement for `conda`. Later, we will replace `conda` commands with `mamba` for increased speed in solving package dependencies.

```
conda install mamba
```

Now we can install a custom `conda` environment. Below are some options. To build either one of the environments, run commands as instructed.

#### dev_2018: Python 3.6.10 and R 3.6.0

```
mamba create --name dev2018 anaconda python=3.6 numpy=1.16.4 numpy-base=1.16.4 tzlocal=2.0.0 pandas=0.25.0 seaborn=0.11.0 rpy2==2.9.4 r=3.6.0 r-base=3.6.0 r-essentials=3.6.0 r-tidyverse=1.2.1 rtools=3.4.0 r-rjsdmx=2.1_0 r-seasonal=1.7.0 rstudio=1.1.456
```

#### dev_2021: Python 3.8.5 and R 3.6.3

```
mamba create --name dev2021 anaconda=2020.11 rpy2=3.4.2 r-base=3.6.3 r-essentials=3.6 rtools=3.4.0 r-rjsdmx=2.1_0 r-seasonal=1.8.1
```
Notes about `dev2021`:

 - There is a problem with the `rstudio` installation in this environment. RStudio version 1.1.456, which is the newest available in `conda`, seems too old for the environment set-up. This causes an error and prevents the installation of RStudio. We might be able to use a standalone installation of RStudio and connect it to the R in `dev2021`, but this might lead to problems when switching between R installations. For this reason, before the `r-rstudio` package is updated, we cannot install RStudio into `dev2021` or later environments.

#### dev_2021b: Python 3.9.7 and R 3.6.3

```
mamba create --name dev2021b anaconda=2021.11 rpy2=3.4.2 r-base=3.6.3 r-essentials=3.6 rtools=3.4.0 r-rjsdmx=2.1_0 r-seasonal=1.8.1 jupyterlab=3.* ipykernel=6.*
```

Notes about `dev_2021b`:

 - Compared to `dev_2021`, has newer versions of `jupyterlab` and `ipykernel` supporting notebook debugging.
 - The same caveat as in `dev_2021` applies to `rstudio`.

#### dev_2023a: Python 3.10.9 and R 4.1.3

```
mamba create --name dev2023a anaconda=2022.10 rpy2 r-base=4.1 r-essentials rtools
```

Notes about `dev_2023a`:

 - Upgrades R to version 4.
 - Compared to previous environments, this drops some specific R packages as they may be installed later on.

#### dev2023a_minforge: Python 3.10.9 and R 3.6.0

Environment that uses *conda-forge* as little as possible. Make sure to remove *conda-forge* from the channel list!

```
mamba create --name dev2023a_minforge anaconda=2022.10 tzlocal=2.1 r-base=3.6.* r-essentials=3.6.* r-tidyverse=1.2.1 rtools
conda activate dev2023a_minforge
mamba install r-tidyselect=1.1.1 -c conda-forge --no-deps
mamba install rpy2=3.5.1 -c conda-forge --no-deps
```

Notes about `dev2023a_minforge`:

 - Similar to dev2023a, but minimizes the need of packages from *conda-forge* channel.
 - Anaconda default channels do not have a newer version of R than 3.6 (updated 2023-12-20).

### Setting up Jupyter kernels for the environments

*Jupyter notebooks* are my preferred way to use Python and R. In order to use the freshly installed Python and R versions with Jupyter notebooks, we need to install *kernels*. We specify the kernels with unique names so that we can have IPython/IR kernels for each `conda` environment separately (see more [here](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)).

Run the following commands in the `conda` prompt to install Python and R kernels for the environment. Here we use `dev2021` as an example. Change the names depending on which environment was installed.

```
conda activate dev2021
python -m ipykernel install --user --name dev2021_py --display-name "dev2021_py"
R
IRkernel::installspec(name='dev2021_r', displayname='dev2021_r')
quit()
```

This should add two folders under the Jupyter kernels directory (typically under *C:\Users\<myusername>\AppData\Roaming\jupyter\kernels*). Check that the folders are created.

### Setting paths

In order to use `rpy2` to call R from Python, the Python instance has to know where the R executable is located. Otherwise, `rpy2` calls will die or crash. See [this](https://stackoverflow.com/a/53639407) for more. To set the `R_HOME` path:

  - An ad-hoc solution that works for all Python instances (terminal, Jupyter):
    ```
    import os
    os.environ['R_HOME'] = '~/Anaconda3/envs/<env_name>/lib/R'
    ```
 - A more permanent solution for Jupyter: Find the *kernel.json* for the Python Jupyter kernel (e.g., *~/jupyter/dev2021_py/kernel.json*). Add parameter `"env": {"R_HOME":"/home/your/anaconda3/envs/my-env-name/lib/R"}` into the file. See [this](https://stackoverflow.com/a/60869259/7037299) and [this](https://stackoverflow.com/questions/39347782/getting-segmentation-fault-core-dumped-error-while-importing-robjects-from-rpy2/53639407#53639407) for more.


### Testing the installations

Run test files in folder *testfiles* to see if everything works:

 - *python.py* (e.g., in VSCode)
 - *python.ipynb* (in Jupyter or VSCode)
 - *R.R* (in command line or in RStudio installed with the environment)
 - *R.ipynb* (in Jupyter)

See the section *Using `conda` environments* below for more on how to run the examples.

## Using `conda` environments

In this section we cover tips on how to use the new `conda` environment. 

### Some general tips

 - Make sure Python executable points to one in the new `conda` environment (check with `import sys; print(sys.executable)`). The path should be something like *~/Anaconda3/envs/<env_name>/python.exe*. Also, make sure that Python import paths include the packages directory of the new environment (check with `print(sys.path)`). The path should be something like *~/Anaconda3/envs/<env_name>/*.
 - Make sure R executable points to one in the new `conda` environment (check with `print(file.path(R.home("bin"))`). The path should be something like *~/Anaconda3/envs/<env_name>/lib/R/bin/x64*. Also, make sure R import paths contain **only** the packages directory of the new environment (`print(.libPaths())`). The path should be something like *~/Anaconda3/envs/<env_name>/lib/R/library*. If there are other paths, reset the paths using `.libPaths("~/Anaconda3/envs/<env_name>/lib/R/library")`.
   - If `.libPaths()` contains other library paths (e.g., from different standalone R versions), wrong packages might be imported on notebook load-out, and these packages cannot be reloaded. This can cause compatibility problems with other packages in the notebook instance. The solution I can recommend is to be pedantic about R package management. In particular, do not install any R packages directly into Windows *HOME* path (usually *User/Documents*) where other R versions might pick them up from. Always use separate package folders (outside of *HOME*) for each R version! See more about R load-out in text [[standalone_r.md]].
- If the Jupyter kernel dies or restarts when running `rpy2` commands (for example, with the error *"Fatal error: unable to initialize JIT!"*), the reason might be that the `R HOME` path is not set and `rpy2` does not find the R installation that came with the environment. In this case, return to the section "Setting paths" above and make sure the path to `R HOME` is set.
- In theory, Python and R kernels of the new `conda` environment should be accessible in Jupyter when run from the *base* `conda` environment, see [here](https://ipython.readthedocs.io/en/stable/install/kernel_install.html) under section *"you can make your IPython kernel in one env available to Jupyter in a different env"*. However, I have run to all kinds of problems with the R kernel, e.g. [this](https://github.com/IRkernel/IRkernel/issues/309), [this](https://github.com/jupyter/jupyter/issues/353), and R installation not being found when called from a Python instance with *rpy2*. Thus, I have found it easier to use Jupyter Lab from within each `conda` environment. This is why we install Jupyter in every environment and not just in `base` as usually suggested (see, e.g., the discussion [here](https://stackoverflow.com/a/39623487/7037299)). Make sure to launch Jupyter from the custom environment (e.g., `conda activate dev2021`, and only then `jupyter lab`).

### Using Python and R in Jupyter Lab

To launch a Python/R instance in Jupyter notebooks, first select the installed environment and then launch Jupyter Lab:

```
conda activate dev2021
jupyter lab
```

This opens up Jupyter Lab in the browser. If Jupyter kernels for the environment were correctly set up, they would be visible on the launcher page. Test running *python.ipynb* (here with *dev2021* environment) in `dev2021_py` kernel and *R.ipynb* using `dev2021_py` kernel. Make sure you choose the correct kernel for each notebook (top-right corner).

### Using R in RStudio

If package *r-rstudio* was installed with the environment, launch RStudio from the Anaconda prompt from the desired command folder path:
```
cd <desired command folder path>
conda activate dev2018
rstudio
```

Then use R Studio as per usual.

Troubleshoot:
 - If opened R files suddenly appear empty in RStudio, one needs to reopen the file with UTF-8 encoding. See [this](https://stackoverflow.com/a/45034170/7037299).
 - If you have multiple environments with an R installation (*env1* and *env2*), RStudio in *env2* might initially point to R.exe in *env1*. To correct this, simply change the R version in RStudio under *Tools* -> *Global options* -> *General* -> *R version*.

### Using Python and R in VSCode

VSCode is one of the best overall IDEs for data science. Thanks to its many plugins, we can run both Python and R from our custom `conda` in VSCode.

**Python files**

To begin with, install [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) plugin for VSCode. Next, make sure the desired custom environment (e.g., `dev2021`) Python interpreter is selected in VSCode (bottom-left). Then, from the *.py* file, right-click and choose *Run Python file in terminal*. This creates a new Python terminal and executes the file. One can also *Run selection/line in Python terminal* to run a specific section. To exit, type `quit()` to close the Python instance. One can also run a file or a section in the interactive terminal. I would recommend using notebooks for interactive computing, however.

**Python notebooks**

Make sure that VSCode launches Jupyter instance from the desired custom `conda` environment (by default, VSCode launches Jupyter from `base`). There are two ways to do this:
  - Make sure we can run `conda` commands from a Powershell terminal by running in Anaconda terminal `conda init powershell` (see [here](https://stackoverflow.com/questions/47800794/how-to-activate-different-anaconda-environment-from-powershell/54811138)). Then, open a Powershell terminal in VSCode, and run `conda activate dev2021`. Next, make sure that 1) the selected VSCode Python interpreter (bottom-left) and 2) the Jupyter interpreter (top-right) both correspond to the Python version installed in the environment. Now launch a Python notebook, and things should work. See more [here](https://medium.com/analytics-vidhya/working-on-jupyter-notebooks-in-vs-code-from-virtual-conda-environment-f415726e329d).
  - Start Jupyter from the desired environment in a separate Anaconda prompt, and in VSCode, select Python interpreter from the Jupyter URL that was launched.

**R files**

**I haven't gotten the VSCode R Terminal for R version in `conda` environments to work!** The reason seems to be that the vanilla R terminal in versions coming with the custom conda environments is missing some required .dlls, preventing the R terminal from launching. This probably also prevents the launch of the VSCode Interactive R terminal (works just fine for a standalone R installation). If I only could get the vanilla terminal to work in the conda R versions, I think this would help with the VSCode terminal, too. Typical instructions for using the given R executable in VSCode would be as follows: 
  - Download VSCode extensions [R](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r) and make sure [R LSP Client](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r-lsp).
  - Install the R language service package into the conda environment: `mamba install r-languageserver`
  - Set the R and R LSP extension paths in VSCode settings.json. This can be done either at the global level or at the project level, as per usual with VSCode settings. Further instructions [in this video](https://www.youtube.com/watch?v=INP-FsluDuk&t) and [this article](https://medium.com/analytics-vidhya/a-fresh-start-for-r-in-vscode-ec61ed108cf6).

**R notebooks**

Previously, this was not possible, but might have been solved now. See [here](https://github.com/Microsoft/vscode-python/issues/5078).

### Calling R from a Python instance

Calling R from a Python instance is achieved using package `rpy2`. There are two examples of how to do this, and many more if you google them!
 - In *python.ipynb*, there is a Jupyter notebook example of how to pass items between different instances, using cell magic.
 - In *python.py*, there is an example of using rpy2 objects.

### Calling Python from an R instance

**I have not explored this yet**. Everything needed should be available via the *reticulate* package, however.

## Adding packages to environments

**Python/R packages using `conda`**

The benefit of using `conda` environments comes from managing dependencies between packages. When installing packages with `conda`, it tries to make sure that new packages do not cause conflicts in the environment. Thus, no matter if Python or R package, **always try installing packages via `conda` first** (or rather with `mamba`, which is a faster, drop-in replacement for `conda`):

```
conda activate <env_name>
mamba install <pckg_name>
```

**Python packages using pip**

Python packages tend to be well available via `conda` from Anaconda default channels or *conda-forge*. If a desired package is not available, one can also install packages via `pip` in the custom `conda` environment. Just make sure you are using pip installed in the `conda` environment. If this does not happen automatically (see *v1* below), then explicitly use `pip` of the correct `conda` environment by setting the path (see *v2* below). For more information see [here](https://stackoverflow.com/a/43729857) and [here](http://know.continuum.io/rs/387-XNW-688/images/conda-cheatsheet.pdf).

*pip install v1*
```
conda activate <env_name>
pip install <pckg_name>
```

*pip install v2*
```
conda activate <env_name>
conda install pip #if not done before
<path_to_env>/bin/pip install <pckg_name>
```

**Python packages using setup.py**

It is also possible to use manual *setup.py* installation, and it should be enough to just activate the environment with `conda activate dev`, following with `python /path/to/mypackage/setup.py install` (or replace `install` with `develop`). See [here)](https://stackoverflow.com/questions/26556865/anaconda-equivalent-of-setup-py-develop). Sometimes it might help to set the command directory as the package directory.

**R packages using install.packages()**

R packages are somewhat trickier than Python packages in `conda`. Newer versions of R packages arrive into `conda` with a lag or might not be available at all. Thus, installing via `conda` might not always work. In this case, we can use the R instance of the environment and call `install.packages()`:
 - Again, make sure that the only element in `.libPaths()` is the package directory for the R in the current `conda` environment (e.g. *~/Anaconda3/envs/dev/lib/R/library*).
- Try first without installing dependencies of the package, as we might be able to install them via `conda`. That is, `install.packages("mylib", dependencies=FALSE)()))`.
- If this fails or dependencies installed via `conda` have wrong versions available, let R installation also install dependencies: `install.packages("mylib", lib="some_R_lib_path", dependencies = TRUE)`.

## Notes about producing installation files for environments

Once an environment is ready, one could export it into files that can be used later to spin up the environment. However, building environments from these files does not usually work on different machines (not sure why).
 - (*OS unspecific*): Export e.g. *dev2018* environment to .yml `conda env export --no-builds > dev2018.yml` (why *--no-builds* see [here](https://github.com/ContinuumIO/anaconda-issues/issues/9480)). Remove explicit prefix from end. Then build environment later by `conda env create --file dev2018.yml`.
 - (*OS specific*): Export e.g. *dev2018* environment to .txt `conda list --explicit > dev2018.txt`. Then build environment later by `conda env create --name dev2018 --file nq_dev2018.txt`. If an error is raised, try removing the line "@EXPLICIT" from the file.

## Useful links
 - https://stackoverflow.com/questions/38066873/create-anaconda-python-environment-with-all-packages
 - https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533
 - https://community.rstudio.com/t/why-not-r-via-conda/9438/3
 - https://medium.com/analytics-vidhya/working-on-jupyter-notebooks-in-vs-code-from-virtual-conda-environment-f415726e329d
 - https://www.anaconda.com/blog/moving-conda-environments
