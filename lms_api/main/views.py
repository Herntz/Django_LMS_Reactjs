from rest_framework import generics
from rest_framework import permissions
from .serializers import *
from .models import *

class TeacherList(generics.ListCreateAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes=[permissions.IsAuthenticated]
    
class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes=[permissions.IsAuthenticated]

    # def  post(self, request):
    #     return render(request, 'teacher_list.html' , {'form':TeacherForm()})
