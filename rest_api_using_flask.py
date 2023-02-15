from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/prime/<int:num>')
def prime(num):
    
    if num > 1:
     
        for i in range(2,num):
             if (num % i) == 0:
                result={
                    
                    
                    "number":num,
                    
                    "prime":False
                }
                break
        else:
            result={
                    
                    
                    "number":num,
                    
                    "prime":True
                }
       

    else:
         result={
                    
                    
                    "number":num,
                    
                    "prime":False
                }
    return jsonify(result)


@app.route('/func')
def func():
    
    return "its function1"
    





    



if __name__ == '__main__':
    app.run(debug=True)
    