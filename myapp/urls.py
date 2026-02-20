from django.contrib import admin
from django.urls import path, include
from myapp.views import view1, view2, view3, view4, view5, view6, view7


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('rs1/', view1),
    path('rs2/', view2),
    path('rs3/', view3),
    path('rs4/', view4),
    path('rs5/', view5),
    path('rs6/', view6),
    path('rs7/', view7),

]