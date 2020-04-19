from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import NameForm


#
# @login_required
# def get_name(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             return HttpResponse('thanks..the input is valid')
#     else:
#         form = NameForm()
#
#     return render(request, 'name.html', {'form': form})

@login_required
def get_name(request):
    import pprint
    pprint.pprint(request.user)
    return HttpResponse(
        "<h2>Its Working User</h2>" + str(request.user) + "<h2>  This view is accessed by allauth..!!</h2>")
