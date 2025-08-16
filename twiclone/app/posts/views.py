from django import forms
from django.shortcuts import redirect, render
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']
        widgets = {'text': forms.Textarea(attrs={'rows':3, 'placeholder':'Що у вас нового?'})}

def timeline(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('timeline')
    return render(request, 'posts/timeline.html', {'form': form, 'posts': Post.objects.all()})
