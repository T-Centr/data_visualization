import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams


rcParams['figure.figsize'] = 12, 10
sns.set_context("paper", font_scale=2)
data = pd.read_csv(
    "https://video.ittensive.com/python-advanced/data-9722-2019-10-14.utf.csv",
    delimiter=";"
)
data["AdmArea"] = data["AdmArea"].apply(lambda x: x.split(" ")[0])
sns.distplot(data["PASSES_OVER_220"]).set(xlabel='', ylabel='',
                                          title="Отличники по ЕГЭ по школам")
plt.show()

sns.swarmplot(x="PASSES_OVER_220", y="AdmArea", data=data).set(
    xlabel='', ylabel='', title="Отличники по ЕГЭ по округам")
plt.show()

sns.violinplot(x="PASSER_UNDER_160", y="AdmArea", data=data, cut=0)
plt.xlabel('')
plt.ylabel('')
plt.title('Хорошие результаты по ЕГЭ по округам')
plt.show()
