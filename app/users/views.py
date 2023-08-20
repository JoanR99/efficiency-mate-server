from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User


# Register API
class RegisterApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            },
            status=status.HTTP_201_CREATED,
        )
