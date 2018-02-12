from flask import Flask, render_template, request
app= Flask(__name_)
app.config['DEBUG'} = TRUE

@app.route('/post_form', methods=['GET','POST'])
def post_form():
	if request.method == 'POST':
		name= request.form['name']
		email= request.form['email']
		mobile= request.form['mobile']
		message= request.form['message']
	return 'Message Submitted!'; 
		
if__name__=="__main__":
app.run()