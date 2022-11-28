# -*- coding: utf-8 -*-

from typing import Any, Dict, List

from docutils import nodes
from docutils.parsers import rst as RST

import sphinx
from sphinx.application import Sphinx
from sphinx.writers.html import HTMLTranslator
from sphinx.writers.latex import LaTeXTranslator

####################### PART I: RST/DOCUTILS SIDE #######################


class helloworld_plugin_node(nodes.General, nodes.Element):
    pass


class HelloWorldPluginDiv(RST.Directive):
    """
    Maps source RST to a <jinja_div_node> doctree node.
    Example rst:
     .. hellworld_plugin:: https://github.com/mautic/plugin-helloworld/blob/mautic-4/Entity/World.php
    Resulting doctree node:
        <div class="admonition info">
            <p class="admonition-title">View on GitHub</p>
            <p>For a most recent example of this code, visit the <a class="reference external" href="https://github.com/mautic/plugin-helloworld/XX">GitHub repo</a> for more information.</p>
        </div>
    """
    node_class = helloworld_plugin_node
    optional_arguments = 0
    option_spec = {
        'url': RST.directives.unchanged
    }
    has_content = True

    def run(self) -> List[nodes.Node]:
        """Create doctree <div> from rst/myst source"""
        # This ensures that we show the content in an "INFO" div block
        self.options['class'] = ['admonition info']
        RST.roles.set_classes(self.options)
        if self.arguments:
            self.options['urls'] = [self.arguments[0]]
        if self.has_content:
            text = '\n'.join(self.content)
        else:
            text = ''
        doctree_node = helloworld_plugin_node(text, **self.options)
        self.add_name(doctree_node)
        self.state.nested_parse(self.content, self.content_offset, doctree_node)
        return [doctree_node]


####################### PART II: SPHINX/HTML SIDE #######################


def visit_helloworld_plugin_div(self: HTMLTranslator, node: helloworld_plugin_node) -> None:
    """
    Maps <div> doctree element to the html output.
    """
    if node.children:
        txt = node.children[0].astext()
    node.remove(node.children[0])

    # self.starttag is defined in docutils.writers.HTML5Translator
    self.body.append(
        self.starttag(node, 'div') + ('<p class="admonition-title">Code Example</p><p>The code example below might be outdated. Find <a href="%s">the latest version of this code example on GitHub</a>.</p>' % txt)
    )
    self.body.append('</div>')


def depart_helloworld_plugin_div(self: HTMLTranslator, node: helloworld_plugin_node) -> None:
    pass


def latex_visit_helloworld_plugin_div(self: LaTeXTranslator, node: helloworld_plugin_node) -> None:
    node.pop(0)


def latex_depart_helloworld_plugin_div(self: LaTeXTranslator, node: helloworld_plugin_node) -> None:
    pass


def setup(app: Sphinx) -> Dict[str, Any]:
    """ Add new doctree node definition to Sphinx, then add html & latex translators for that node. """ 
    app.add_node(helloworld_plugin_node,
                 html=(visit_helloworld_plugin_div, depart_helloworld_plugin_div),
                 latex=(latex_visit_helloworld_plugin_div, latex_depart_helloworld_plugin_div),
                 text=(visit_helloworld_plugin_div, depart_helloworld_plugin_div),
                 man=(visit_helloworld_plugin_div, depart_helloworld_plugin_div),
                 texinfo=(visit_helloworld_plugin_div, depart_helloworld_plugin_div))

    app.add_directive('helloworld-plugin-code-url', HelloWorldPluginDiv)

    return {
        'version': sphinx.__display_version__,
    }