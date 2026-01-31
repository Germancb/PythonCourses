# Import Libraries
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

# Actual preferences for 10 movies
actual = ['Like', 'Like', 'Dislike', 'Like', 'Dislike', 'Like', 'Dislike', 'Dislike', 'Like', 'Dislike']

# Model's predictions for those 10 movies
predictions = ['Like', 'Like', 'Like', 'Dislike', 'Dislike', 'Like', 'Dislike', 'Like', 'Like', 'Dislike']

# Create a confusion matrix using sklearn
conf_matrix = metrics.confusion_matrix(actual, predictions, labels=['Like', 'Dislike'])

# The 'labels' parameter in confusion_matrix function is used to specify the order of classes. 
# Here, 'Like' is considered as the positive class and 'Dislike' as the negative class.

# Plot the confusion matrix using seaborn
plt.figure(figsize=(6, 6))
sns.heatmap(conf_matrix, annot=True, fmt='g', cmap='PiYG', xticklabels=['Like', 'Dislike'], yticklabels=['Like', 'Dislike'])
plt.xlabel('Predicted Preference', fontsize=12)
plt.ylabel('Actual Preference', fontsize=12)
plt.show()