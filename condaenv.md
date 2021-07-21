# `conda` data science environments

**By Ville Voutilainen/NoobQuant, updated 2021-07-21.**

**MIT license, usage at one's own risk!**

## Introduction

This article is my "cookbook recipe" on how to build tailored `conda` environments for everyday data science work with Python and R. The article covers following topics:

 - How to install `conda` environments containing fresh Python and R installations;
 - How to install packages to the environments;
 - How to run Python and R instances, separately and together, in Jupyter Lab, VSCode, and RStudio.

The instructions are written for a **Windows 10 machine**. They might be applicable to other operating systems to some degree, but no guarantees are made.

### What are Anaconda, `conda`, and `conda` environments?

[Anaconda](https://www.anaconda.com/) is a popular data science platform for several programming languages, most notably Python and R. Anaconda is also a company pursuing all kinds of ends, but here we focus on the software it provides. Anaconda lets you run Python and R in virtual **environments**, which constitute a logically separable playing fields for your data science experiments. The environments can be loaded up with different versions of Python and R programs as well as bundles of **packages** (aka. libraries) that power your work. Both environments and packages are managed with `conda`, the package manager of Anaconda.

### Why to use tailored NoobQuant `conda` environments for data science work?

Python and R are great tools for data science. The web is full of discussions which one is better, but in my opinion these conversations often miss the mark. Each language has its own advantages and there are huge benefits in being able to flexibly change between the two.

For example, Python is great for machine learning as well as for general infrastructure around the data science workflow. On the other hand, R offers a much broader set of statistical tools. The goal of this article is to build an environment where one can employ the best parts of both worlds, on the fly!

A clear advantage of `conda` comes with its dependency management capabilities. Maintaining Python or R packages and versions can be a hazzle, let alone doing the same for both. `conda` environments are, according to my knowledge, the best way to manage package and program versions over time and across each other. It offers reproducible data science environments that one can spin up whenever needed. Being diligent about the software versions will make life much easier and may save you from the cardinal sin of producing irreproducible science and/or code.

With **NoobQuant `conda` environments** one can, for example:

 - Run Python in VSCode or Jupyter Lab;
 - Run R in RStudio or Jupyter Lab;
 - Call R code from a Python instance with *rpy2*;
 - Use typical Python data science packages such as *pandas* and *scikit learn*;
 - Use typical R data science packages such as *tidyverse*.
 - Fetch economic time series from public APIs using *rjsdmx*.

### When **not** to use NoobQuant `conda` environments?

The custom environments I use are not perfect nor suited for every occasion. They have evolved based on personal preferences of someone who does most of the work in Python, but every now and then needs R for running statistical analyses.

NoobQuant `conda` environments proposed in this article may not be for you if:

 - **You solely use R**. R environment dependency management as itself might be easier with other tools, such as *packrat*. The power of `conda` environments comes from Python package management and combining that with R or even Julia. Also, `conda` often does not offer latest R packages.
 - **You are afraid of getting your hands dirty**. Installing and managing `conda` environments might be time consuming at times, although in the long run I believe it pays for itself in reproducibility. If you do not like the "extra" work that comes with being able to fully customize the tools for your needs, then NoobQuant `conda` environments might not be your thing.

## Building tailored `conda` environments

### Download and install Anaconda

First, we need to install Anaconda. One could also download a stripped version of Anaconda, called Miniconda, but in this article we focus on Anaconda. Anaconda distributions can be do installed from [here](https://repo.anaconda.com/archive/). Miniconda distributions can be do installed from [here](https://repo.anaconda.com/miniconda/).

**\<optional\>**

If there have been previous Anaconda installations on your machine, check that no previous specification files are haunting in the directories. Typical suspects outside *~/Anaconda/* folder are:

 - Anacondarelated
    - C:\Users\<my_user_name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3
 - Jupyter related
   - C:\Users\<my_user_name>\.jupyter
   - C:\Users\<my_user_name>\.ipynb_checkpoints
   - C:\Users\<my_user_name>\.ipython
   - C:\ProgramData\jupyter
   - C:\Users\<my_user_name>\AppData\Roaming\jupyter
 - `conda` related
   - C:\Users\<my_user_name>\.conda
 - Python packages related
   - C:\Users\<my_user_name>\.matplotlib
   - C:\Users\<my_user_name>\.keras
   - etc.
 - Windows environment variables: remove all Anaconda related paths.

**\</optional\>**

In this article we use Anaconda version *2020.02-Windows-x86_64*. Download and run the installer. Install the software to preferred path. When installing, uncheck *"Register Anaconda3 as my default Python"* (we don't want to use Python in `base` environment as our default). Also check the *"add to path"* checkbox (although it is not recommended by the wizard). Following window paths added are:

  - *~/Anaconda3*
  - *~/Anaconda3/Library/mingw-w64/bin*
  - *~/Anaconda3/Library/usr/bin*
  - *~/Anaconda3/Library/bin*
  - *~/Anaconda3/Scripts*

### Installing environments

Open Anaconda prompt, where most of the commands will be given. We start by telling `conda` to add a few extra channels to the list where to look for packages from. The channels to be added are *conda-forge* and *r*. Python packages tend to be faster available in *conda-forge* than in default channels. *r* is needed for R packages.

```
conda config --add channels conda-forge
conda config --add channels r
```

Next, install [mamba](https://github.com/TheSnakePit/mamba) in the `base` conda environment. `mamba` is a faster, drop-in replacement for `conda`. Later we will replace `conda` commands with `mamba` for increased speed in solving package dependencies.

```
conda install mamba
```

Now we can install a custom `conda` environment. There are two tested *NoobQuant* `conda` environments. One can also both, but make sure to complete the installation fully for each environment before starting with the other.

 - `dev2018`: Year 2018 version with Python 3.6.10 and R 3.6.0
 - `dev2021`: Year 2021 version with Python 3.8.5 and R 3.6.3

To build either one of the environments, run commands as detailed in subsections.

#### dev_2018: Year 2018 version with Python 3.6.10 and R 3.6.0

```
mamba create --name dev2018 anaconda python=3.6 numpy=1.16.4 numpy-base=1.16.4 tzlocal=2.0.0 pandas=0.25.0 seaborn=0.11.0 rpy2==2.9.4 r=3.6.0 r-base=3.6.0 r-essentials=3.6.0 r-tidyverse=1.2.1 rtools=3.4.0 r-rjsdmx=2.1_0 r-seasonal=1.7.0 rstudio=1.1.456
```

#### dev_2021: Year 2021 version with Python 3.8.5 and R 3.6.3**

```
mamba create --name dev2021 anaconda=2020.11 rpy2=3.4.2 r-base=3.6.3 r-essentials=3.6 rtools=3.4.0 r-rjsdmx=2.1_0 r-seasonal=1.8.1
```
Note about *dev_2021*:
 - There is a problem with *rstudio* installation for this environment. RStudio version 1.1.456, which is the newest available in `conda`, seems too old for the environment set-up. This causes an error and prevents installation of RStudio. We might be able to use a standalone installation of RStudio and connect it to the R in *dev2021*, but this might lead to problems when switching between R installations. For this reason, before *r-rstudio* package is updated for Anacondawe cannot install RStudio into `dev2021` environment.

### Jupyter kernel set-up for new environments

*Jupyter notebooks* are my preferred way to use Python and R. In order to use the freshly installed Python and R versions in Jupyter notebooks, we need to install *kernels* that tell Jupyter from where to look for the programs. To this end, we specify kernels with unique names so that we can have IPython/IR kernels for each `conda` environment separately (see more [here](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)).

Run following commands in `conda` prompt to install Python and R kernel for the environment. Here we use `dev2021` as an example. Change the names depending on which environment was installed.

```
conda activate dev2021
python -m ipykernel install --user --name dev2021_py --display-name "dev2021_py"
R
IRkernel::installspec(name='dev2021_r', displayname='dev2021_r')
quit()
```

This should add two folders under Jupyter kernels directory (typically under *C:\Users\<myusername>\AppData\Roaming\jupyter\kernels*). Check that the folders are created.

### Testing the installations

Finally, run test files to see if everything works:

 - python.py (e.g. in VSCode);
 - python.ipynb (in Jupyter or VSCode);
 - R.R (e.g. in RStudio installed with the environment);
 - R.ipynb (in Jupyter).

See section *Using NoobQuant `conda` environments* below for more on how to run the examples.

## Using NoobQuant `conda` environments

In this section we cover tips on how to use the new `conda` environment. There are some general tips that one should consider:

 - Make sure Python executable points to one in the new `conda` environment (check with `import sys; print(sys.executable)`). The path should be something like *~/Anaconda3/envs/<env_name>/python.exe*. Also make sure that Python import paths include the packages directory of the new environment (check with `print(sys.path)`). The path should be something like *~/Anaconda3/envs/<env_name>/~*.
 - Make sure R executable points to one in the new `conda` environment (check with `print(file.path(R.home("bin"))`). The path should be something like *~/Anaconda3/envs/<env_name>/lib/R/bin/x64*. Also make sure R import paths contain **only** the packages directory of the new environment (`print(.libPaths())`). The path should be something like *~/Anaconda3/envs/<env_name>/lib/R/library*. If there are other paths, reset the paths using `.libPaths("~/Anaconda3/envs/<env_name>/lib/R/library")`.

### Using Python and R in Jupyter Lab

To launch a Python/R instance in Jupyter notebooks, first select the installed environment and then launch Jupyter Lab:

```
conda activate dev2021
jupyter lab
```

This opens up Jupyter Lab in the browser. If Jupyter kernels for the environment were correctly set up, they will be visible on the launcher page. Test running *python.ipynb* (here with *dev2021* environment) in `dev2021_py` kernel and *R.ipynb* using `dev2021_py` kernel. Make sure you choose a correct kernel for each notebook (top-right corner).

Common problems that might arise:

- If Jupyter kernel dies/restarts when running *rpy2* commands, the reason might be that `R HOME` path is not set and *rpy2* does not find the R installation that came with the environment. In this case we need to add a path for R in this particular Python kernel:
  - Find the *kernel.json* for Python Jupyter kernel (e.g. *~/jupyter/dev2021_py/kernel.json*)
  - Add `"env": {"R_HOME":"/home/your/anaconda3/envs/my-env-name/lib/R"}`, see [this](https://stackoverflow.com/a/60869259/7037299). Also helpful might be [this](https://stackoverflow.com/questions/39347782/getting-segmentation-fault-core-dumped-error-while-importing-robjects-from-rpy2/53639407#53639407).
- One problem with R in Jupyter notebooks might be that `.libPaths()` contains other library paths (from different standalone R versions) that precede the correct one of the `conda` environment. When this happens, wrong packages might be used on notebook loadout, and these packages cannot be reloaded. This can cause compatibility problems with other packages in the notebook instance. The solution I can recommend is to be pedantic about R packages management. In particular, do not install any R packages into Windows *HOME* path (usually *User/Documents*) where other R versions might pick them up from. Always use separate package folders (outside of *HOME*) for each R version! See more about R load-up in text *standalone_r.md*.
- In theory, Python and R kernels of the new `conda` environment should be accessible in Jupyter when run from *base* `conda` environment, see [here](https://ipython.readthedocs.io/en/stable/install/kernel_install.html) under section *"you can make your IPython kernel in one env available to Jupyter in a different env"*. However, I have run to all kinds of problems with the R kernel, e.g. [this](https://github.com/IRkernel/IRkernel/issues/309), [this](https://github.com/jupyter/jupyter/issues/353), and R installation not being found when called from Python instance with *rpy2*. Thus, I have found it easier to use Jupyter Lab from within each `conda` environment. This is why we install Jupyter in every environment and not just in `base` as usually suggested (see e.g. discussion [here](https://stackoverflow.com/a/39623487/7037299)). Make sure to launch Jupyter from custom environment (e.g. first `conda activate dev2021`, and only then `jupyter lab`).

### Using R in RStudio

If package *r-rstudio* was installed with the environment, launch RStudio from Anaconda prompt, from the desired command folder path:
```
cd <desired command folder path>
conda activate dev2018
rstudio
```

Then use R Studio as per usual.

Troubleshoot:
 - If opened R files suddenly appear empty in RStudio, one needs to reopen the file with UTF-8 encoding. See [this](https://stackoverflow.com/a/45034170/7037299).

### Using Python and R in VSCode

VSCode is one of the best overall IDE's for data science. Thanks to its many plugins we can run both Python and R from our custom `conda` in VSCode.

**Python files**

To begin with, install [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) plugin for VSCode. Next, make sure the desired custom environment (e.g. `dev2021`) Python interpreter is selected in VSCode (bottom-left). Then from the *.py* file, right-click and choose *Run Python file in terminal*. This creates a new Python terminal and executes the file. One can also *Run selection/line in Python terminal* to run a specific section. To exit,  type `quit()` to close the Python instance. One can also run file/section of it in interactive terminal, in which case VSCode launches Jupyter to create an interactive window. I would not recommend this too much, however. Rather use notebooks for interactive computing.

**Python notebooks**

Make sure that VSCode launches Jupyter instance by from desired custom `conda` environment (by default VSCode launches Jupyter from `base`). Two ways to do this:
  - Make sure we can run *conda* commands from powershell terminal by running in Anaconda terminal `conda init powershell` (see [here](https://stackoverflow.com/questions/47800794/how-to-activate-different-anaconda-environment-from-powershell/54811138)). Then open powershell terminal in VSCode, run `conda activate dev2021`. Then make sure that 1) selected VSCode Python interpreter (bottom-left) and 2) the Jupyter interpreter (top-right) both correspond to the Python version installed in the environment. Now launch a Python notebook and things should work. See more [here](https://medium.com/analytics-vidhya/working-on-jupyter-notebooks-in-vs-code-from-virtual-conda-environment-f415726e329d).
  - Start Jupyter from desired environment in a separate Anaconda prompt and in VSCode select Python interpreter from the Jupyter url that was launched.

**R files**

**Cannot get the VSCode R Terminal for R version in conda environment to work!** The reason seems to be that the vanilla R terminal in versions coming with the NoobQuant conda environments is missing some required .dlls, preventing R terminal from launching. This probably also prevents the launch of VSCode Interactive R terminal (works just fine for a standalone R installation). If I would only get the vanilla terminal to work in the conda R versions, I think this would help with VSCode terminal, too. Typical instructions for using given R executable in VSCode would be as follows: 
  - Download VSCode extensions [R](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r) and make sure [R LSP Client](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r-lsp).
  - Install R language service package to the conda environment: `mamba install r-languageserver`
  - Set R and R LSP extension paths in VSCode settings.json. This can be done either at global level or at project level as per usual with VSCode settings. Further instructions [in this video](https://www.youtube.com/watch?v=INP-FsluDuk&t) and [this article](https://medium.com/analytics-vidhya/a-fresh-start-for-r-in-vscode-ec61ed108cf6).

**R notebooks**

Not yet possible, but coming: see [here](https://github.com/Microsoft/vscode-python/issues/5078).

### Calling R from a Python instance

Calling R from a Python instance is achieved using package *rpy2*. There are two examples how to do this, and many more if you google them!
 - In python.ipynb there is a Jupyter notebook example how to pass items between different instances, using cell magics.
 - In python.py there is an example using rpy2 objects.

### Calling Python from an R instance

**I have not explored this yet**. Everything should be directly available using *reticulate* package, however.

## Adding packages to environments

**Python/R packages using `conda`**

The benefit of using `conda` environments comes from managing dependencies between packages. When installing packages with `conda`, it tries to make sure that new packages do not cause conflicts in the environment. Thus, no matter if Python or R package, **always try installing packages first via `conda`** (or rather with `mamba`, which is a faster, drop-in replacement for `conda`):

```
conda activate <env_name>
mamba install <pckg_name>
```

**Python packages using pip**

Python packages tend to be well available via `conda`. If a desired package is not available, one can also install packages via `pip` in the custom `conda` environment. Just make sure you are using pip installed in the `conda` environment. If this does not happen automatically (see *v1* below), then explicitly use `pip` of the correct `conda` environment by setting the path (see *v2* below). For more information see [here](https://stackoverflow.com/a/43729857) and [here](http://know.continuum.io/rs/387-XNW-688/images/conda-cheatsheet.pdf).

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

It is also possible to use manual *setup.py* installation and it should be enough to just activate the environment with `conda activate dev`, following with `python /path/to/mypackage/setup.py install` (or replace `install` with `develop`). See [here)](https://stackoverflow.com/questions/26556865/anaconda-equivalent-of-setup-py-develop). Sometimes it might help to set command directory as the package directory.

**R packages using install.packages()**

R packages are somewhat trickier than Python packages in `conda`. Newer versions of R packages arrive into `conda` with a lag or might not be available at all. Thus, installing via `conda` might not always work. In this case we can use the R instance of the environment and call `install.packages()`:
 - Again, make sure that the only element in `.libPaths()` is the package directory for the R in in the current `conda` environment (e.g. *~/Anaconda3/envs/dev/lib/R/library*).
- Try first without installing dependencies of the package, as we might be able to install then via `conda`. That is, `install.packages("mylib", dependencies=FALSE)()))`.
- If this fails or dependencies installed via `conda` have wrong versions available, let R installation also install dependencies: `install.packages("mylib", lib="some_R_lib_path", dependencies = TRUE)`.

## Notes about producing installation files for environments

Once an environment is ready, one could export it into files that can be used later to spin up the environment. However, building environments from these files does not usually work on different machines (not sure why).
 - (*OS unspecific*): Export e.g. *dev2018* environment to .yml `conda env export --no-builds > dev2018.yml` (why *--no-builds* see [here](https://github.com/ContinuumIO/anaconda-issues/issues/9480)). Remove explicit prefix from end. Then build environment later by `conda env create --file dev2018.yml`.
 - (*OS specific*): Export e.g. *dev2018* environment to .txt `conda list --explicit > dev2018.txt`. Then build environment later by `conda env create --name dev2018 --file nq_dev2018.txt`. If error is raised, try removing line "@EXPLICIT" from the file.

## Useful links
 - https://stackoverflow.com/questions/38066873/create-anaconda-python-environment-with-all-packages
 - https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533
 - https://community.rstudio.com/t/why-not-r-via-conda/9438/3
 - https://medium.com/analytics-vidhya/working-on-jupyter-notebooks-in-vs-code-from-virtual-conda-environment-f415726e329d
 - https://www.anaconda.com/blog/moving-conda-environments
