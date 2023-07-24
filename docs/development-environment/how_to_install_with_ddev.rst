How to install Mautic with DDEV
###############################

Pre-requisites with DDEV
========================
1. You should have DDEV installed on your machine. If not, please follow the instructions here: https://ddev.readthedocs.io/en/stable/#installation

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

.. Note:: When asked if you want to install Mautic, choose yes.

.. list-table:: Users and passwords
    :header-rows: 1

    * - Username
      - Password
    * - ``admin``
      - ``mautic``
    * - ``sales``
      - ``mautic``

