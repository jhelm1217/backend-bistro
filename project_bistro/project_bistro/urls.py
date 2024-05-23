from django.urls import path, include
from rest_framework import routers
from app_backend_bistro.views import *


router = routers.DefaultRouter()
router.register(r'MenuItem', MenuItemViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'Order', OrderViewSet)
router.register(r'OrderItem', OrderItemViewSet)
router.register(r'driver', DriverViewSet)
router.register(r'review', ReviewViewSet)





urlpatterns = [
    path('', include(router.urls))

]



'''


axios.get(https://this-website.com/students/)

axios.get(https://this-website.com/students/{id}) this will get a specific student with the id key 

axios.post(https://this-website.com/students/) creates a student 

axios.put(https://this-website.com/students/{id}) updates a student  with the speicif key 

axios.delete(https://this-website.com/students/{id}) deletes a student with the specific id key 

url request has 
*header - configuration information 
* body this has the data, parameters 


'''