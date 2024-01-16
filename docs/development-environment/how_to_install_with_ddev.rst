How to install Mautic with DDEV
###############################

.. note:: 
    If you get stuck, join the lively Mautic Community on :xref:`Mautic Slack` or the :xref:`Developer Forum` for support and answers. **Please first post in the forum**, then share the link in Slack, so others can learn from your question.

Pre-requisites with DDEV
========================
1. You should have DDEV and Docker or Colima installed on your machine. If not, please follow the instructions here: :xref:`ddev install`

Installing Mautic is a two-step process:
========================================
1. Clone this repository

.. code-block:: bash

    git clone https://github.com/mautic/mautic.git

.. Note:: Clone the repository in the directory where you want to install Mautic.

1. Install Mautic running DDEV.

.. code-block:: bash

    cd mautic
    ddev start

.. list-table:: Users and passwords
    :header-rows: 1

    * - Username
      - Password
    * - ``admin``
      - ``Maut1cR0cks!``
    * - ``sales``
      - ``Maut1cR0cks!``

.. Note:: Versions of Mautic prior to 5.1 use the password ``mautic``
