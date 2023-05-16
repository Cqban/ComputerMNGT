from django.shortcuts import render,get_object_or_404,redirect
from computerApp.forms import AddMachineForm, AddPersonnelForm, AddInfraForm
from computerApp.models import Machine, Personnel, Infrastructure
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
	infra_id = request.GET.get('infra')
	infrastructures = Infrastructure.objects.all()

	if query:
		machines = machines.filter(nom__icontains=query)
	if mach:
		machines = machines.filter(mach=mach)
	if infra_id:
		machines = machines.filter(infra_id=infra_id)

	context = {'machines': machines, 'today': today, 'infrastructures': infrastructures}
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
			print("form valid")

			infra_id = form.cleaned_data['infra']
			infra = get_object_or_404(Infrastructure, id=infra_id)
			new_machine = Machine(nom=form.cleaned_data['nom'],
									mach=form.cleaned_data['mach'],
									maintenanceDate=form.cleaned_data['maintenanceDate'],
									etat=form.cleaned_data["etat"],
									infra=infra)
			new_machine.save()
			infra.ajouter_machine(new_machine)
			return redirect('machines')
	else:
		form = AddMachineForm()

	infras = Infrastructure.objects.all()
	context = {'form': form, 'infras': infras}
	return render(request, 'computerApp/machine_add.html', context)

def delete_machine(request, machine_id):
	machine = get_object_or_404(Machine, id=machine_id)
	infra = machine.infra
	if request.method == 'POST':
		infra.supprimer_machine(machine)
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
    
def infra_list_view(request):
	infras = Infrastructure.objects.all()

	for infra in infras:
		total_machines = infra.machines.count()
		active_machines = infra.machines.filter(etat=True).count()
        
		if total_machines > 0:
			infra.usage_percentage = active_machines / total_machines * 100
		else:
			infra.usage_percentage = 0
	    
	context={'infras': infras}
	return render(request, 'computerApp/infra_list.html', context)

def infra_add_form(request):
	if request.method == 'POST':
		form = AddInfraForm(request.POST)
		if form.is_valid():
			responsable_id = form.cleaned_data['responsable']
			responsable = get_object_or_404(Personnel, num_secu=responsable_id)
            
			infrastructure = Infrastructure(nom=form.cleaned_data['nom'], responsable=responsable)
			infrastructure.save()
			return redirect('infrastructures')
		else:
			print(form.errors)
	else:
		form = AddInfraForm()
    
	personnels = Personnel.objects.all()
	context = {'form': form, 'personnels': personnels}
	return render(request, 'computerApp/infra_add.html', context)

def delete_infra(request, infrastructure_id):
    infrastructure = get_object_or_404(Infrastructure, id=infrastructure_id)
    if request.method == 'POST':
        infrastructure.machines.all().delete()  # Supprimer toutes les machines associées
        infrastructure.delete()
        return redirect('infrastructures')

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