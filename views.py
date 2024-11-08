from django.shortcuts import render, get_object_or_404, redirect
from theater_lab.models import Actor
from .forms import ActorForm
from django.http import JsonResponse

def actor_list(request):
    actors = Actor.objects.all()
    return render(request, 'actors/actor_list.html', {'actors': actors})

def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    return render(request, 'actors/actor_detail.html', {'actor': actor})

def actor_create_or_edit(request, pk=None):
    actor = get_object_or_404(Actor, pk=pk) if pk else None
    if request.method == "POST":
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect('actor_list')
    else:
        form = ActorForm(instance=actor)
    return render(request, 'actors/actor_create_or_edit.html', {'form': form})

def actor_delete(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    if request.method == "POST":
        actor.delete()
        return redirect('actor_list')
    return render(request, 'actors/confirm_delete.html', {'actor': actor})
