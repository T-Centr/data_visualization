import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats


sns.set_context("paper", font_scale=2)
data = pd.read_csv(
    "https://video.ittensive.com/python-advanced/data-9722-2019-10-14.utf.csv",
    delimiter=";"
)
data["AdmArea"] = data["AdmArea"].apply(lambda x: x.split(" ")[0])
data1 = pd.DataFrame(data, columns=["PASSES_OVER_220", "PASSER_UNDER_160",
                                    "AdmArea"])
sns.pairplot(data1, hue="AdmArea", height=6)
plt.show()

sns.jointplot("PASSES_OVER_220", "PASSER_UNDER_160", data, height=12,
              kind="kde").annotate(stats.pearsonr)
plt.show()

print(round(stats.pearsonr(data["PASSES_OVER_220"],
                           data["PASSER_UNDER_160"])[0], 2))
