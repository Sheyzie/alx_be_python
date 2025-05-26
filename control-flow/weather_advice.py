# This script will ask the user about the current weather conditions and provide clothing recommendations based on the input.

# get user input for weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ")

if weather == 'sunny':
    print('Wear a t-shirt and sunglasses.')
elif weather == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
elif weather == 'cold':
    print('Make sure to wear a warm coat and a scarf.')
else:
    print("Sorry, I don't have recommendations for this weather.")
