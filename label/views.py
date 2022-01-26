from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import os, datetime, csv

from .models import Patient
from .forms import PatientForm

@login_required
def patient_detail(request, pk):
    CHOICES_AP = {  '0': 'Normal',
                    '1': 'Apical Anterior',
                    '2': 'Basal',
                    '3': 'Septal',
                    '4': 'Deleted'
                }
    CHOICES_lat = { '0': 'Normal',
                    '1': 'Septal',
                    '2': 'Posterolateral',
                    '3': 'Deleted'
                }
    if request.method == 'POST':
        item = get_object_or_404(Patient, pk=pk)
        form = PatientForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # save the post content
            item.date_of_update = str(datetime.datetime.today())
            item.apl = form.cleaned_data['label_ap']
            item.latl = form.cleaned_data['label_lat']
            item.save()

            if item.pk == Patient.objects.count():
                # no NEXT (1)
                content = {
                        'name': item.name,
                        'previous': item.pk -1,
                        'next': item.pk + 1,
                        'ref': item.ref.url,
                        'ap': item.ap.url,
                        'lat': item.lat.url,
                        'apl': CHOICES_AP[item.apl],
                        'latl': CHOICES_lat[item.latl],
                        'form': form,
                        'btn':1,
                }
            elif item.pk == 1:
                # no PREVIOUS (2)
                content = {
                        'name': item.name,
                        'previous': item.pk -1,
                        'next': item.pk + 1,
                        'ref': item.ref.url,
                        'ap': item.ap.url,
                        'lat': item.lat.url,
                        'apl': CHOICES_AP[item.apl],
                        'latl': CHOICES_lat[item.latl],
                        'form': form,
                        'btn':2,
                }
            else:
                content = {
                        'name': item.name,
                        'previous': item.pk -1,
                        'next': item.pk + 1,
                        'ref': item.ref.url,
                        'ap': item.ap.url,
                        'lat': item.lat.url,
                        'apl': CHOICES_AP[item.apl],
                        'latl': CHOICES_lat[item.latl],
                        'form': form,
                        'btn':0,
                }
            return render(request, 'label/patient_detail.html', content)

    else:
        item = get_object_or_404(Patient, pk=pk)
        form = PatientForm()
        if item.pk == Patient.objects.count():
            # no NEXT (1)
            content = {
                    'name': item.name,
                    'previous': item.pk -1,
                    'next': item.pk + 1,
                    'ref': item.ref.url,
                    'ap': item.ap.url,
                    'lat': item.lat.url,
                    'apl': CHOICES_AP[item.apl],
                    'latl': CHOICES_lat[item.latl],
                    'form': form,
                    'btn':1,
            }
        elif item.pk == 1:
            # no PREVIOUS (2)
            content = {
                    'name': item.name,
                    'previous': item.pk -1,
                    'next': item.pk + 1,
                    'ref': item.ref.url,
                    'ap': item.ap.url,
                    'lat': item.lat.url,
                    'apl': CHOICES_AP[item.apl],
                    'latl': CHOICES_lat[item.latl],
                    'form': form,
                    'btn':2,
            }
        else:
            content = {
                    'name': item.name,
                    'previous': item.pk -1,
                    'next': item.pk + 1,
                    'ref': item.ref.url,
                    'ap': item.ap.url,
                    'lat': item.lat.url,
                    'apl': CHOICES_AP[item.apl],
                    'latl': CHOICES_lat[item.latl],
                    'form': form,
                    'btn':0,
            }
        return render(request, 'label/patient_detail.html', content)


@login_required
def load_csv(request):
    csvfile = "patients.csv"
    with open(csvfile) as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers
        for row in reader:
            _, created = Patient.objects.get_or_create(
            name = row[0],
            ref = row[1],
            ap = row[2],
            apl = row[3],
            lat = row[4],
            latl = row[5],
            )
    return HttpResponseRedirect(reverse('patient_detail', kwargs={'pk':1}))
