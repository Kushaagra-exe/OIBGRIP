from flask import Flask, request, render_template


app = Flask(__name__)
app.static_folder = 'static'

@app.route('/', methods = ['POST', 'GET'])
def tempconvert():
    if request.method == 'POST':
        temp = int(request.form['num'])
        type = request.form['temp']
        temp_c = 0
        temp_f = 0
        temp_k = 0
        if type == 'F':
            temp_f = temp
            temp_c = (temp-32)/1.8
            temp_k = temp_c + 273.15
        elif type == 'C':
            temp_f = (temp*1.8)+32
            temp_c = temp
            temp_k = temp + 273.15
        else:
            temp_f = (temp_c*1.8)+32
            temp_c = temp - 273.15
            temp_k = temp

        return render_template('tempout.html', f=temp_f, c=temp_c, k=temp_k)
    
    else:
        return render_template('temperature.html')

        

            

if __name__ == '__main__':
    app.run(port=5000, debug=True)