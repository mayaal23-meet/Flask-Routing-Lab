from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

product=['pictures','signatures','videos from maya']
# Your code should be below
@app.route('/')
def home():
	sales = ['1 pic for 7$','3 pics for 15$', '15 precent discount for subscribers']
	return render_template('home.html', sales=sales)

@app.route('/product')
def products():
	return render_template('product.html')

# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
