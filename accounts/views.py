from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile
