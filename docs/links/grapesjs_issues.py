from . import link

link_name = "GrapesJS issue queue" 
link_text = "GrapesJS builder issues" 
link_url = "https://github.com/mautic/mautic/issues?q=is%3Aopen+is%3Aissue+label%3Abuilder-grapesjs" 

link.xref_links.update({link_name: (link_text, link_url)})
