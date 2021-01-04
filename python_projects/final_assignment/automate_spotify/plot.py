import seaborn as sns
import matplotlib.pyplot as plt

bird= sns.load_dataset("penguins")
g = sns.FacetGrid(bird, col="island", hue="species")

g.map(plt.scatter, "flipper_length_mm", "body_mass_g", alpha=.6)
g.add_legend()
plt.show()

sns.stripplot(x="island", y="body_mass_g", hue= "species", data=bird, palette="Set1")
plt.show()

sns.swarmplot(x="island", y="body_mass_g", hue="species",data=bird, palette="Set1", dodge=True)
plt.show()

sns.lmplot(x="body_mass_g", y="culmen_length_mm", hue="sex", col="island", markers=["o", "x"],palette="Set1",data=bird)
plt.show()

sns.lmplot(x="body_mass_g", y="culmen_length_mm", hue="sex", col="island",row="sex",order=2, markers=["o", "x"],palette="Set1",data=bird)
plt.show()

sns.set_palette("gist_rainbow_r")
sns.jointplot(x="body_mass_g", y="culmen_length_mm", kind="hex",data=bird )
plt.show()

g = sns.jointplot(x="body_mass_g", y="culmen_length_mm", data=bird, kind="hex", color="c")
g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
g.set_axis_labels("Body Mass (in gram)", "Culmen Length ( in mm)")

plt.show()
sns.pairplot(bird, hue="island")
plt.show()