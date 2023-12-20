# Using standalone R in conjunction with `conda` environments

**By Ville Voutilainen, updated 2023-12-20.**

**MIT license, usage at one's own risk!**

This note explains how to install and use a standalone R version in conjunction with tailored `conda` environments, as explained in the text [[condaenv.md]]. A standalone R installation might be useful as R packages in Anaconda default channels update slowly and might not always be available.

A very good text on installing and using R can be found in [Efficient R Programming](https://csgillespie.github.io/efficientR/).

## Notes on R environments

R sessions are controlled using hte files *.Rprofile* and *.Renviron*. In order to use R effectively, we need to specify some needed content for these files. More information on these files can be found [here](https://support.rstudio.com/hc/en-us/articles/360047157094-Managing-R-with-Rprofile-Renviron-Rprofile-site-Renviron-site-rsession-conf-and-repos-conf) and [here](https://csgillespie.github.io/efficientR/set-up.html#r-startup).

There are three places where R searches for *.Rprofile* and *.Renviron* (in order of search): 
 1. Current project — `getwd()`
 2. *HOME* — `Sys.getenv("HOME")`
 3. *R_HOME* — `Sys.getenv("R_HOME")`

How to use the control files depends on the needed use of R.

### Case with multiple R versions

If we want to be able to run different versions of standalone R on the machine, the *HOME* level is too broad, as then multiple R instances would be using the same files. A preferable option would be to have the control files at the level of *R_HOME*, separately for each standalone R version. Unfortunately, it seems that putting the control files under *R_HOME* does not work for some reason (the R session does not find the files, even when there are no files in the other two preferred paths).

This leaves us with the project-level option. That is, we will have separate *.Rprofile* and *.Renviron* files for each project. This is perhaps slightly inconvenient, but at the end of the day, not too big of a hindrance, as we can simply copy the prepared files under each project.

If we only need to set *.Rprofile* and don't need *.Renviron*, things become easier: *.Rprofile* can be sourced in a session in a custom manner when needed, whereas *.Renviron* is sourced on session start only from the three paths given below. This means that we could store *.Rprofile* in a single custom path (and not in every project folder) and source it manually when needed (this will actually become handy when installing a Jupyter R kernel; see below).

### Case with a single R version

When we are sure we don't need multiple standalone R versions, we can simply put both *.Rprofile* and *.Renviron* under *HOME*.

##  R standalone installation

Next, we describe the procedure for installing a standalone R program. The installation will be called `r_sa_2021` and includes R version 4.1.0.

### R program installation

 -  Download the R program from [here](https://cran.r-project.org/bin/windows/base/) and install it using the wizard.
 - Find and remove default control files *.Rprofile* and *.Renviron*:
   - Level *HOME*: `Sys.getenv("HOME")` 
   - Level *R_HOME*: `Sys.getenv("R_HOME")` 
 - Add a folder *"R-x.x.x-packages"* (where x's correspond to the R version number being installed) in a path of choice.
   - The path may be *R_HOME*, as long as the user has read and write rights to the folder. For example, if *R_HOME* is behind admin rights and the user is not an admin, then *R_HOME* won't do it.
 - Add two folders in the created folder: *rfiles* and *packages*.

### Rtools installation

RTools is needed to build R packages from source.

 - Install RTools from [here](https://cran.r-project.org/bin/windows/Rtools/). The tested version is *rtools40v2-x86_64.exe*.
   - This installs folder *rtools40* with RTools in a chosen path.
 - Add *RTOOLS40_HOME* to Windows PATH (if it does not happen automatically): Environment variables -> User variables -> Name: RTOOLS40_HOME, Path: "path_to_rtools" (e.g., "C:\Program Files\rtools40").

### RStudio installation

Optionally, one can also install RStudio.

### Preparing control files

Next, we prepare the needed control files.

#### Case with multiple R versions

Prepare project-level *.Rprofile* file and place it in the project folder. The file will specify the previously created folder as the place to store installed packages.

```
message(".Rprofile has been loaded from <project name here>!")
.libPaths("my_custom_path/R-x.x.x-packages/packages")
```

Prepare another "R installation level" *.Rprofile* file. This is meant for the R Jupyter kernel. We can put the file into a custom path, say the above-created *rfiles* folder, or under *R_HOME* (the kernel specs will explicitly refer to this file with a path).

```
message(".Rprofile has been loaded from rfiles folder!")
.libPaths("my_custom_path/R-x.x.x-packages/packages")
```

Finally, prepare a project-level *.Renviron* file and place it in the project folder. The point is to adjust the PATH variable so that Rtools can be found.

```
# Adjust PATH variable so that Rtools can be found
PATH="${RTOOLS40_HOME}\usr\bin;${PATH}"
```

#### Case with a single R version

Prepare *.Rprofile* and *.Renviron* files and place them under *HOME*.

*.Rprofile*:
```
message(".Rprofile has been loaded from HOME!")
.libPaths("my_custom_path/R-x.x.x-packages/packages")
```

*.Renviron*:
```
# Adjust PATH variable so that Rtools can be found
PATH="${RTOOLS40_HOME}\usr\bin;${PATH}"
```

### Using standalone R installation

#### Case with multiple R versions

Launch R (or RStudio) from the command prompt in the project folder (be careful with Windows paths, spaces need to be dealt with: `C:\Program^ Files\R\R-4.1.0\bin\R.exe`). This way we are using the project-level *.Rprofile* and *.Renviron* files.
   
```
cs project_folder
path/to/R/bin/R.exe
```

Next, test that everything crucial works:
  - On launch, we should see the custom message from the project-level *.Rprofile*.
  - Test that Rtools can be found: `Sys.which("make")` should return the RTools path. Then, test source installation. For example, using `install.packages("jsonlite", type="source")`.

#### Case with a single R version

Simply launch R. Test that everything crucial works, as in the case with multiple R installations.

### Using standalone R with tailored `conda` environments (in Jupyter)

We need to install R kernel so that `conda` environments know from where to use the standalone R installation (see [here](https://irkernel.github.io/installation/) and [here](https://github.com/IRkernel/IRkernel/blob/master/R/installspec.r)).

 - Install the kernel among the other kernels created for tailored `conda` environments by running the following code in the standalone R instance. The important thing is to point to the "R installation level" *.Rprofile* file created above:

    ```
    install.packages('IRkernel')
    IRkernel::installspec(name='r_sa_2021', displayname='r_sa_2021', prefix="path_to_kernels/jupyter/kernels", rprofile="~/R-x.x.x-packages/rfiles/.Rprofile")
    ```
   - The command may create extra folder layers. Remove them by locating the folder *r_sa_2021* and copy-paste it to the same level as the rest of the kernels. Delete empty folder layers.
 
Some important additions:

  - Python installations in the `conda` environments do not by default know where to look for the standalone R installation. When running R from Python, we need to specify the path to the standalone R installation (the path can be something like "C:\Program Files\R\R-x.x.x"):

    ```
    import os
    os.environ['R_HOME'] = 'path to R folder'
    ```
 - Note that when running the standalone R through Jupyter, it does not get to know the content of proper *.Renviron* (it might see the content of other such files from a `conda` environment installation), so that, e.g., RTools might point to an incorrect source (try with `Sys.which("make")`). This means that, e.g., all Rtools-related stuff must be done in a "proper" R instance, not via the Jupyter kernel.

## Sources :
 - https://csgillespie.github.io/efficientR/set-up.html#r-startup
 - https://support.rstudio.com/hc/en-us/articles/360047157094-Managing-R-with-Rprofile-Renviron-Rprofile-site-Renviron-site-rsession-conf-and-repos-conf
 - https://stackoverflow.com/questions/63680272/install-two-versions-of-rtools
 - https://cran.r-project.org/bin/windows/Rtools/
 - https://stackoverflow.com/questions/46819684/how-to-access-and-edit-rprofile