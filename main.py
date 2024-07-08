# Import matplotlib library here
import matplotlib.pyplot as plt

# Let's rank some of our favorite snacks
snack_scores = [40, 30, 30]

slice_labels = ["fries", "chips", "sour candy"]

# Let's make a pie chart!
plt.pie(snack_scores, labels=slice_labels)

# Give your pie chart a title in the quotes
plt.title("Tauri's Munchies")

# Put the name of your file in the quotes and give it a .png extension
plt.savefig("")

