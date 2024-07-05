Providing effective user feedback
=================================

When developing features, it's crucial to ensure that Users receive clear feedback and guidance when certain information or data is not available. Instead of simply hiding tabs or displaying zeroed metrics, for example, we should adopt a proactive approach to inform and guide Users.

Fundamental principles
----------------------

The principles of visibility, transparency, and guidance form the foundation of an intuitive and informative User experience.

- **Visibility**: Keep all functionalities visible, even when there is no data available.
- **Transparency**: Communicate that information is missing.
- **Guidance**: Provide instructions on how to obtain or enable the necessary data.

Visibility ensures that Users are aware of all available functionalities, even when they are not active or populated. Transparency builds trust by clearly explaining why certain information might be missing. Guidance empowers Users by providing clear paths for action and improvement. Together, these principles transform Points of frustration into solutions, helping marketing professionals complete their tasks.

Practical implementation
------------------------

The practical implementation of these guidelines in Mautic goes beyond simply avoiding blank screens. It involves creating a conversation with the User, anticipating their needs, and guiding them with minimal workload. Every informative message, call to action (CTA), or configuration tip serves as a contextual mini-tutorial, educating Users about the platform's capabilities while helping them overcome obstacles.

When encountering situations where data is absent, follow these guidelines:

- Replace empty areas or zeroed metrics with explanatory messages. For example:
  
  "We don't have any information about the devices used yet. This will happen automatically when Users interact with your Campaigns."
  
- Include clear CTAs that guide the User on how to proceed. For example:
  
  "No Email activity? Start sending some Campaigns to populate this data!"
  
- If the lack of data is due to incomplete configuration, provide direct guidance:
  
  "It looks like device tracking is not enabled. Go to settings to enable it."
  
- Help Users understand the value of the missing data:
  
  "Device information helps optimize your Campaigns for different platforms. Once we have this data, you'll see detailed analytics here."
  
- Use icons, colors, or visual elements to indicate areas that need attention.

This approach not only improves immediate usability but also accelerates Users' learning curve, leading to more sophisticated use of the platform over time. Users do not feel "stuck" when encountering areas without data, but are instead motivated to explore and fill those gaps.

"No Results" template
---------------------

Mautic includes a reusable template for displaying informative messages when no results are available. This template offers a consistent and flexible way to provide User feedback, with options for additional actions.

Template Structure
------------------

.. code-block:: twig

    {% if tip is defined %}
    <div class="alert alert-info">
        {{ tip|trans }}
        {% if link is defined and (href is defined or onclick is defined) %}
        <a class="ml-a" href="{{href}}" onclick="{{onclick}}">{{link|trans}}</a>
        {% endif %}
    </div>
    {% endif %}

Parameters
----------

The template accepts the following parameters:

- **tip** (required): A translation string that contains the main message to be displayed.
- **link** (optional): A translation string for the link/button text.
- **href** (optional): URL for navigation when the link is clicked.
- **onclick** (optional): JavaScript function to be executed when the link is clicked.

Functionality
-------------

The template checks if `tip` is defined. If not, nothing will be rendered. If `tip` is present, a `div` with the class `alert alert-info` is created, containing the translated message. If `link` is defined, and at least one of `href` or `onclick` is also present, a link will be added below the main message. The link can be configured to navigate to a new page (`href`) or execute a JavaScript function (`onclick`).

Usage example
-------------

To use this template in your code, you can include it as follows:

.. code-block:: twig

    {{ include('@MauticCore/Helper/no-information.html.twig', {
        'tip': 'Mautic.segment.no.results',
        'link': 'Mautic.segment.add.new',
        'href': '{{ path('Mautic_segment_action', {'objectAction': 'new'}) }}'
    }) }}

In this example, the template will display a message indicating that no Segments are available, with a link to create a new Segment.

Why?
----

It ensures a uniform presentation of "no results" messages across the platform, providing consistency in the User experience. Its flexibility allows it to be used in various situations, from empty lists to graphs without data, adapting to different contexts. The optional link makes the template actionable, guiding the User to actions that can resolve the "no results" situation, promoting engagement and problem resolution. Additionally, support for internationalization allows messages to be translated into different languages, making the platform more globally accessible.

Best practices
--------------

To maximize the effectiveness of this template, it's important to follow some best practices. Always provide a clear and informative message in the `tip` parameter, ensuring that the User understands the current situation. When appropriate, include a link to an action that can help the User resolve the "no results" situation, promoting a more interactive and solution-oriented experience. It's crucial to use specific messages for each context, avoiding generic texts like "No results found," which may not provide useful information to the User. Finally, ensure that all strings used are included in the translation files, guaranteeing a consistent experience in all supported languages.

This approach aligns with modern User experience (UX) design best practices. It incorporates principles of informative design, immediate feedback, and contextual guidance. By providing relevant information and actions at the exact moment and place where the User needs them, we are creating an interface that not only reacts to User actions but anticipates and meets their needs.

Clear messages and specific guidance can reduce the number of support tickets related to User confusion or "missing" functionalities. Additionally, by standardizing how we handle empty or inactive states across the platform, we create a more consistent and maintainable codebase.

It's essential to note that, while we have general guidelines, implementation should be customized for each specific context. A message that works well for empty Email metrics might not be appropriate for a Campaign report without data. Think critically about the specific context of each implementation and adapt the messages and CTAs accordingly.
