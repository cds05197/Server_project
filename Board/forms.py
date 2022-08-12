from django import forms
from .models import Board
from django.utils.safestring import mark_safe

class BoardCreateForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    print(self)
    self.fields['title'].widget.attrs.update({'class' : 'form-control'})
    self.fields['file_upload'].widget.attrs.update({'class' : 'form-control'})
    self.fields['content'].widget.attrs.update({'class' : 'form-control', 'rows' : '20'})
    
    
  class Meta:
    model = Board
    fields = ('title', 'file_upload', 'content')
    
class CustomFileWidget(forms.FileInput):
  def __init__(self, attrs={}):
      super().__init__(attrs)

  def render(self, name, value, attrs=None, renderer=None):
    output = []
    print(value)
    if value and hasattr(value, "url"): # 첨부파일이 존재한다
      file_name = value.url.split('/')[-1] # /단위로 자르고 리스트 마지막 원소 -> 파일명
      output.append(super().render(name, value, attrs))
      # 현재 FileInput class에 render함수 재정의해서 사용중
      # 기본적으로 FileInput에서 생성되는 HTML 태그를 추가한다.
      output.append(f'<span class="form-control">첨부파일 : <a class="text-reset text-decoration-none" target="_blank" href="{value.url}">{file_name}</a><input class="form-check-input ms-2 me-1" type="checkbox" name="upload_clear" id="upload_clear_id" value="upload_del">Delete</span>')
      # 이후 사용자가 커스텀으로 사용할 태그 추가
      # checkbox 체크 시 수정작업에서 첨부파일 삭제
      return mark_safe(u''.join(output))
      # mark_safe 기존 태그 + 커스텀 태그가 output에 정의되어 있는데
      # 이를 join으로 한 줄로 만들고, 일반 문자열 방식으로 리턴해주는
      # 기능을 담당한다. 
    output.append(super().render(name, value, attrs))
    # url 없을 시 기본 태그만 가지고 리턴해줌
    return mark_safe(u''.join(output))

class BoardUpdateForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update({'class': 'form-control'})
    self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
    self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})
  
  class Meta:
    model = Board
    fields = ('title', 'file_upload', 'content')
    widgets = {
      'file_upload': CustomFileWidget,
    }