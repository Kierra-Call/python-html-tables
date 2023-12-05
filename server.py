from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"





#THIS WILL MOVE LOCATIONS LATER -- (controller file)
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def list_loop():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    print(users)
    return render_template("index.html", users=users)  # Return the string 'Hello World!' as a response
#*******************************

#This is always at the bottom!
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
#*******************************