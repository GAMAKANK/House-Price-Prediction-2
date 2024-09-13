from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)  # Boilerplate code to start Flask

# Reading data
data = pd.read_csv("final_dataset.csv")

# Loading model
pipe = pickle.load(open("linear_model.pkl","rb"))

# Creating route for index to load
@app.route('/')
def index():
    # Fetching data from the main file
    squareMeters = sorted(data['squareMeters'].unique())
    numberOfRooms = sorted(data['numberOfRooms'].unique())
    hasYard = sorted(data['hasYard'].unique())
    hasPool = sorted(data['hasPool'].unique())
    floors = sorted(data['floors'].unique())
    cityPartRange = sorted(data['cityPartRange'].unique())
    made = sorted(data['made'].unique())
    isNewBuilt = sorted(data['isNewBuilt'].unique())
    hasStormProtector = sorted(data['hasStormProtector'].unique())
    basement = sorted(data['basement'].unique())
    attic = sorted(data['attic'].unique())
    garage = sorted(data['garage'].unique())
    hasGuestRoom = sorted(data['hasGuestRoom'].unique())
    

    return render_template(
        'index.html',
        squareMeters=squareMeters,
        numberOfRooms=numberOfRooms,
        hasYard=hasYard,
        hasPool=hasPool,
        floors=floors,
        cityPartRange=cityPartRange,
        made=made,
        isNewBuilt=isNewBuilt,
        hasStormProtector=hasStormProtector,
        basement=basement,
        attic=attic,
        garage=garage,
        hasGuestRoom=hasGuestRoom,
        
    )

# Creating app button to predict 
@app.route('/predict', methods=['POST'])
def predict():
    # Fetching data from form
    squareMeters = int(request.form.get('squareMeters'))
    numberOfRooms = int(request.form.get('numberOfRooms'))
    hasYard = int(request.form.get('hasYard'))
    hasPool = int(request.form.get('hasPool'))
    floors = int(request.form.get('floors'))
    cityPartRange = int(request.form.get('cityPartRange'))
    made = int(request.form.get('made'))
    isNewBuilt = int(request.form.get('isNewBuilt'))
    hasStormProtector = int(request.form.get('hasStormProtector'))
    basement = int(request.form.get('basement'))
    attic = int(request.form.get('attic'))
    garage = int(request.form.get('garage'))
    hasGuestRoom = int(request.form.get('hasGuestRoom'))

    # Create a dataframe with the input data
    input_data = pd.DataFrame(
        [[squareMeters, numberOfRooms, hasYard, hasPool, floors, cityPartRange, made, isNewBuilt, hasStormProtector, basement, attic, garage, hasGuestRoom]],
        columns=['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors', 'cityPartRange', 'made', 'isNewBuilt', 'hasStormProtector', 'basement', 'attic', 'garage', 'hasGuestRoom']
    )

    # Printing the input data
    print("Input Data:")
    print(input_data)

    # Handle unknown categories in the input data - like if a categorical feature is not recognized, fill it with a default value
    for column in input_data.columns:
        unknown_categories = set(input_data[column]) - set(data[column].unique())
        if unknown_categories:
            # Handle unknown categories (e.g., replace with a default value)
            input_data[column] = input_data[column].replace(unknown_categories, data[column].mode()[0])

    print("Processed Input Data:")
    print(input_data)

    # Predict the price
    prediction = pipe.predict(input_data)[0]

    return str(prediction)

# Ending Flask app and mentioning the port where to run
if __name__ == '__main__':
    app.run(debug=True, port=5000)



# from flask import Flask , render_template, request, jsonify  "jsonify":Unknown word.
# import pandas as pd
# import pickle

# app = Flask(__name__) #boiler code to start flask
# #reading data
# data=pd.read_csv("final_dataset.csv")
# #loading model
# with open('linear_model.pkl', 'rb') as pipe:
#     model = pickle.load(pipe)


# ## creating route for index to load
# @app.route('/')
# def index():
#     #fetchinf data from main file
#     squareMeters = sorted(data['squareMeters'].unique())
#     numberOfRooms = sorted(data['numberOfRooms'].unique())
#     hasYard = sorted(data['hasYard'].unique())
#     hasPool = sorted(data['hasPool'].unique())
#     floors = sorted(data['floors'].unique())
#     cityPartRange = sorted(data['cityPartRange'].unique())
#     made = sorted(data['made'].unique())
#     isNewBuilt = sorted(data['isNewBuilt'].unique())
#     hasStormProtector = sorted(data['hasStormProtector'].unique())
#     basement = sorted(data['basement'].unique())
#     attic = sorted(data['attic'].unique())
#     garage = sorted(data['garage'].unique())
#     hasGuestRoom = sorted(data['hasGuestRoom'].unique())
#     price = sorted(data['price'].unique())
#     return render_template('index.html',squareMeters=squareMeters,numberOfRooms=numberOfRooms,hasYard=hasYard,hasPool=hasPool,floors=floors,cityPartRange=cityPartRange,made=made,isNewBuilt=isNewBuilt,hasStormProtector=hasStormProtector,basement=basement,attic=attic,garage=garage,hasGuestRoom=hasGuestRoom,price=price)
                           
                          
# #creating app button to predict 
# @app.route('/predict',methods=['POST'])
# def predict():
#     #fetching data from form
#     #first we have to request it from the csv file for droopdown then have to request from the form
#     squareMeters = int(request.form.get('squareMeters'))
#     numberOfRooms = int(request.form.get('numberOfRooms'))
#     hasYard = int(request.form.get('hasYard'))
#     hasPool = int(request.form.get('hasPool'))
#     floors = int(request.form.get('floors'))
#     cityPartRange = int(request.form.get('cityPartRange'))
#     made = int(request.form.get('made'))
#     isNewBuilt = int(request.form.get('isNewBuilt'))
#     hasStormProtector = int(request.form.get('hasStormProtector'))
#     basement = int(request.form.get('basement'))
#     attic = int(request.form.get('attic'))
#     garage = int(request.form.get('garage'))
#     hasGuestRoom = int(request.form.get('hasGuestRoom'))
   
   
#    #create a dataframe with the input data
#     input_data = pd.DataFrame([[squareMeters,numberOfRooms,hasYard,hasPool,floors,cityPartRange,made,isNewBuilt,hasStormProtector,basement,attic,garage,hasGuestRoom]],
#                              columns=['squareMeters','numberOfRooms','hasYard',
#                                       'hasPool','floors','cityPartRange','made','isNewBuilt',
#                                       'hasStormProtector','basement','attic','garage','hasGuestRoom'])#fetching from main file

#     #printing the input data
#     print("Input Data:")
#     print(input_data)


#     # -------------------------see again-------------------------
#     #handle unknown catogories in the input data - like if a catogoral feature is null,we have to fill it with default
#     for column in input_data.columns:
#         unknown_categories = set(input_data[column])-set(data[column].unique())
#         if unknown_categories  :
#             #handle unknown categories (e.g. replace with a default value)
#             input_data[column] = input_data[column].replace(unknown_categories,data[column].mode()[0])

#     print("Processsed Input Data:")
#     print(input_data)
#     # ------------------------till here for unknown categories--------------------------


#     #predict the price
#     prediction = pipe.predict(input_data)[0]


#     return str(prediction)


# #ending flask app and mentioning the port where to run
# if __name__ == '__main__':
#     app.run(debug=True,port=5000)
