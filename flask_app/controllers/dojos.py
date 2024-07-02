from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, redirect, request


@app.route("/")
@app.route("/dojos")
def dojos():
    """This route displays all dojos"""
    dojos = Dojo.retrieve_info()
    return render_template("dojos.html", dojos=dojos)


@app.get("/dojos/new")
def new_dojo():
    """This route displays new dojo"""
    return render_template("new_dojos.html")


@app.get("/dojos/<int:dojo_id>")
def dojo_details(dojo_id):
    """This route displays a dojos info"""

    dojo = Dojo.retrieve_by_id_with_ninjas(dojo_id)
    if dojo == None:
        return "No dojo information found"
    return render_template("dojo_details.html", dojo=dojo)


@app.post("/dojos/create")
def create_dojo():
    """The route that processes the form"""

    print(request.form)
    dojo_id = Dojo.create(request.form)
    print("New Dojo:" + str(dojo_id))
    return redirect("/dojos")


@app.get("/dojos/<int:dojo_id>/edit")
def edit_dojo(dojo_id):
    """This route displays edit form"""

    dojo = Dojo.retrieve_info_id(dojo_id)
    if dojo == None:
        return "No dojo information found"
    return render_template("edit_dojo.html", dojo=dojo)


@app.post("/dojos/update")
def update_dojo():
    """This route processes the Edit form"""

    dojo_id = request.form["dojo_id"]
    Dojo.update(request.form)
    return redirect(f"/dojos/{dojo_id}")


@app.post("/dojos/<int:dojo_id>/delete")
def delete_dojo(dojo_id):
    """Deletes a dojo"""

    Dojo.delete_by_id(dojo_id)
    return redirect("/dojos/")
