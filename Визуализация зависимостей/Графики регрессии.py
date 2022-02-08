import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams


rcParams['figure.figsize'] = 12, 12
sns.set_context('paper', font_scale=2)
data = pd.read_csv(
    "https://video.ittensive.com/python-advanced/data-9722-2019-10-14.utf.csv",
    delimiter=";"
)
data["AdmArea"] = data["AdmArea"].apply(lambda x: x.split(" ")[0])
data["District"] = data["District"].str.replace(" район", "")
data["EDU_NAME_TITLE"] = data["EDU_NAME"].apply(
    lambda x: x.split(" ")[-1].replace("»", "")
)
sns.lmplot(x="PASSES_OVER_220", y="PASSER_UNDER_160", data=data, col="AdmArea",
           col_wrap=3, truncate=True)
plt.show()

data1 = data.set_index("AdmArea").loc["Центральный"]
sns.lmplot(x="PASSES_OVER_220", y="PASSER_UNDER_160", data=data1,
           col="District", col_wrap=3, truncate=True)
plt.show()

data2 = data1.set_index("District").loc["Басманный"]
sns.lmplot(x="PASSES_OVER_220", y="PASSER_UNDER_160", data=data2,
           col="EDU_NAME_TITLE", col_wrap=3, truncate=True)
plt.show()

pd.options.display.max_colwidth = 1000
print(data2.set_index('EDU_NAME_TITLE').loc["экономики"]["EDU_NAME"])
