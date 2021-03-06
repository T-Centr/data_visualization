import matplotlib.pyplot as plt
import geopandas as gpd
import descartes


data = gpd.read_file("https://video.ittensive.com/python-advanced/moscow.json")
data = data.to_crs({'init': 'epsg:3857'})
fig = plt.figure(figsize=(8, 8))
area = plt.subplot(1, 1, 1)
data[data["NAME_AO"] == "Центральный"].plot(
    ax=area, legend=True, column="NAME", cmap="tab20")
plt.show()

fg = plt.figure(figsize=(20, 16))
area = plt.subplot(1, 1, 1)
data.plot(ax=area, legend=True, column="NAME_AO", cmap="tab20")
plt.show()
