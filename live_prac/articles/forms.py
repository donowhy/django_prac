from django import forms 
from .models import Article
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30) 
#     #model 에서 CharField는 내부 파라미터가 필수지만 forms는 필수가 아님! 여기서 안쓰면 쭈르륵 다 쓸 수 있음.
#     #model은 db와 연관이 되어 있으니까
#     content = forms.CharField(widget=forms.Textarea) #CharField는 폼에서!   #TextField

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__' # 타이틀만 필요하면 'title'로 가능
        #exclud도 가능

    #Trun False로 반환하기
    #clean_ 까지는 정해진 구조
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'django' in title: #django라는 키워드가 title에 있으면~
    #         return True
    #     return False