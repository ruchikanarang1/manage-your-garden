from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from plants.models import Add

# Create your views here.
def index(request):
    return render(request, 'index1.html')
   #return HttpResponse("home page")




def find(request):
        if request.method == 'POST':
            search_query = request.POST.get('search_query')
        # Perform a search query based on the user input
            plants = Add.objects.filter(name__icontains=search_query)
            return render(request, 'find_plant_results.html', {'plants': plants, 'search_query': search_query})
        return render(request, 'find.html')
    

def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        
        # Check if all required fields are present
        if name and description and price:
            # Create and save the new plant
            plant = Add(name=name, description=description, price=price)
            plant.save()
    return render(request, 'add.html')

def delete(request):    
    plants = Add.objects.all()
    selected_plant = None

    if request.method == 'POST':
        plant_id = request.POST.get('plant')
        if plant_id:
            selected_plant = get_object_or_404(Add, pk=plant_id)

    return render(request, 'delete.html', {'plants': plants, 'selected_plant': selected_plant})

def confirm_delete(request):
    if request.method == 'POST':
        plant_id = request.POST.get('plant_id')
        if plant_id:
            plant = get_object_or_404(Add, pk=plant_id)
            plant.delete()
            return redirect('plant_list')
    return redirect('delete')







# Create your views here.
