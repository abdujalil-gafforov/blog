mig:
	./manage.py makemigrations
	./manage.py migrate
	@echo "----------------------------------------------------------------"
	@echo "Ma'lumotlar yangilandi"
hello:
	@echo "hello"
update:
	sudo apt update
	sudo apt upgrade
	yes
