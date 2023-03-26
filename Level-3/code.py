import os
from flask import Flask, request  

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set        
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            pass
        
        # builds path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prof_picture_path = os.path.normpath(os.path.join(base_dir, path))
        # defends against path traversal attacks
        if base_dir != os.path.commonpath([base_dir, prof_picture_path]):
            return base_dir
    
        with open(prof_picture_path, 'rb') as pic:
            picture = bytearray(pic.read())

        # assume that image is returned on screen after this
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        tax_data = None
        
        if not path:
            raise Exception("Error: Tax form is required for all users")
       
        base_dir = os.path.dirname(os.path.abspath(__file__))
        form_path = os.path.abspath(os.path.normpath(path))
        # defends against path traversal attacks
        if base_dir != os.path.commonpath([base_dir, form_path]):
            return base_dir

        with open(form_path, 'rb') as form:
            tax_data = bytearray(form.read())

        # assume that taxa data is returned on screen after this
        return form_path