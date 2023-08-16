from flask_app import app
from flask_app.models import user, recipe
from flask import redirect, render_template, request, session, flash

@app.route('/recipes')
def display_recipes():
    if 'user_id' not in session.keys():
        return redirect('/')
    current_user = user.User.get_user_with_recipes(session['user_id'])
    print('test')
    print(current_user.recipe_list)
    users = user.User.get_all()
    rel_users = []
    for guy in users:
        guy_with_r = user.User.get_user_with_recipes(guy.id)
        print(len(guy_with_r.recipe_list))
        if len(guy_with_r.recipe_list) > 0:
            rel_users.append(guy_with_r)
            print(guy_with_r.first_name)
    print(rel_users)
    
    return render_template('recipes.html', user=current_user, rel_users=rel_users)

@app.route('/recipes/<int:recipe_id>')
def show_recipe(recipe_id):
    this_recipe = recipe.Recipe.get_by_id(recipe_id)
    recipe_creator = user.User.get_by_id(this_recipe.creator_id)
    current_user = user.User.get_by_id(session['user_id'])
    return render_template('show_recipe.html', recipe=this_recipe, recipe_creator=recipe_creator, user=current_user)

@app.route('/recipes/add')
def add_r_page():
    if 'user_id' not in session.keys():
        return redirect('/')
    return render_template('add_recipe.html')

@app.post('/process/add')
def add_recipe():
    if not recipe.Recipe.validate_recipe(request.form):
        print(request.form)
        return redirect('/recipes/add')
    recipe.Recipe.create(request.form)
    return redirect('/recipes')

@app.route('/recipes/<int:recipe_id>/edit')
def show_edit_page(recipe_id):
    this_recipe = recipe.Recipe.get_by_id(recipe_id)
    if session['user_id'] != this_recipe.creator_id:
        session.clear()
        return redirect('/')
    
    return render_template('edit_recipe.html', recipe=this_recipe)

@app.post('/process/edit')
def edit_recipe():
    recipe_id = request.form['recipe_id']
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/{recipe_id}/edit')
    recipe.Recipe.update(request.form)
    return redirect('/recipes')

@app.post('/recipes/<int:recipe_id>/delete')
def delete_recipe(recipe_id):
    this_recipe = recipe.Recipe.get_by_id(recipe_id)
    if session['user_id'] != this_recipe.creator_id:
        session.clear()
        return redirect('/')
    recipe.Recipe.delete(recipe_id)
    return redirect('/recipes')
