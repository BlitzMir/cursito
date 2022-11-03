from turtle import color
import matplotlib.pyplot as mpl

sales={
    "2018": 10000,
    "2019":25000,
    "2020": 17000,
    "2021": 28000
}

names = list(sales.keys())
values = list(sales.values())


mpl.barh(range(len(sales)),values, tick_label=names, color= ["blue", "yellow", "teal", "crimson"])
mpl.grid(True)
mpl.xticks(rotation=90)
mpl.title("Ventas de Productos (2018-2020)",loc="left", fontdict={"fontsize":14, "fontweight":"bold", "color":"tab:blue"})
mpl.xlabel("Años", color="teal", size=12)
mpl.ylabel("Cantidad", color="teal", size=12)
mpl.show()