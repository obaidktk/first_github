# # step1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt
# # step 2 set theme
sns.set_theme(style="ticks",color_codes=True)
# # # step 3load dataset
kashti= sns.load_dataset("titanic")
# # # step 4 plot basic graph eith one varibale
# p=sns.countplot(x="sex",data=kashti)
# # plt.show()

# # # step 5 plot basic graph with two variable(count plot)
# p=sns.countplot(x="sex",data=kashti, hue="class")
# # plt.show()

# step 6 plot basic graph with two variable (count plot) with titles
p=sns.countplot(x="sex",data=kashti, hue="class")
p.set_title("obaid ka count plot for kashti")
plt.show()