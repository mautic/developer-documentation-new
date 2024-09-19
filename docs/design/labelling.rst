Guidelines for labelling the Mautic interface
============================================

Capitalization
--------------

Use sentence—case capitalization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. vale off

Sentence-style capitalization is the preferred method for UI text elements due to its readability and efficiency. This style, which is predominantly lowercase, makes it easy for readers to distinguish between common nouns and proper nouns, and is generally considered the quickest form to read.

.. vale on

When using sentence-case capitalization, only capitalize the initial letter of the first word in the text and other words that require capitalization, such as proper nouns.

.. vale off

For example, you would write labels in a form as "First name" and "Email address." Apply this approach consistently across all UI text elements, except when the text is a product or service name, or trademarked.

.. vale on

Examples:

.. vale off

- Analyse your lead generation chart with Marketing Insights.
- Automate your marketing Campaigns.

.. vale on

Avoid title case capitalization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Title or headline case capitalization involves capitalizing the first letter of most words, excluding articles, conjunctions, or prepositions unless they're the first or last word in the sentence or phrase.

However, this approach presents several challenges in practical implementation:

- It requires all content creators within an organization to understand and consistently apply complex grammatical rules regarding word capitalization.
- It often relies on subjective interpretations of what constitutes "important" or "special" words, which leads to inconsistencies if not clearly communicated or understood across the organization.
- Moreover, title case can impede reading speed and comprehension, as it makes it more difficult for readers to distinguish between proper nouns and common nouns.

These factors combined make title case less desirable in many user interface and content design scenarios, especially when prioritizing clarity and ease of reading.

**Do:** automate your marketing Campaigns

**Avoid:** automate your marketing Campaigns

Avoid all caps capitalization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. vale off

All caps (or uppercase) capitalization means every letter is capitalized. This style is slower to read, especially for longer text, because individual letter shapes are less distinguishable due to their uniform height and lack of ascenders or descenders.

.. vale on

It also typically requires more space in the UI per letter compared to sentence case. Additionally, it makes it difficult for readers to distinguish between proper nouns and common nouns. For example, product names are easily distinguishable from features in regular text, but these distinctions take longer when the text is in all caps.

**Do:** Get started with Mautic to automate your marketing workflows and enhance customer engagement.

.. vale off

**Avoid:** GET STARTED WITH MAUTIC TO AUTOMATE YOUR MARKETING WORKFLOWS AND ENHANCE CUSTOMER ENGAGEMENT.

.. vale on

When to use capital letters
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Capital letters are reserved for:

- Official, trademarked products or services, unless they intentionally use a lowercase initial, such as the iPhone.
- Initialisms (for example, FBI, CIA) or acronyms (for example, NASA, UNESCO).
- Names of people.
- Names of countries or places.
- UI labels that are capitalized.
- Words that begin a sentence or phrase.

If a term is not in the list above, it should not be capitalized. Some company and product names use non-standard capitalization. When referring to these, ensure accuracy. Examples include node.js, GitHub, eBay and JavaScript.

How to refer to UI elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When writing about a UI element, use the same capitalization as seen in the UI. For example, if an input field is labeled "Email," refer to it as the Email input field. Similarly, if a button is labeled "Submit," correctly refer to it as the Submit button. If a product page is titled "User dashboard," write it as "Access your settings on the User dashboard page."

**Do:** Access your settings on the User dashboard page.

**Avoid:** Access your settings on the User Dashboard page.

Capitalizing proper nouns
^^^^^^^^^^^^^^^^^^^^^^^^^

The names of people, places, and products are proper nouns and therefore all take initial capitals. Examples of proper nouns are:

.. vale off

- Ruth Cheesley
- Mautic Conference Europe 2024
- São Paulo, Brazil
- Microsoft Copilot

.. vale on

Capitalizing abbreviations
^^^^^^^^^^^^^^^^^^^^^^^^^^

When referencing a product name, use the official full name rather than an abbreviation or initials. Use all uppercase letters for well-recognized abbreviations, including both initialisms and acronyms, such as GIF.

- ASCII
- CAPTCHA
- FAQ
- HTML
- OK (not Ok or Okay)

When there's a possibility that an abbreviation might be unfamiliar to the target audience, it's advisable to spell it out in full the first time you use it. For commonly known abbreviations, such as PDF, CEO, or AM/PM, it's perfectly acceptable to use them without spelling them out.

Capitalizing all other words
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Capitalize a word only if it begins a sentence, phrase, or UI element name. To emphasize a particular word or phrase within a sentence, use italic or bold formatting (but not both) instead of capitalizing it to denote "specialness."

Examples:

**Do:** You can use a global policy to apply changes to all Users.

**Avoid:** You can use a Global Policy to apply changes to all Users


Simple writing
==============

Use simple words and sentences
------------------------------

Choose the simplest term suitable for your audience; for instance, use "fast" instead of "expeditious" and "start" instead of "commence." Be concise by keeping sentences short and straightforward, and remove wordy or redundant phrases.

.. tip::
   Create a terminology list for your product that includes preferred words and those to avoid. This tool aids consistency, especially when multiple people are writing copy.

Respect Users' time by making content quick and easy to read. Trim content to as few words as possible without being terse. It's advisable to avoid terms of politeness, such as "please" and "thank you," in a UI, as they may be inappropriate or offensive in some cultural contexts.

Use simple present tense
------------------------

Use simple verbs and tenses, and keep sentences concise, friendly, and punchy. Focus on the User's context to make content relevant. The more familiar you are with their situation, the better you can communicate effectively with fewer words. When using past or future tense, prefer straightforward verb forms over those with "have," "has," "had," "been," "should," "would," and "will."

Conversational style
--------------------

To set the appropriate tone and conversation level, imagine the User engaging with the product as if in a dialogue. The interaction between words, imagery, and actions forms this conversation, creating a back-and-forth on the screen between the User and the product.

The conversational level depends on the User's journey stage and the task they're performing. The most conversational content typically appears in the "discover, try, and buy" phases, while error messages often require brevity.

Regardless of the conversational level, writing should always be simple, clear, and easy to understand, maintaining a friendly, human, and inviting tone. Use everyday language instead of jargon, and choose short words for faster reading rather than long, impressive-sounding ones.

Formal versus casual tone
-------------------------

While a formal tone is often suitable for technical and business writing, a more casual tone is increasingly accepted and expected in UI and supporting materials. Use contractions when they fit the context and enhance the flow. Starting sentences with "and," "but," or "so" is acceptable when it creates shorter, scannable sentences, but use these sparingly. Use exclamation marks positively and limit them to one per context.

Examples:

**Do:** Your campaign was sent successfully !

**Avoid:** An error occurred during the process!!

Terms of politeness
-------------------

These terms are often overused and can convey an inappropriate tone for technical material, as they're perceived differently across cultures. Use terms like "please" and "thank you" thoughtfully.

For example, you might say, "The Mautic installation process might take a few minutes. Please wait." Use politeness in a UI only when the User is experiencing an inconvenience.

For instance, avoid saying, "Please configure your email settings to access advanced features," as it can be unnecessary.

Can, may, and might
-------------------

Terms of ability
^^^^^^^^^^^^^^^^

These terms are often misused. "Can" implies ability, while "may" implies permission or sometimes uncertainty.

**Do:** "You can configure the dashboard to display real-time analytics."

Use "can" to express ability.

**Avoid:** "You may configure the dashboard to display real-time analytics"

Avoid 'may' when you mean 'can.'

Terms of possibility
^^^^^^^^^^^^^^^^^^^^

These terms can be confusing. When both "may" and "might" are applicable, generally use "might" to avoid confusion with the multiple meanings of "may."

Examples:

**Do:** "You might need additional permissions to access the advanced settings."

Do use 'might' to clarify possibility.

**Avoid:** "You may need additional permissions to access the advanced settings."

Avoid 'may' when 'might' will work.

Inclusive language
------------------

Avoid racial, cultural, or gender bias. Ensure all words are inclusive.

Pronouns
--------

Use the second person (you, your) as often as possible.

Examples:

**Do:** "You can update your profile settings"

**Also do:** "Try refining your search criteria to find the desired results."

Use the first person in headings or labels specific to the User, such as "My preferences" or "My notifications." However, switch to second person in explanatory text, like "Your notifications are updated every hour."

Use the first person (we, our) to refer to the organization when appropriate, such as in requests for personal information where the user benefits from knowing why the information is needed.

Example: "Why do we need your Contact details?"

Active and passive voice
------------------------

The active voice is direct and emphasizes the subject of the sentence. The subject clearly "acts upon" the verb (hence, "active"). For example, "John ate the apple." In situations where either voice will work, generally choose the active voice for more directness.

Examples:

**Do:** Next, the User updates the profile settings.

Use active voice when appropriate.

**Avoid:** Next, the profile settings are updated by the User.

Avoid passive voice when active voice suffices.

The passive voice, however, flips the construction so the subject is secondary to the verb and object. Often, the subject is not included in the sentence. For example, "The campaign was launched by the team" or simply "The campaign was launched." Only sentences with direct objects can be constructed in passive voice, so "The team launched" cannot be passively constructed.

The passive voice can create a more natural tone in certain contexts. For example, if the true subject is a system and the human is secondary, passive voice can be suitable.

Examples:

**Do:** The report needs to be generated.

**Avoid:** Someone needs to generate the report


Action labels
=============

Users depend on consistent labels for common actions to navigate interfaces effectively. Use this list to label actions in Mautic.

A
-

Add
^^^

Takes an existing object and uses it in a new context (for example, adds an item to the cart, adds a User to a group, or adds a document to a folder).

Where appropriate, combine add with the object (for example, Add User or Add role). Compare Create, Insert, New, and Upload.

Apply
^^^^^

Saves changes without closing the dialog. These properties often affect subsequent system behavior.

Use instead of Save changes. Compare Save and Save as.

Approve
^^^^^^^

Indicates the User agrees. In a business process, typically initiates the next step.

Compare Reject.

B
-

Back
^^^^

Returns the User to the previous step in a sequence of steps, such as in a wizard.

Use instead of Previous. Compare Next and Finish.

Browse
^^^^^^

Assists the User in selecting a file (for example, on a button or link next to an entry field). Typically opens a secondary window where the user can locate and select the desired directory and file.

C
-

Cancel
^^^^^^

Stops the current action and closes the dialog.

Warn the User of any possible negative consequences of stopping an action from progressing, such as data corruption. Compare Reset.

Clear
^^^^^

This action clears all the fields or selections. Also deletes the contents of a document, such as a log. Typically the default selection or value is re-established for controls that always have a selection or value, such as radio buttons.

Where appropriate, combine clear with the object (for example, Clear fields or Clear all). Compare Delete and Remove.

Close
^^^^^

Closes the current page or window (for example, closing a secondary window containing online help).

Do not use Close alongside OK or Cancel actions. Compare Cancel and Done.

Copy
^^^^

Creates new instances of the selected objects in a specific destination.

Combine Copy with the object being copied (for example, Copy folder) or the destination (for example, Copy to clipboard) if there are multiple possibilities. Compare New.

Create
^^^^^^

Makes a new object from scratch (for example, creates a calendar event or creates a new document).

In scenarios where the User needs to supply some details or settings as part of the create process, use new to initiate the action and create to apply the user-supplied details or settings to the new object. Compare Add, Copy, Insert, and New.

Customize
^^^^^^^^^

Allow a User to make desired changes.

D
-

Delete
^^^^^^

Destroys an existing object so that it no longer exists (for example, deletes a file from a directory or deletes a value from a table cell).

Where appropriate, combine Delete with the object (for example, Delete column or Delete row). Compare Clear and Remove.

Docs
^^^^

Opens a separate window containing the landing page for the product documentation.

Use as link text only for the specific link that points to the product documentation from the console menu bar. Compare Learn more.

Done
^^^^

Indicates that the User has finished working in an environment (for example, editing templates) and wants to return to where he or she came from.

Compare Close and Finish.

Download
^^^^^^^^

Transfers a file from a remote system to a local system.

Compare Upload.

Drop
^^^^

Use only when referring to dropping a database table.

In other scenarios, use Clear, Delete, or Remove.

E
-

Edit
^^^^

Allows data or values to be changed.

Empty trash
^^^^^^^^^^^

Permanently deletes all files or objects that have been placed into a trash container.

Compare Move to trash.

Export
^^^^^^

Saves data in a different format external to the system. Typically opens a secondary window for the User to specify the file type and destination (for example, storing table data as a set of comma-separated values).

Compare Import.

F
-

Filter
^^^^^^

Shortens a list to objects that match the filter criteria.

Compare Find and Search.

Find
^^^^

Moves the cursor to the next element matching the specified criteria (for example, view the next occurrence of a specific word within an email message).

Compare Filter and Search.

Finish
^^^^^^

Indicates completion of a series of steps, such as in a wizard.

Compare Done.

G
-

Get help
^^^^^^^^

Opens a search field from which the User can search for help information.

Use only as link text on the console menu bar. Compare Docs and Learn more.

H
-

Hide
^^^^

Removes an element that was previously shown (for example, enables the User to hide details or descriptions).

Compare Show.

I
-

Import
^^^^^^

Transforms data or objects from an external source. Typically opens a secondary window for the User to locate the external source.

Context: creating a new table based on comma-separated values contained in a separate file. Compare Export.

Insert
^^^^^^

Adds an element at a particular position in an ordered view.

Context: adding a picture to the body of a document or inserting a record into a table. Compare Add and New

L
-

Launch
^^^^^^

Do not use Launch; use Start.

Learn more
^^^^^^^^^^

Opens additional, highly contextual information. Insert at the end of inline text or hover text where more information follows but doesn't fit in the current context.

If space permits, combine Learn more with meaningful text that describes the content you're pointing to. For example, if your User needs some best practices to manage apps in multiple regions, you could use Learn more about regions.

Log in
^^^^^^

Enters a site or app. This choice typically opens a Form for entry of credentials. Also used on the submission button after Users enter their credentials.

Use instead of Sign in. This is to make it visually distinct from Sign up. These options are often side by side and the different words allow for quick recognition. Compare Log out.

Log out
^^^^^^^

Exits an app or site.

Use instead of Sign out. Compare Log in.

M
-

Move
^^^^

Transfers an object from one container (for example, folder, activity, or page) to another.

Move to trash
^^^^^^^^^^^^^

A soft delete. Moves a file or object to an area from where it can later be permanently deleted or recovered.

Use instead of Delete if it is possible for the User to recover the objects. Compare Empty trash.

N
-

New
^^^

Starts the creation of a new object. New either creates the object immediately or opens a dialog or set of fields where the user can enter properties.

Combine new with the object to create (for example, New User or New column). Compare Add, Copy, Create, Insert, and Save as.

Next
^^^^

Advances the User to the next step in a sequence of steps, such as in a wizard.

Compare Back and Finish.

O
-

OK
^^

Confirms an action or completes the current task.

Best practice is to use a label corresponding to the specific action (for example, Save or Close or Delete). Use OK only when such a label is not available. Write as shown: two letters, both uppercase.

P
-

Play
^^^^

Starts audio, video, or an animation.

.. vale off

Post
^^^^

.. vale on

Adds a new comment to an online community or adds status to a log or record.

If you are editing an existing comment, use Save instead.

Preview
^^^^^^^

Shows how an object or content will appear with formatting applied before the content is published or distributed. Alternatively, provides an incomplete display of an existing object without leaving the current context.

Print
^^^^^

Sends a copy of the currently selected object or the object in view to the printer.

R
-

Redo
^^^^

Redoes an undo action.

Likely used only as a tooltip on an icon button. Compare Undo.

Refresh
^^^^^^^

.. vale off

Reloads the view of an object when the displayed view has become unsynchronized with the source.

.. vale on

Likely used only as a tooltip on an icon button.

Reject
^^^^^^

Indicates the User doesn't approve. In a business process, typically blocks the process from proceeding to the next step.

Compare Approve.

Remove
^^^^^^

Removes an object from the current context but the object is not destroyed as a result of the action (for example, removes a user from a group or removes an item from the cart).

Where appropriate, combine Remove with the object that will be removed (for example, Remove User or Remove role). Compare Clear and Delete.

Reply
^^^^^

Indicates or completes a response to an email or a comment.

Reset
^^^^^

Reverts values back to their last saved state. The last saved state includes the values stored the last time the User clicked Apply. Doesn't close the dialog or window.

Compare Cancel, Restore, Restore defaults, and Undo.

Restore
^^^^^^^

Brings a file back after deletion, corruption, or similar event.

Compare Reset.

Restore all
^^^^^^^^^^^

Completes a restore operation on all files or objects in a given system or container.

Compare Restore.

Restore defaults
^^^^^^^^^^^^^^^^

Sets Form values to the default settings.

Compare Reset and Undo.

Run
^^^

Initiates a procedure.

Use Run instead of Execute.

S
-

Save
^^^^

Saves pending modifications made to a file or document. Doesn't close the window or panel.

Compare Apply.

Save as
^^^^^^^

Creates a new object based on the state of the object currently being viewed. The User names the new object and typically identifies its location.

Search
^^^^^^

Returns all objects (for example, files, names, or documents) within a defined set (for example, in a folder, directory, database, or the internet) that match some specified criteria.

Compare Filter and Find.

Select
^^^^^^

Selects data from a table.

Select all
^^^^^^^^^^

Adds all objects in the view to the selection set or checks all checkboxes.

Compare Clear.

Send
^^^^

Transfers an email or other information to the recipient or destination.

Show
^^^^

Reveals an object that was previously hidden (for example, shows descriptions or shows further details).

Compare Hide.

Sign up
^^^^^^^

Creates a User account or registers a User in a system.

Use instead of Register.

Sort
^^^^

Sorts a list or table column.

Likely used only as a tooltip on an icon button. Can be used without 'ascending' or 'descending' only if the order can be provided to a screen reader in the code for accessibility.

Start
^^^^^

Deploy an app or service to its development or production environment so that it can be used.

Use instead of Launch.

Submit an idea
^^^^^^^^^^^^^^

Opens a separate window containing the IBM Cloud Ideas portal.

Use only as link text on the Support widget from the console menu bar.

T
-

Top
^^^

Returns to the top of the page.

Use instead of Back to top.

U
-

Undo
^^^^

Reverts to the state before the most recent changes made by the User. Repeated use successively reverts to prior states in reverse chronological order. Applies to changes in data and not to changes made to the view.

Not all actions, such as Save, can be undone. Compare Redo, Reset, and Restore.

Update
^^^^^^

Label for a button in a dialog or Form for editing an object. The settings in the dialog are applied to the object when it is updated.

Compare Edit.

Upload
^^^^^^

Transfers a file from a local system to a remote system.

Compare Download.

V
-

View details
^^^^^^^^^^^^

Presents additional information or properties for the object


Quick list
==========

- **Add**: incorporates an existing object into a new context, such as adding a Contact to a Mautic segment.
- **Apply**: saves changes without closing the dialog, affecting future system behavior.
- **Approve**: indicates User agreement, typically moving to the next step in a business process.
- **Back**: returns the User to the previous step, such as in a setup wizard. Use instead of Previous.
- **Browse**: assists in selecting a file, often opening a secondary window for locating and selecting a directory or file.
- **Cancel**: stops the current action and closes the dialog.
- **Clear**: removes all fields or selections, often re-establishing default values for controls like radio buttons. Combine with the object when appropriate, such as Clear fields or Clear all.
- **Close**: closes the current page or window, like closing a secondary window with online help.
- **Copy**: creates new instances of selected objects in a specific destination. Combine with the object being copied or the destination, like Copy to clipboard.
- **Create**: makes a new object from scratch, such as creating a calendar event.
- **Customize**: allows a User to make desired changes.
- **Delete**: destroys an existing object, like deleting a file from a directory. Combine with the object when appropriate, such as Delete column.
- **Docs**: opens a separate window containing the landing page for product documentation.
- **Done**: indicates the User has finished working in an environment and wants to return to the previous location.
- **Download**: transfers a file from a remote system to a local system.
- **Drop**: use when referring to dropping a database table.
- **Edit**: allows data or values to be changed.
- **Empty trash**: permanently deletes all files or objects in a trash container.
- **Export**: saves data in a different format external to the system.
- **Filter**: shortens a list to objects matching the filter criteria.
- **Find**: moves the cursor to the next element matching specified criteria.
- **Finish**: indicates completion of a series of steps, such as in a wizard.
- **Get help**: opens a search field for help information.
- **Hide**: removes an element that was previously shown.
- **Import**: transforms data or objects from an external source.
- **Insert**: adds an element at a particular position in an ordered view.
- **Learn more**: opens additional, highly contextual information.
- **Log in**: enters a site or app, typically opening a Form for credential entry.
- **Log out**: exits an app or site.
- **Move**: transfers an object from one container, such as a folder, activity, or page, to another.
- **Move to trash**: performs a soft delete by moving a file or object to an area where it can be permanently deleted or recovered later.
- **OK**: confirms an action or completes the current task. Use specific labels like Save or Close when available.
- **Play**: starts audio, video, or an animation.
.. vale off
- **Post**: adds a new comment to a community or updates a status log.
.. vale on
- **Preview**: displays how content will appear with formatting before publishing.
- **Save**: saves modifications to a file or document without closing the window.
- **Search**: returns objects matching specified criteria within a defined set, such as a Mautic Contact list.
- **Select**: chooses data from a table.
- **Send**: transfers information to a recipient or destination.
- **Show**: reveals previously hidden objects, like showing additional Contact details in Mautic.
- **Sign up**: creates a User account or registers a User in a system.
- **Sort**: organizes a list or table column, useful for segmenting Contacts in Mautic.
- **Start**: deploys an app or service to its environment for use.
- **Submit an idea**: opens a window for submitting feedback or ideas, used as link text in support widgets.
- **Top**: returns to the top of the page.
- **Undo**: reverts to the state before recent changes, applicable to data changes.
- **Update**: applies settings from a dialog to an object, like ``updatingContact`` preferences in Mautic.
- **Upload**: transfers a file from a local to a remote system