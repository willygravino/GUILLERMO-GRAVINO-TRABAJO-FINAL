from django.shortcuts import render
from AdminVideos.models import Video
# from AdminVideos.forms import VideoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView #, DetailView,  
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q


def index(request):
    return render(request, "AdminVideos/index.html")


class VideoList(ListView):
    model = Video
    context_object_name = "videos"

    def get_queryset(self):
        query = "" # aquí irá el nombre del usuario logueado
        object_list = Video.objects.filter(quienes_aparecen__icontains=query)
        return object_list 
   
   
    #def get_queryset(self):
    #    query = self.request.GET.get('q')
    #    object_list = Movie.objects.filter(Q(title__icontains=query)|Q(genre__icontains=query))
    #    return object_list
    

class VideoMineList(LoginRequiredMixin, VideoList):
    
    def get_queryset(self):
        return Video.objects.filter(publisher=self.request.user.id).all()


#class VideoDetail(DetailView):
#    model = Video
#    context_object_name = "video"


class VideoUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    success_url = reverse_lazy("videos-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        video_id =  self.kwargs.get("pk")
        return Video.objects.filter(propietario=user_id, id=video_id).exists()


class VideoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    context_object_name = "video"
    success_url = reverse_lazy("videos-list")

    def test_func(self):
        user_id = self.request.user.id
        video_id =  self.kwargs.get("pk")
        return Video.objects.filter(propietario=user_id, id=video_id).exists()


class VideoCreate(LoginRequiredMixin, CreateView):
    model = Video
    success_url = reverse_lazy("videos-list")
    fields = '__all__'


#class VideoSearch(ListView):
#    model = Video
#    context_object_name = "videos"

 #   def get_queryset(self):
 #       criterio = self.request.GET.get("criterio")
 #       result = Video.objects.filter(carousel_caption_title__icontains=criterio).all()
 #       return result

class Login(LoginView):
    next_page = reverse_lazy("index")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html' 
    success_url = reverse_lazy('videos-list')


class Logout(LogoutView):
    template_name = "registration/logout.html"


#class ProfileCreate(LoginRequiredMixin, CreateView):
#    model = Profile
#    success_url = reverse_lazy("videos-list")
#    fields = ['avatar',]

#    def form_valid(self, form):
#        form.instance.user = self.request.user
#        return super().form_valid(form)

#class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
#    model = Profile
#    success_url = reverse_lazy("videos-list")
#    fields = ['avatar',]
#
#    def test_func(self):
#        return Profile.objects.filter(user=self.request.user).exists()


#class MensajeCreate(CreateView):
#    model = Mensaje
#    success_url = reverse_lazy('mensaje-create')
#    fields = '__all__'


#class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#    model = Mensaje
#    context_object_name = "mensaje"
#    success_url = reverse_lazy("mensaje-list")

#    def test_func(self):
#        return Mensaje.objects.filter(destinatario=self.request.user).exists()
    

#class MensajeList(LoginRequiredMixin, ListView):
#    model = Mensaje
#    context_object_name = "mensajes"

#    def get_queryset(self):
#        import pdb; pdb.set_trace
#        return Mensaje.objects.filter(destinatario=self.request.user).all()
    

# Create your views here.
