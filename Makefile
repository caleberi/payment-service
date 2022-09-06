env_name = payment-service

create_enviroment:
	@echo "🎡 creating environment ..."
	python3 -m venv ~/.${env_name}


setup_environment:
	@echo "🎯 setting up environment"
	#source  ~/.${env_name}/bin/activate

install_deps:
	@echo "🐝 installing required dependencies"
	# python3 -m pip install --upgrade pip
	pip3 install -r requirements.txt
