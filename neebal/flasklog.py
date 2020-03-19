from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from forms2 import FileForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/file", methods=['GET', 'POST'])
def file():
    form = FileForm()
    if form.validate_on_submit():
        startline = int(form.startline.data)
        endline = int(form.endline.data)
        flash(f'Account created for {form.filename.data}!', 'success')     
        with open(os.path.join(os.getcwd(),form.filename.data), "r", encoding="utf8", errors='ignore',) as f:
            content = f.readlines()
            # content1 = f.read()
            outContent = []
            if (startline==-1) and (endline == -1):
                for line in content:
                    outContent.append(line) 
            elif (startline==-1) and (endline != -1):
                for line in content[:endline+1]:
                    outContent.append(line)
            elif (startline!=-1) and (endline == -1):
                for line in content[startline:]:
                    outContent.append(line)
            else:
                for line in content[startline:endline+1]:
                    outContent.append(line)

        return render_template('file.html', text=outContent, form=form)
    return render_template('file.html', title='file', form=form)

@app.route("/<filename>/")
@app.route("/<filename>/<int:startline>/")
@app.route("/<filename>/<int:startline>/<int:endline>")
def filename1(filename, startline = -1, endline = -1):
    # startline = int(startline)
    # endline = int(endline)
    with open(os.path.join(os.getcwd(),filename), "r", encoding="utf8", errors='ignore',) as f:
        content = f.readlines()
        # content1 = f.read()
        outContent = []
        if (startline==-1) and (endline == -1):
            for line in content:
                outContent.append(line) 
        elif (startline==-1) and (endline != -1):
            for line in content[:endline+1]:
                outContent.append(line)
        elif (startline!=-1) and (endline == -1):
            for line in content[startline:]:
                outContent.append(line)
        else:
            for line in content[startline:endline+1]:
                outContent.append(line)
   
    return render_template('filename.html', text=outContent)


if __name__ == '__main__':
    app.run(debug=True)
