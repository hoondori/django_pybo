sudo apt update
sudo apt install python3-venv git
mkdir -p projects/venvs
python3 -m venv projects/venvs/mysite
source ./projects/venvs/mysite/bin/activate
pip install  wheel
pip install django==3.1.3 markdown
cd ./projects
git clone https://github.com/hoondori/django_pybo.git
cd ./django_pybo
python3 manage.py runserver