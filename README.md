# 2024 `plotnine` contest

This repository contains code for my entry in the [2024 Plotnine Contest](https://posit.co/blog/announcing-the-2024-plotnine-contest/). 

<img src="plot.png" width="100%" alt="area chart of carbon emissions">

## Data 

The data is available from [github.com/rfordatascience/tidytuesday/blob/master/data/2024/2024-05-21/readme.md](https://github.com/rfordatascience/tidytuesday/blob/master/data/2024/2024-05-21/readme.md). The original data can be downloaded from [carbonmajors.org/Downloads](https://carbonmajors.org/Downloads). The Carbon Majors dataset is available for download and for non-commercial use, subject to InfluenceMap's [Terms and Conditions](https://influencemap.org/terms). The version used in this plot was downloaded in May 2024.

## Code

The code to reproduce the figure can be found in `plot.py`, and the source code for a more detailed tutorial can be found in the `index.qmd` file which is deployed at [nrennie.github.io/2024-plotnine-contest](https://nrennie.github.io/2024-plotnine-contest). This site is deployed with GitHub Actions, demonstrating that the plot is fully reproducible.

This entry for the `plotnine` contest was inspired by a visualisation I previously created using `{ggplot2}` in R for [#TidyTuesday](https://github.com/rfordatascience/tidytuesday/blob/master/data/2024/2024-05-21/readme.md). You can see the original R version at [github.com/nrennie/tidytuesday/tree/main/2024/2024-05-21](https://github.com/nrennie/tidytuesday/tree/main/2024/2024-05-21).

## Fonts

This plot uses `"Arial"` font. The code checks if 'Arial' is available on your operating system, and if it is not will use the default `sans` font instead. Alternatively, you change the variable `body_font` to the name of a font that you do have installed.
