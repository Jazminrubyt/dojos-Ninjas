from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask import render_template, redirect, request


@app.route("/ninjas/all")
def ninjas():
    """This route displays all ninjas"""
    ninjas = Ninja.retrieve_info()
    return render_template("ninjas.html", ninjas=ninjas)


@app.get("/ninjas")
def new_ninja():
    """This route displays new ninja"""

    dojos = Dojo.retrieve_info()
    for dojo in dojos:
        print("*************")
        print(dojo.name)

    return render_template("ninjas.html", dojos=dojos)


@app.get("/ninjas/<int:ninja_id>")
def ninja_details(ninja_id):
    """This route displays a ninjas info"""

    ninja = Ninja.retrieve_info_id(ninja_id)
    if ninja == None:
        return "No ninja information found"
    return render_template("ninjas.html", ninja=ninja)


@app.post("/ninjas/create")
def create_ninja():
    """The route that processes the form"""

    print(request.form)
    ninja_id = Ninja.create(request.form)
    print("New Ninja:" + str(ninja_id))
    dojo_id = request.form["dojo_id"]
    return redirect(f"/dojos/{dojo_id}")


@app.get("/ninjas/<int:ninja_id>/edit")
def edit_ninja(ninja_id):
    """This route displays edit form"""

    ninja = Ninja.retrieve_info_id(ninja_id)
    if ninja == None:
        return "No ninja information found"
    return render_template("edit_ninja.html", ninja=ninja)


@app.post("/ninjas/update")
def update_ninja():
    """This route processes the Edit form"""

    ninja_id = request.form["ninja_id"]
    Ninja.update(request.form)
    return redirect(f"/ninjas/{ninja_id}")


@app.post("/ninjas/<int:ninja_id>/delete")
def delete_ninja(ninja_id):
    """Deletes a ninja"""

    Ninja.delete_by_id(ninja_id)
    return redirect("/ninjas/")
