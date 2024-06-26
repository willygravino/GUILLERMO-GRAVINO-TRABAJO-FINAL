from django.shortcuts import render, redirect
from AdminVideos.models import Video, Profile, Mensaje
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



def index(request):
    return render(request, "AdminVideos/index.html")
   
def about(request):
    return render(request, "AdminVideos/about.html")

class VideoList(ListView):
    model = Video
    context_object_name = "videos"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            try:
                if self.request.user.profile:
                        query = self.request.user.profile.nombre_completo
                        if query:
                            object_list = Video.objects.filter(quienes_aparecen__icontains=query)
                        return object_list
            except Exception:
               object_list = Video.objects.filter(quienes_aparecen__icontains="%%")
            return object_list
        else:
            object_list = Video.objects.filter(quienes_aparecen__icontains="%%")
        return object_list
    
class VideosMineList(LoginRequiredMixin, VideoList):
    template_name = 'AdminVideos/videosmine_list.html' 

    def get_queryset(self):
      return Video.objects.filter(propietario=self.request.user.id)

class VideoDetail(DetailView):
    model = Video
    context_object_name = "video"


class VideoUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    success_url = reverse_lazy("videos-list")
    fields = ["nombre_video","url_video","descripcion_video","quienes_aparecen","image","fecha_video"]
    #fields = '__all__'

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
    fields = ["nombre_video","url_video","descripcion_video","quienes_aparecen","image","fecha_video"]
#    fields = '__all__'

    def form_valid(self, form):
        el_propietario = form.save(commit=False)
        el_propietario.propietario = self.request.user
        el_propietario.save()
        return redirect(self.success_url)

class Login(LoginView):
    next_page = reverse_lazy("videos-list")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('videos-list')


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html', {})


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("videos-list")
    fields = ["nombre_completo","avatar"]

    def form_valid(self, form):
        el_user = form.save(commit=False)
        el_user.user = self.request.user
        el_user.save()
        return redirect(self.success_url)


class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Profile
    success_url = reverse_lazy("videos-list")
    fields = ["nombre_completo","avatar"]

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()


class MensajeCreate(CreateView):
   model = Mensaje
   success_url = reverse_lazy('videos-list')
   fields = '__all__'


class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Mensaje
   context_object_name = "mensaje"
   success_url = reverse_lazy("mensaje-list")

   def test_func(self):
       return Mensaje.objects.filter(destinatario=self.request.user).exists()
    

class MensajeList(LoginRequiredMixin, ListView):
   model = Mensaje
   context_object_name = "mensajes"

   def get_queryset(self):
       import pdb; pdb.set_trace
       return Mensaje.objects.filter(destinatario=self.request.user).all()
    
