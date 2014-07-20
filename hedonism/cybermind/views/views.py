from django.shortcuts import render


LOOP_COUNTER = [i for i in range(100)]


def cybermind(request, name):
    human_name = str(name).title()
    context = {'count': LOOP_COUNTER, 'human_name': human_name}
    return render(request, 'cybermind/cybermind.html', context)
