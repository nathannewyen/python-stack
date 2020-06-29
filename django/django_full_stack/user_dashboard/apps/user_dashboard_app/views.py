from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin, User, Message, Comment
import bcrypt

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signin(request):
    return render(request, 'signin.html')


def reg_admin(request):
    return render(request, 'admin_reg.html')


def reg_admin_process(request):
    errors = Admin.objects.register_admin_validators(request.POST)

    # Check Valid Registration
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/register/admin/")
    # Register Successfully
    else:
        hashed_pw = bcrypt.hashpw(
            request.POST["reg_password_admin"].encode(), bcrypt.gensalt()).decode()
        newAdmin = Admin.objects.create(
            email=request.POST["reg_email_admin"],
            first_name=request.POST["first_name_admin"],
            last_name=request.POST["last_name_admin"],
            password=hashed_pw
        )
        request.session["admin_id"] = newAdmin.id
    return redirect('/dashboard/admin/')


def signin_user_process(request):
    errors = User.objects.login_users_valid(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")
    else:
        user = User.objects.filter(email=request.POST["login_email_user"],)
        logged_user = user[0]
        request.session["user_id"] = logged_user.id
    return redirect("/dashboard/")


def signin_admin(request):
    return render(request, 'signin_admin.html')


def signin_admin_process(request):
    errors = Admin.objects.login_admin_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")
    else:
        admin = Admin.objects.filter(email=request.POST["login_email_admin"],)
        logged_admin = admin[0]
        request.session["admin_id"] = logged_admin.id
    return redirect("/dashboard/admin/")


def register(request):
    return render(request, 'register.html')


def regval(request):
    emaillist = User.objects.filter(email=request.POST['reg_email'])
    if len(emaillist) > 0:
        found = True
    else:
        found = False

    context = {
        'found': found,
    }
    return render(request, 'regpartials.html', context)


def register_process(request):
    errors = User.objects.create_user_validators(request.POST)

    # Check Valid Registration
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/register/")
    # Register Successfully
    else:
        hashed_pw = bcrypt.hashpw(
            request.POST["reg_password"].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            email=request.POST["reg_email"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            password=hashed_pw
        )
        request.session["user_id"] = user.id

    return redirect('/dashboard/')


def dashboard_admin(request):
    if 'admin_id' not in request.session:
        return redirect("/")
    context = {
        'admin': request.session["admin_id"],
        'all_admins': Admin.objects.all(),
        'all_users': User.objects.all(),
    }
    return render(request, 'dashboard_admin.html', context)


def new_user(request):
    return render(request, 'add_user.html')


def new_user_process(request):
    errors = User.objects.add_user_validator(request.POST)

    # Check Valid Create
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/users/new/")
    # Register Successfully
    else:
        hashed_pw_user = bcrypt.hashpw(
            request.POST["reg_password_user"].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        email=request.POST["reg_email_user"],
        first_name=request.POST["first_name_user"],
        last_name=request.POST["last_name_user"],
        password=hashed_pw_user
    )
    return redirect("/dashboard/")


def dashboard(request):
    context = {
        'this_user': request.session["user_id"],
        'all_users': User.objects.all(),
    }
    return render(request, "dashboard.html", context)


def remove(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/dashboard/admin/")


def user(request, id):
    message_data = Message.objects.all()
    user = User.objects.get(id=id)
    user_id = request.session["user_id"]

    for message in message_data:
        print(message.user_message.id, user.id)

    context = {
        'user': User.objects.get(id=id),
        'user_id': request.session["user_id"],
        'message_data': Message.objects.all(),
        'comment_data': Comment.objects.all(),
    }

    return render(request, "user.html", context)


def edit_user(request, id):
    context = {
        'user': User.objects.get(id=id),
    }
    return render(request, "edit_user.html", context)


def edit_user_process(request, id):
    user = User.objects.get(id=id)
    user.email = request.POST['user_edit_email']
    user.first_name = request.POST['user_edit_first_name']
    user.last_name = request.POST['user_edit_last_name']
    user.save()
    return redirect(f"/user/{user.id}/")


def edit_password_process(request, id):
    user = User.objects.get(id=id)
    errors = User.objects.users_update_valid(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect(f"/users/edit/{user.id}/")
    else:
        hashed_pw = bcrypt.hashpw(
            request.POST["user_update_password"].encode(), bcrypt.gensalt()).decode()
        user.password = hashed_pw
        user.save()
        return redirect(f"/user/{user.id}")


def description_process(request, id):
    user = User.objects.get(id=id)
    user.description = request.POST['user_edit_description']
    user.save()
    return redirect(f"/user/{user.id}/")


def post_message(request, id):
    user_post_message = User.objects.get(id=request.session["user_id"])
    user_get_message = User.objects.get(id=id)

    Message.objects.create(
        user_message=user_post_message, message=request.POST['post_message'])

    return redirect(f"/user/{user_get_message.id}/")


def post_comment(request, id):

    user = User.objects.get(id=request.session["user_id"])
    message = Message.objects.get(id=request.POST['message_id'])
    Comment.objects.create(message_id=message, user_comment=user,
                           comment=request.POST['post_comment'])

    return redirect(f"/user/{user.id}/")


def delete_message(request, user_id, message_id):
    delete_message = Message.objects.get(id=message_id)
    delete_message.delete()
    return redirect(f"/user/{user_id}/")


def delete_comment(request, user_id, comment_id):
    delete_comment = Comment.objects.get(id=comment_id)
    delete_comment.delete()
    return redirect(f"/user/{user_id}/")


def signout(request):
    request.session.clear()
    return redirect("/")
