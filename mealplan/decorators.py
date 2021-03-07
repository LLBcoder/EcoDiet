from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated :
            return redirect('/')
        else :
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated :
            return view_func(request, *args, **kwargs)
        else :
            return redirect('/demo')
    
    return wrapper_func