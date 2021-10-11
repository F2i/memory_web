from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as LogOut

from .models import Memory
import folium
from jinja2 import Template

# Create your views here.
class MyNewMarker(folium.ClickForMarker):
    _template = Template(u"""
        {% macro script(this, kwargs) %}
            function newMarker(e){
                //xoa pin cu
                {{this._parent.get_name()}}.eachLayer(function(layer){ 
                        if (layer instanceof L.Marker){
                        {{this._parent.get_name()}}.removeLayer(layer);
                        }});
                var new_mark = L.marker().setLatLng(e.latlng).addTo({{this._parent.get_name()}});
                // new_mark.dragging.enable();
                // new_mark.on('dblclick', function(e){ {{this._parent.get_name()}}.removeLayer(e.target)});
                new_mark.bindPopup({{ this.popup }});
                //lay output coor
                var input_lat = parent.document.getElementById('validationLat');
			    var input_lng = parent.document.getElementById('validationLng');
                input_lat.value = e.latlng.lat.toFixed(4);
                input_lng.value = e.latlng.lng.toFixed(4);
                };
            {{this._parent.get_name()}}.on('click', newMarker);
        {% endmacro %}
        """)  # noqa



def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    memories = Memory.objects.filter(user=request.user)
    if memories:
        memories = reversed(memories)

    else:
        pass

    return render(request, 'home.html', {'memories': memories})


@login_required
def create(request):
    def memory_creation_page(request):
        map = folium.Map(
            location=[10.774592941159328, 106.69244265706874], zoom_start=15)
        map.add_child(MyNewMarker(popup="Anh ban a!"))
        map = map._repr_html_()
        # cai nay co the dung ModelForm class de tot hon
        return render(request, 'memorycreation.html', {'map': map})


    if request.method == 'POST':
        location, comment, lat, lng = request.POST.get(
            'location'), request.POST.get('comment'), request.POST.get('lat'), request.POST.get('lng')
        if location and comment and lat and lng:
            memory = Memory(location=location,
                            comment=comment,
                            latitude=lat,
                            longtitude=lng,
                            user=request.user)
            memory.save()
            return redirect('home')
        else:
            return memory_creation_page(request)
    else:
        return memory_creation_page(request)


@login_required
def logout(request):
    LogOut(request)
    return render(request, 'logout.html')
