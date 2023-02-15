from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from rest_framework import viewsets


class TaskNameRouter(viewsets.ModelViewSet):
    serializer_class = TaskNameSerializer
    queryset = Task_name.objects.all() 

class TaskViewRouter(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


@api_view(['GET'])
def TaskView(requset):
    task = Task.objects.all()

    tasks = TaskSerializer(task, many = True).data

    return Response(tasks)

@api_view(['POST'])
def task_name(requset):
    name = requset.POST["name"]
    Task_name.objects.create(name=name)
    return Response('done')


@api_view(['PUT'])
def edit_task(requset, pk):
    name = requset.POST.get("name")
    cat = Task_name.objects.get(id=pk)
    cat.name = name
    cat.save()
    return Response('done')

@api_view(['DELETE'])
def delete_task(requset, pk):
    name = requset.POST.get("name")
    cat = Task_name.objects.get(id=pk).delete
    cat.name = name
    cat.save()

    



