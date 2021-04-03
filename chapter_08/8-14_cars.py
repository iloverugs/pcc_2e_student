# Write a function that stores info about car in a dictionary
# Function recieve manufacturer and a model name
# Function should then receive arbitrary number of keyword arguments (car_info).
def car_information(manufacturer_info, model_info, **car_info):
    """Function prints dictionary of car information."""
    car_info['manufacturer'] = manufacturer_info
    car_info['model'] = model_info
    return car_info

# Call function with required info and two other name-value pairs
automobile_info = car_information('ford', 'explorer',
                                color='red', tow_package=True)
# Print the dictionary
print(automobile_info)