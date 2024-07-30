from django.shortcuts import render
from django.http import JsonResponse
import random

# Importing algorithms
from sorting_algorithms.bubbleSort import bubble_sort
from sorting_algorithms.selectionSort import selection_sort
from sorting_algorithms.insertionSort import insertion_sort
from sorting_algorithms.mergeSort import merge_sort
from sorting_algorithms.quickSort import quick_sort
from sorting_algorithms.heapSort import heap_sort
from sorting_algorithms.countingSort import counting_sort

def home(request):
    return render(request, 'home.html')

def generate_random_values(request):
    data = [random.randint(1, 150) for _ in range(50)]  # Reduced the number of elements for better visibility
    return JsonResponse({'values': data})

def sort_values(request):
    data = list(map(int, request.GET.getlist('data[]')))
    algorithm = request.GET.get('algorithm')
    time_tick = float(request.GET.get('speed'))

    sorting_steps = []

    def store_step(arr, colorArray):
        sorting_steps.append({'data': arr.copy(), 'colors': colorArray.copy()})

    if algorithm == 'Bubble Sort':
        bubble_sort(data, store_step, time_tick)
    elif algorithm == 'Selection Sort':
        selection_sort(data, store_step, time_tick)
    elif algorithm == 'Insertion Sort':
        insertion_sort(data, store_step, time_tick)
    elif algorithm == 'Merge Sort':
        merge_sort(data, 0, len(data) - 1, store_step, time_tick)
    elif algorithm == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, store_step, time_tick)
    elif algorithm == 'Heap Sort':
        heap_sort(data, store_step, time_tick)
    else:
        counting_sort(data, store_step, time_tick)

    return JsonResponse({'steps': sorting_steps})
