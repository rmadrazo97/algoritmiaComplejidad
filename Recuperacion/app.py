from flask import Flask, render_template

#---read ordered File....
def read(file):
    fileR = open(file)
    #getting all lines in the file. 
    sentences1 = []
    for x in fileR:
        value = x
        #if last char = "\n" do not add it. 
        if (value[len(value)-1] == "\n"):
            value = value[0:len(value)-1]
            #sentences1.append(value)
        sentences1.append(value)
    #print(sentences1)
    print(sentences1)
    return sentences1

def order():
    print("ORDENANDO")


app = Flask(__name__)
@app.route('/')
def index():
    ordered = read("orderedFile.txt")
    return render_template('main.html',items = ordered)

if __name__ == '__main__':
    app.run(debug = True)
