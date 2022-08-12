from django.shortcuts import get_object_or_404, render, redirect
from Board.models import Board
from Board.forms import BoardCreateForm,BoardUpdateForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from django.contrib.auth.decorators import login_required
from config import settings
import os 
from django.core.exceptions import PermissionDenied

# Create your views here.
class BoardList(ListView):
    model = Board
    template_name = 'Board/Board/board_list.html'
    ordering = '-pk'
    paginate_by = 10

class BoardDetail(DetailView):
    model = Board
    template_name = 'Board/Board/board_detail.html'
    
    def dispatch(self, request,*args,**kwargs) :
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
    # args, kwargs 는 함수 오버라이딩 유연성을 위해서 선언된 것
    # url 패턴 요청시 로그인 여부 확인을 한다
    # 로그인 여부 부정합시 raise 명령어를 통해 permissionError 반환
    
class BoardCreate(CreateView):
    model = Board
    form_class = BoardCreateForm
    template_name = 'Board/Board/board_form.html'
    
    def form_valid(self, form): #이미 CreateView에 정의된 거 오버라이딩
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super().form_valid(form)
        else:
            return redirect('/Board')    
        # 어떤 사용자가 로그인 후 게시글작성을 하고 Submit 버튼을누르면
        # 그 내용이 Self.request가 된다. 이 request안에 사용자 정보가 있기에
        # 사용자정보를 current_user에 저장한다. 이후 사용자 정합성 검증 실시
        # URL 조작으로 해당 클래스 접근시 로그인 인증 상태를 체크하여 방지한다.
        # 이후 변경된 form으로 superclass에 form_valid 함수실행
        # 원래 모든 정합성 검사는 super에 form_valid가 수행해준다.
        
# login_required 데코레이션 패턴을 이용하여, 로그인 상태에서만 해당
# 함수가 실행되도록 정의한다. ( 메타정보를 하위 함수에 적용 )
# 로그인이 되어있지 않은 사용자가 해당 함수를 사용하려고 시도 할 
# 경우 로그인 페이지로 이동시키는 역할을 수행한다.        
@login_required(login_url='common:login')
def BoardDelete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.user != board.author:
        return redirect('Board:detail', pk=pk)
    if board.file_upload:
        file_upload_path = os.path.join(settings.MEDIA_ROOT, board.file_upload.path)
        if os.path.exists(file_upload_path):
            os.remove(file_upload_path)
    board.delete()
    return redirect('Board:list')

class BoardUpdate(UpdateView):
    model = Board
    form_class = BoardUpdateForm
    template_name = 'Board/Board/board_form_update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
      if self.get_object().file_upload.name != '':
        if self.object.file_upload != self.get_object().file_upload.name:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
        if 'upload_clear' in self.request.POST:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
              self.object.file_upload = ''
      return super().form_valid(form)
