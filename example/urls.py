from django.urls import path
from .views import (
    ListExampleAPIHasAuth,
    ListExampleAPIIsAdmin,
    ListExampleAPINoAuth,
    RetrieveExampleAPIHasAuth,
    RetrieveExampleAPIIsAdmin,
    RetrieveExampleAPINoAuth,
    DeleteExampleAPIHasAuth,
    DeleteExampleAPIIsAdmin,
    DeleteExampleAPINoAuth,
    CreateExampleAPIHasAuth,
    CreateExampleAPIIsAdmin,
    CreateExampleAPINoAuth,
    UpdateExampleAPIHasAuth,
    UpdateExampleAPIIsAdmin,
    UpdateExampleAPINoAuth,
)

urlpatterns = [
    path('list/no-auth/', ListExampleAPINoAuth.as_view(), name='list-no-auth'),
    path('list/is-auth/', ListExampleAPIHasAuth.as_view(), name='list-is-auth'),
    path('list/is-admin/', ListExampleAPIIsAdmin.as_view(), name='list-is-admin'),
    
    path('retrieve/no-auth/<int:id>/', RetrieveExampleAPINoAuth.as_view(), name='retrieve-no-auth'),
    path('retrieve/is-auth/<int:id>/', RetrieveExampleAPIHasAuth.as_view(), name='retrieve-is-auth'),
    path('retrieve/is-admin/<int:id>/', RetrieveExampleAPIIsAdmin.as_view(), name='retrieve-is-admin'),
    
    path('delete/no-auth/<int:id>/', DeleteExampleAPINoAuth.as_view(), name='delete-no-auth'),
    path('delete/is-auth/<int:id>/', DeleteExampleAPIHasAuth.as_view(), name='delete-is-auth'),
    path('delete/is-admin/<int:id>/', DeleteExampleAPIIsAdmin.as_view(), name='delete-is-admin'),
    
    path('create/no-auth/', CreateExampleAPINoAuth.as_view(), name='create-no-auth'),
    path('create/is-auth/', CreateExampleAPIHasAuth.as_view(), name='create-is-auth'),
    path('create/is-admin/', CreateExampleAPIIsAdmin.as_view(), name='create-is-admin'),
    
    path('update/no-auth/<int:id>/', UpdateExampleAPINoAuth.as_view(), name='update-no-auth'),
    path('update/is-auth/<int:id>/', UpdateExampleAPIHasAuth.as_view(), name='update-is-auth'),
    path('update/is-admin/<int:id>/', UpdateExampleAPIIsAdmin.as_view(), name='update-is-admin'),
    

]