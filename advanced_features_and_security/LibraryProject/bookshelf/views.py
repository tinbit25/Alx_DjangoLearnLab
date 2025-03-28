# views.py

from django.shortcuts import render
from .forms import ExampleForm  # Importing ExampleForm from forms.py

# Your view function
def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # You can now use these values, e.g., send an email or save to the database
    else:
        form = ExampleForm()

    return render(request, 'example_template.html', {'form': form})
