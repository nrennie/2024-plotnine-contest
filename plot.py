
# Load packages -----------------------------------------------------------

import plotnine as gg
import pandas as pd
import numpy as np
from string import Template

# Load data ---------------------------------------------------------------

events = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2024/2024-02-27/events.csv')
births = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2024/2024-02-27/births.csv')
deaths = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2024/2024-02-27/deaths.csv')


# Data wrangling

# Mutate and transform the dataframe
plot_births = births.copy()
plot_births['type'] = 'birth'
plot_births = plot_births.rename(columns={'year_birth': 'year'})
plot_births = plot_births[plot_births['year'] >= 1900]

# Using a template string for the label
def create_label(row):
    return f"{row['person']} ({row['description'].strip()})"

plot_births['label'] = plot_births.apply(create_label, axis=1)

# Calculations for theta, x, y, and angle
theta = np.linspace(np.pi / 4, (7 / 4) * np.pi, num=len(plot_births))
plot_births['theta'] = theta
plot_births['x'] = 6 * np.cos(theta)
plot_births['y'] = 6 * np.sin(theta)
plot_births['angle'] = 180 + 360 * (theta / (2 * np.pi))

plot_births <- births |>
  mutate(type = "birth") |>
  rename(year = year_birth) |>
  filter(year >= 1900) |>
  mutate(label = glue("{person} ({str_trim(description)})")) %>%
  mutate(
    theta = seq(pi / 4, (7 / 4) * pi, length.out = nrow(.)),
    x = 6 * cos(theta),
    y = 6 * sin(theta),
    angle = 180 + 360 * (theta / (2 * pi))
  )

plot_deaths <- deaths |>
  mutate(type = "death") |>
  rename(year = year_death) |>
  filter(year >= 1900) |>
  mutate(label = glue("{person} ({str_trim(description)})")) %>%
  mutate(
    theta = seq(pi / 4, (7 / 4) * pi, length.out = nrow(.)),
    x = 3 * cos(theta),
    y = 3 * sin(theta),
    angle = 180 + 360 * (theta / (2 * pi))
  )

# Load fonts --------------------------------------------------------------

# font_add_google('Roboto', 'roboto')
# font_add_google('Roboto Slab', 'roboto_slab')
# showtext_auto()


# Define colours and fonts-------------------------------------------------

bg_col = '#fafafa'
text_col = 'gray5'
highlight_col = '#35978f'

body_font = 'roboto'
title_font = 'roboto_slab'



# Define text -------------------------------------------------------------

social = nrBrand::social_caption(
  bg_colour = bg_col,
  icon_colour = highlight_col,
  font_colour = text_col,
  font_family = body_font
)
title = 'Take a leap! Births and deaths on February 29<sup>th</sup>'
st = glue('February 29 is a leap day (or 'leap year day'), an intercalary date
added periodically to create leap years in the Julian and Gregorian calendars. 
Wikpedia lists {nrow(dplyr::filter(births, year_birth >= 1900))}
<span style='color: {highlight_col};'>births</span> and {nrow(dplyr::filter(deaths, year_death >= 1900))}
<span style='color: #bf812d;'>deaths</span> on a leap day since 1900.')
cap = paste0(
  '**Data**: Wikipedia<br>**Graphic**:', social
)


# Plot --------------------------------------------------------------------

ggplot() +
  geom_textcircle(
    data = dplyr::filter(births, year_birth >= 1900),
    mapping = aes(label = person),
    colour = highlight_col,
    r = 6,
    family = body_font,
    size = 6,
  ) +
  geom_textcircle(
    data = dplyr::filter(deaths, year_death >= 1900),
    mapping = aes(label = person),
    colour = '#bf812d',
    r = 3,
    family = body_font,
    size = 6,
  ) +
  # add title and subtitle
  geom_textbox(
    data = data.frame(x = 0, y = 1.2, label = title),
    mapping = aes(x = x, y = y, label = label),
    hjust = 0,
    colour = text_col,
    family = title_font,
    fontface = 'bold',
    lineheight = 0.5,
    fill = 'transparent',
    box.colour = 'transparent',
    size = 11,
    minwidth = 0.5
  ) +
  geom_textbox(
    data = data.frame(x = 0, y = -0.5, label = st),
    mapping = aes(x = x, y = y, label = label),
    hjust = 0,
    colour = text_col,
    family = body_font,
    lineheight = 0.5,
    fill = 'transparent',
    box.colour = 'transparent',
    size = 9,
    minwidth = 0.45
  ) +
  scale_x_continuous(limits = c(-8, 8)) +
  scale_y_continuous(limits = c(-8, 8)) +
  labs(caption = cap) +
  theme_void(base_size = 30, base_family = body_font) +
  theme(
    plot.margin = margin(5, 5, 5, 5),
    plot.background = element_rect(fill = bg_col, colour = bg_col),
    panel.background = element_rect(fill = bg_col, colour = bg_col),
    plot.caption = element_textbox_simple(
      colour = text_col,
      hjust = 0,
      halign = 0,
      margin = margin(b = 5, t = -5, l = 5),
      lineheight = 0.5,
      family = body_font
    )
  )

