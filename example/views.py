from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from .serializers import ExampleModel, ExampleSerializer

class ListExampleAPINoAuth (ListAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()


class ListExampleAPIHasAuth (ListAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()
    permission_classes = [IsAuthenticated]


class ListExampleAPIIsAdmin (ListAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()
    permission_classes = [IsAdminUser]

class RetrieveExampleAPINoAuth (RetrieveAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()
    lookup_field = 'id'

class RetrieveExampleAPIHasAuth (RetrieveAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class RetrieveExampleAPIIsAdmin (RetrieveAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAdminUser]


class DeleteExampleAPINoAuth (DestroyAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()
    lookup_field = 'id'

class DeleteExampleAPIHasAuth (DestroyAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class DeleteExampleAPIIsAdmin (DestroyAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAdminUser]


class CreateExampleAPINoAuth (CreateAPIView) : 
    serializer_class = ExampleSerializer

class CreateExampleAPIHasAuth (CreateAPIView) : 
    serializer_class = ExampleSerializer
    permission_classes = [IsAuthenticated]

class CreateExampleAPIIsAdmin (CreateAPIView) : 
    serializer_class = ExampleSerializer
    permission_classes = [IsAdminUser]

class UpdateExampleAPINoAuth (UpdateAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()
    lookup_field = 'id'

class UpdateExampleAPIHasAuth (UpdateAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class UpdateExampleAPIIsAdmin (UpdateAPIView) : 
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAdminUser]
