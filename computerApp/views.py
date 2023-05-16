from django.shortcuts import render,get_object_or_404,redirect
from computerApp.forms import AddMachineForm, AddPersonnelForm
from computerApp.models import Machine, Personnel
import openai
from datetime import date

def index(request):
	machines = Machine.objects.all()
	personnels = Personnel.objects.all()
	context = {
		'machines' : machines,
		'personnels' : personnels,
	}
	return render(request, 'index.html', context)

def machine_list_view(request):
	today = date.today
	machines = Machine.objects.all().order_by('nom')
	query = request.GET.get('query')
	mach = request.GET.get('type')
	if query:
		machines = machines.filter(nom__icontains=query)
	if mach:
		machines = machines.filter(mach=mach)
	context = {'machines': machines, 'today': today}
	return render(request, 'computerApp/machine_list.html', context)

def machine_detail_view(request, pk):
	machine = get_object_or_404(Machine, id=pk)
	print(machine.maintenanceDate)
	context={'machine': machine}
	return render(request, 'computerApp/machine_detail.html', context)

def machine_add_form(request):
	if request.method == 'POST':
		form = AddMachineForm(request.POST or None)
		if form.is_valid():
			new_machine = Machine(nom=form.cleaned_data['nom'],
									mach=form.cleaned_data['mach'],
									maintenanceDate=form.cleaned_data['maintenanceDate'],
									etat=form.cleaned_data["etat"])
			new_machine.save()
			return redirect('machines')
	else:
		form = AddMachineForm()
	context = {'form': form}
	return render(request, 'computerApp/machine_add.html', context)

def delete_machine(request, machine_id):
    machine = get_object_or_404(Machine, id=machine_id)
    if request.method == 'POST':
        machine.delete()
        return redirect('machines')
    
def toggle_machine(request, pk):
	machine = get_object_or_404(Machine, id=pk)
	machine.etat = not machine.etat
	if request.method == 'POST':
		machine.save()
		return redirect('machine-detail', pk=pk)
	

def personnel_list_view(request):
	personnels = Personnel.objects.all().order_by('nom')
	query = request.GET.get('q')
	if query:
		personnels = personnels.filter(nom__icontains=query)
	context={'personnels': personnels}
	return render(request, 'computerApp/personnel_list.html', context)

def personnel_detail_view(request, pk):
	personnel = get_object_or_404(Personnel, num_secu=pk)
	context={'personnel': personnel}
	return render(request, 'computerApp/personnel_detail.html', context)

def personnel_add_form(request):
	if request.method == 'POST':
		form = AddPersonnelForm(request.POST or None)
		if form.is_valid():
			new_personnel = Personnel(nom=form.cleaned_data['nom'],
										prenom=form.cleaned_data['prenom'],
										num_secu=form.cleaned_data['num_secu'],
										sexe=form.cleaned_data['sexe']
									)
			print("Saved")
			new_personnel.save()
			return redirect('personnels')
	else:
		form = AddPersonnelForm()
	context = {'form': form}
	return render(request, 'computerApp/personnel_add.html', context)

def delete_personnel(request, personnel_id):
    personnel = get_object_or_404(Personnel, num_secu=personnel_id)
    if request.method == 'POST':
        personnel.delete()
        return redirect('personnels')


api_key = "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"

def chat_bot(request):
	chatbot_response = None
	if api_key is not None and request.method == 'POST':
		openai.api_key = api_key
		user_input = request.POST.get('user_input')
		prompt = user_input

		response = openai.Completion.create(
			engine = 'text-davinci-003',
			prompt = prompt,
			max_tokens=256,
			#stop="."
			temperature=0.5
		)
		print(response)

		chatbot_response = response["choices"][0]["text"]

	return render(request, 'chat.html', {"response": chatbot_response})