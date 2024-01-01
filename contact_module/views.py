from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView

from product_module.models import Product
from site_module.models import SiteSetting
from .forms import ContactUsForm, ContactUsModelForm, ProfileForm
from .models import ContactUs, UserProfile


# Create your views here.

class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args ,**kwargs)
        setting : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context

# class ContactUsView(FormView):
#     template_name = 'contact_module/contact_us_page.html'
#     form_class = ContactUsModelForm
#     success_url = '/contact-us/'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class ContactUsView(View):
# def get(self, request):
#     contact_form = ContactUsModelForm()
#     return render(request, 'contact_module/contact_us_page.html', {
#         'contact_form': contact_form
#     })
#
# def post(self, request):
#     contact_form = ContactUsModelForm(request.POST)
#     if contact_form.is_valid():
#         contact_form.save()
#         return redirect('home_page')
#     return render(request, 'contact_module/contact_us_page.html', {
#         'contact_form': contact_form
#     })

# def contact_us_page(request):
#     if request.method == 'POST':
#         contact_form = ContactUsForm(request.POST)
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             # print(contact_form.cleaned_data)
#             # contact = ContactUs(
#             #     full_name=contact_form.cleaned_data.get('full_name'),
#             #     title=contact_form.cleaned_data.get('title'),
#             #     email=contact_form.cleaned_data.get('email'),
#             #     message=contact_form.cleaned_data.get('message')
#             # )
#             # contact.save()
#             contact_form.save()
#             return redirect('home_page')
#     else:
#         # contact_form = ContactUsForm()
#         contact_form = ContactUsModelForm()
#     return render(request, 'contact_module/contact_us_page.html', {
#         'contact_form': contact_form
#     })

class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'

    # def get(self, request):
    #     form = ProfileForm()
    #     return render(request, 'contact_module/create_profile_page.html', {
    #         'form': form
    #     })
    #
    # def post(self, request):
    #     submitted_file = ProfileForm(request.POST, request.FILES)
    #
    #     if submitted_file.is_valid():
    #         profile = UserProfile(image=request.FILES['user_image'])
    #         profile.save()
    #         return redirect('/contact-us/create-profile')
    #
    #     return render(request, 'contact_module/create_profile_page.html', {
    #         'form': submitted_file
    #     })


class ProfilesView(ListView):
    template_name = 'contact_module/profile_list_page.html'
    model = UserProfile
    context_object_name = 'profiles'



