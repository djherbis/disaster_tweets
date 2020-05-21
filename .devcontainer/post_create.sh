echo "post_create.sh CWD: $(pwd)"
pip install whisk
whisk setup
source venv/bin/activate
whisk dvc setup
dvc pull
