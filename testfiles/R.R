######################################
# Minimalistic .R test file
# See R.ipynb for more robust tests.
######################################

# Show paths of R.exe and import paths
print(file.path(R.home("bin"), "R"))
print(.libPaths())

# Test imports
library(tidyverse)
library(ggplot2)
library(datasets)

# Test tidyverse packages
data(iris)
iris.means <- iris %>%
  group_by(Species) %>%
  summarize(SL.mean = mean(Sepal.Length),
            SL.se = sd(Sepal.Length)/sqrt(n()))
print(iris.means)

ggplot(
  data=iris.means,
  mapping=aes(x = Species, y = SL.mean)
) +
geom_point() +
geom_errorbar(
  mapping=aes(ymin = SL.mean - SL.se, ymax = SL.mean + SL.se),
  width = 0.3
)
