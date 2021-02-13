from django import forms

class PostForm(forms.Form):
    posttitle = forms.CharField(max_length = 30,
    widget = forms.TextInput(attrs = {
    'class': 'form-control',
    'placeholder' : 'Your Post Title',
    'id' : 'inputTitle',
    }))

    postdesc = forms.CharField(widget = forms.Textarea({
    'class' : 'form-control',
    'rows' : '5',
    'id' : 'text',
    'placeholder' : 'Write something new...',
    }))
