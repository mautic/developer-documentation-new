# -*- coding: utf-8 -*-

import requests
import os

def get_code_samples(app):

    print("Getting code samples from GitHub... This might take a while!")
    
    code_samples = app.config.code_samples
    code_samples_downloaded_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/code_samples_downloaded"

    for key in code_samples:
        # E.g. code_samples_downloaded/Entity_World.php
        file_path = code_samples_downloaded_dir + "/" + key

        # If the file exists already, skip downloading it, so that we don't overload GitHub with requests
        if (os.path.exists(file_path)):
            print(key + " exists already. Skipping download.")
            continue

        print("Downloading " + code_samples[key] + "...")

        # Get the code from GitHub and copy into the file (key), e.g. Entity_World
        r = requests.get(code_samples[key], allow_redirects=True)
        open(code_samples_downloaded_dir + "/" + key, 'wb').write(r.content)

def setup(app):

    app.add_config_value('code_samples', {}, True)
    app.connect("builder-inited", get_code_samples)
