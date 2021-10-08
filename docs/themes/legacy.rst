Legacy Builder
==========================================================

.. Warning:: The legacy Builder is still available in Mautic 4, however it will be removed in Mautic 5. Refer to the `Builder documentation <https://docs.mautic.org/en/builders>`__ for more information.

Slots
-----

Slot definition
^^^^^^^^^^^^^^^

The slot can be defined by a single HTML attribute ```data-slot="{slot type here}"````. For example, the text slot can be defined even with the demo content.

When the Theme is opened in the builder, the div with attribute ```data-slot="text"``` will make the text inside the div editable within the inline Froala editor.

.. code-block:: html

    <div data-slot="text">
        <a>@JaneDoe</a> has invited you to join Awesome inc!
    </div>

The slot types currently built:

Image
"""""
Inserts a single image into the div. You can click on it and edit it with options which provides Froala editor (link, change image source, alt text, ...)

Button
""""""
Inserts an HTML button. You can define text, URL as well as padding, size and position.

Text
""""
Inserts a new text slot which you can edit with a HTML editor.  This enables the use of media such as images and videos.

Separator
"""""""""
Inserts a horizontal line to separate content.

Slot Containers
^^^^^^^^^^^^^^^
As previously stated, the user can drag and drop new slots when creating an email based on a Theme. Therefore, as a Theme developer, you have to define where the user can drop the slots. You can do this with a single HTML attribute ``data-slot-container="1"``.

.. code-block:: html

    <div data-slot-container="1">
        <div data-slot="text">
            <a>@JaneDoe</a> has invited you to join Awesome inc!
        </div>
    </div>

This enables the user to drop the new slots into this container. In the example above there is already one predefined slot which the user can move to another container, remove or edit.

This functionality will provide you with lots of creative freedom for designing and developing your own unique Email and Landing Pages. Have a unique design? Share it with the community on the forums! We would love to see how you’re using Mautic to engage your audience.

Sections
---------

Sections are full width parts of the Theme which can enable the user to change the background color in the section wrapper (full monitor width) and in the section content itself. It’s possible to move the sections up or down, delete the sections and even create a new ones with layout of 1,2 or 3 columns.

Section
^^^^^^^

The section holds the content. It should be centered and should have fixed width. This fixed width should be consistent with all other sections. Section also wraps the content. The section can be any block HTML element with attribute ``data-section="1"``.

.. code-block:: html

    <div data-section="1">
        <div data-slot-container="1">
            <div data-slot="text">
                <a>@JaneDoe</a> has invited you to join Awesome inc!
            </div>
        </div>
    </div>

Section Wrapper
^^^^^^^

Section wrappers must have 100% width of the browser window. You therefore have to split your theme into several "rows" if you want to enable the users to change the background of each section. The section wrapper can be any block HTML element with attribute ``data-section-wrapper="1"``.

.. code-block:: html

    <div data-section-wrapper="1">
        <div data-section="1">
          <div data-slot-container="1">
              <div data-slot="text">
                  <a>@JaneDoe</a> has invited you to join Awesome inc!
              </div>
          </div>
        </div>
    </div>
