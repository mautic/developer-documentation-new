from . import _main_code_sample

# Output file name must be unique!
output_file_name = "Entity_World.php"
# Ensure that the URL always starts with https://raw.githubusercontent.com/...
url = "https://raw.githubusercontent.com/mautic/plugin-helloworld/mautic-4/Entity/World.php" 

_main_code_sample.code_samples.update({output_file_name: (url)})
