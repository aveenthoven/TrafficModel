## FrieslandModel

This part of the project is about modelling the roads of Friesland, from raw data from NDW (Nationaal Dataportaal Wegverkeer)
to a simplified graph. This is done in the following notebooks `road analysis.ipynb`, `road analysis 2.ipynb`, `road analysis 3.ipynb`.

> **Note**: To run this locally, use `git clone` instead of downloading the zip-file of this repository, otherwise the shapefiles
> may not be read correctly.

### Notebook `road analysis.ipynb`

This uses the dataset 'Snelheden' from the NDW (see [open data NDW](https://opendata.ndw.nu/)), which is stored within
`wegen.7z`. The notebook extracts this dataset to this directory automatically if it isn't done already, due to the large file size.
Alternatively, it can be extracted manually.

This notebook is primarily used to analyze the dataset Snelheden but also generates the dataset `friesland.shp`.
The dataset `friesland.shp` contains only the provincial and state roads of Friesland.
From this dataset, a graph is constructed which eliminates 2-degree nodes, which then is stored as a shapefile
to `./wegengraaf/lines.shp` and `./wegengraaf/points.shp`.

### Notebook `road analysis 2.ipynb`

The notebook `road analysis 2.ipynb` uses `momepy` and `cityseer` to simplify the graph of `friesland.shp`.
Also includes the 2-degree node elimination again. Before storing it as a shapefile again, the amount of attributes is reduced (less columns). The data is stored to `./wegengraaf2/`.

Now, the dataset from `./wegengraaf2/` is manually edited using QGIS to remove errors etc. This is done a couple of times, so it is recommended to
not change any shapefiles from `./wegengraaf2/` or use `road analysis 2.ipynb` to generate the dataset, except when using it to create new datasets.

When manually editing the `wegengraaf2`-dataset, it is recommended to plot the lines and edges as a graph without line geometry, such that wrong connections become clear. (See parts of `shortest path graph.ipynb`).

The polygon shapefile `cities.shp` is used to show where the cities are when
drawing the map with the nodes and edges. This is created manually. 

### Notebook `road analysis 3.ipynb`

This notebook processes `wegengraaf2` again, changing the CRS to a local one such that the lengths can be recalculated. Also contains previews of the dataset and shows a map of the nodes and edges with the cities.
Goal of this notebook is to remove errors from the dataset automatically, when it is too time-consuming to do it by hand.

### Notebook `shortest path graph.ipynb` and `extended graph model.ipynb`

This notebook uses the `wegengraaf2`-dataset to model the traffic in Friesland.
For now, this only includes shortest path implementations of the road network `wegengraaf2`.

The notebook `extended graph model.ipynb` is based on `shortest pat graph.ipynb`.