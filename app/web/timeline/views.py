from django.views.generic import CreateView, DeleteView, ListView, UpdateView, View
from .models import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse
from .forms import *
from web.users.auth import auth_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404
from web.users.auth import user_passes_test
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, permission_required
from django.forms.models import model_to_dict
import json


@user_passes_test(auth_test, group_name='wonen')
def manage_timeline(request):
    Moment_FormSet = modelformset_factory(Moment, form=MomentForm, extra=0, can_delete=True)
    if request.method == 'POST':
        formset = Moment_FormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            instances = formset.save()
            for instance in instances:
                instance.save()
            for object in formset.deleted_objects:
                object.delete()
            return HttpResponseRedirect(reverse('manage_timeline'))

    else:
        formset = Moment_FormSet()
    return render(request, 'timeline/manage_moments.html', {
        'moment_form_set': formset,
        'form': MomentForm()
    })


@require_http_methods(["POST"])
@user_passes_test(auth_test, group_name='wonen')
def update_moment(request, moment_id):
    form = MomentForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        instance = form.save()
        print(instance.name)
        return JsonResponse(model_to_dict(instance))
    return JsonResponse(form.errors)


class MomentUpdateView(UserPassesTestMixin, UpdateView):
    model = Moment
    form_class = MomentForm
    http_method_names = ['post', ]

    def test_func(self):
        return auth_test(self.request.user, 'wonen')

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({'message' : 'Data is saved'}, status=200)

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)


@require_http_methods(["POST"])
@user_passes_test(auth_test, group_name='wonen')
def order_timeline(request):
    if request.is_ajax():
        data = json.loads(request.body)
        moment_list = Moment.objects.filter(id__in=[o['id'] for o in data])
        for i, moment in enumerate(moment_list):
            moment.order = data[i]['order']
        Moment.objects.bulk_update(moment_list, ['order'])
        return JsonResponse({'message': 'Data is saved'}, status=200)
    return JsonResponse({'message': 'error'}, status=400)


