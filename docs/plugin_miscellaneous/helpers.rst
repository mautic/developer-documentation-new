Helpers
#######

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Mautic ships many helper classes. The most commonly used ones appear below.

.. vale off

ChartQuery and Graphs
*********************

.. vale on

Several classes help generate chart data:

.. code-block:: php

    <?php

    use Mautic\CoreBundle\Helper\Chart\ChartQuery;
    use Mautic\CoreBundle\Helper\Chart\LineChart;

    $chart = new LineChart($unit, $dateFrom, $dateTo, $dateFormat);
    $query = new ChartQuery($this->entityManager->getConnection(), $dateFrom, $dateTo);
    $q     = $query->prepareTimeDataQuery('lead_points_change_log', 'date_added', $filter);
    $data  = $query->loadAndBuildTimeData($q);
    $chart->setDataset($this->translator->trans('mautic.point.changes'), $data);
    $data  = $chart->render();

``ChartQuery`` retrieves chart data from the database. Instantiate it with the Doctrine connection and the ``DateTime`` from and to dates. It guesses the time unit - hours, days, weeks, months, or years - from the range, or you can force a unit by passing it as the fourth argument - ``H``, ``d``, ``W``, ``m``, or ``Y``. It also fills in any missing items so the data displays correctly in a line chart.

``LineChart`` displays date and time data with time on the horizontal axis and values on the vertical axis, and it can hold multiple datasets. Instantiate it with a unit - ``null`` to guess - a from date, a to date, and a date format - ``null`` to generate one automatically. Add a dataset with ``setDataset($label, $data)``, where ``$data`` comes from ``ChartQuery``. Mautic generates the color of each dataset automatically. Call ``render()`` to get the data prepared for the frontend.

Instantiate ``PieChart`` with ``new PieChart()``. Add a dataset with ``setDataset($label, $value)``, then call ``render()``.

``BarChart`` displays variants of the same value, with the variants on the horizontal axis. Instantiate it with ``new BarChart($labels)``, where ``$labels`` lists the variants. Add a dataset with ``setDataset($label, $data, $order)``, then call ``render()``.

On the frontend, render the prepared chart template and pass in the chart data, the chart type - ``line``, ``bar``, or ``pie`` - and the chart height. The width is responsive.

.. vale off

DateTime
********

.. vale on

Use ``Mautic\CoreBundle\Helper\DateTimeHelper`` to convert between Coordinated Universal Time and the local timezone:

.. code-block:: php

    <?php

    $dtHelper  = new \Mautic\CoreBundle\Helper\DateTimeHelper('2015-07-20 21:39:00', 'Y-m-d H:i:s', 'local');
    $utcString = $dtHelper->toUtcString();

Refer to the class for its other conversion methods.

.. vale off

Input
*****

.. vale on

Use ``Mautic\CoreBundle\Helper\InputHelper`` to sanitize submitted input into clean strings:

.. code-block:: php

    <?php

    use Mautic\CoreBundle\Helper\InputHelper;

    // ...
    $clean = InputHelper::clean($input);
    $clean = InputHelper::int($input);
    $clean = InputHelper::alphanum($input);
    $clean = InputHelper::html($input);

Refer to the class for its other cleaning methods.
