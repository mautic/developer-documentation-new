from . import link

link_name = "hello_world_plugin" 
link_text = "Hello World Plugin" 
link_url = "https://github.com/mautic/plugin-helloworld" 

link.xref_links.update({link_name: (link_text, link_url)})
