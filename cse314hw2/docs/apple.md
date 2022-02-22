# Apple Stock Dataset (2014)

For full dataset view [plotly/datasets/2014_apple_stock.csv](https://github.com/plotly/datasets/blob/master/2014_apple_stock.csv).

## Overview

* ###Why the visualization is interesting?<br />
    - Users can easily choose the date range from a calendar.


## Demo

![appl_DEMO](demo_pics/appl_DEMO.png)

## Callbacks

`update_AAPL_fig(start_date,end_date)` - Update x-axis range of the APPL line graph according to the selected date range

**Parameters:**<br />
** - start_date: ** `date object` start date, will be converted to string in `YYYY-MM-DD` format<br />
** - end_date: ** `date object`  end date, will be converted to string in `YYYY-MM-DD` format<br />
** - returns: ** `figure` a line graph with updated date range that will be passed into the dcc.Graph component<br />

![appl_callback](demo_pics/appl_callback.png)