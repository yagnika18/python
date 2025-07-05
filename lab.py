import pandas as pd

# Define the data as a dictionary
data = {
    'name': ['Vikram','Aditya','Charli','Shreya','Meghana','Rohit','Uma','Keerthi','Mahesh','Ram'],
    'age': [21,22,20,22,21,20,12,21,20,20],
    'id': [1,2,3,4,5,6,7,8,9,10],
    'phone_number': ['8247680608','9885845553','7093930861','9618305365','08717261923','8976123489','67891244578','81718218213'],
    'overall_marks': [85.5,92,78,64.8,72,88,94,98,79.5,90]
}# Create the DataFrame
df = pd.DataFrame(data)
# Print the DataFrame
print(df)
