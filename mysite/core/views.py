from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm #, Us
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404

from .models import Profile, Consultation
from .forms import UserForm, ConsultForm, UploadFileForm
from .utils import handle_uploaded_file

# Multiupload
from django.views.generic.edit import FormView
from .forms import UploadForm
from .models import Attachment

# user edit
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.utils import timezone


# Pages that require the user to be logged in:
@login_required
def edit_user(request, pk):
    user = User.objects.get(pk = pk)
    user_form = UserForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, Profile,
        fields=("username", "website", "bio", "photo"))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, 
                    instance=created_user)

                if formset.is_valid():
                    # print "request.FILES.keys(): " + "; ".join(request.FILES.keys())
                    handle_uploaded_file(request.FILES['file'], fname="a_file.jpg")
                    created_user.save()
                    formset.save()
                    redir_target = request.path.replace("edit/", "")
                    return HttpResponseRedirect(redir_target)

        return render(request, "account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        return PermissionDenied

@login_required
def consult_new(request):
    if request.method == 'POST':
        form = ConsultForm(request.POST)
        if form.is_valid():
            cons = form.save(commit=False)
            cons.owner = request.user
            cons.date_created = timezone.now()
            cons.date_modified = timezone.now()
            cons.save()
            return redirect('consult_detail', pk=cons.pk)
        else:
            return render(request, "consult_edit.html", {'error': "INVALID"})
    else:
        form = ConsultForm()
    return render(request, 'consult_edit.html', {'form': form})

@login_required
def consult_edit(request, pk):
    cons = get_object_or_404(Consultation, pk=pk)
    title = cons.title
    if request.method == 'POST':
        form = ConsultForm(request.POST, instance=cons)
        print(form.errors)
        if form.is_valid():
            cons = form.save(commit=False)
            cons.owner = request.user
            cons.date_modified = timezone.now()
            cons.save()
            return redirect('consult_detail', pk=cons.pk)
        else:
            return redirect('consult_detail', pk=cons.pk)
    else:
        form = ConsultForm(instance=cons)
    return render(request, 'consult_edit_tab.html', {'form': form, 'title': title})

###################################
# Pages that do not require login:
###################################
def consults(request):
    cons = Consultation.objects.all()
    return render(request, 'consults.html', {"cons": cons})

def consult_detail(request, pk):
    consult = get_object_or_404(Consultation, pk=pk)
    return render(request, "consult_detail.html", {"consult": consult})

def species(request):
    return render(request, 'species.html')

def places(request):
    return render(request, 'places.html')

def people(request):
    peeps = Profile.objects.all()
    return render(request, 'people.html', {"peeps": peeps})

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def user_profile(request, pk):
    user_id = str(request).split("/")[2]
    prof = Profile.objects.get(user_id = user_id)
    user = User.objects.get(pk = pk)
    if(str(request.user.id) == user_id):
        edit = "inline"
    else:
        edit = "none"   # hide the edit option if no login
    results = {
        'username': str(prof.username),
        'website': str(prof.website),
        'bio': str(prof.bio),
        'edit': edit
    }
    return render(request, 'profile.html', results)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
