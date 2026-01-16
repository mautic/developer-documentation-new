Reports
#######

To add and render custom Reports in Mautic, your Plugin needs to listen to three events:

* ``\Mautic\ReportBundle\ReportEvents::REPORT_ON_BUILD``
* ``ReportEvents::REPORT_ON_GENERATE``
* ``ReportEvents::REPORT_ON_GRAPH_GENERATE``

This guide walks you through defining a custom Report, generating Report data, and rendering graphs.

.. vale off

Defining the Report
*******************

.. vale on

Use the ``ReportEvents::REPORT_ON_BUILD`` event to define:

* The Report context
* Available columns
* Available filters - defaults to columns
* Available graphs

Column definition
=================

Each column array can include the following properties:

.. list-table::
    :widths: 15 20 15 50
    :header-rows: 1

    * - Key
      - Required?
      - Type
      - Description
    * - ``label``
      - REQUIRED
      - string
      - The language string for the column.
    * - type
      - REQUIRED
      - string
      - Column type.
    * - alias
      - OPTIONAL
      - string
      - An alias for the returned value. Useful in conjunction with ``formula``.
    * - formula
      - OPTIONAL
      - string
      - SQL formula instead of a column. For example, ``SUBSTRING_INDEX(e.type, \'.\', 1)``.
    * - link
      - OPTIONAL
      - string
      - Route name to convert the value into a hyperlink. Used usually with an ID of an Entity. The route must accept ``objectAction`` and ``objectId`` parameters.

Filter definition
=================

Filters are optional. If you don't define them, the system defaults to using the column definitions. However, filters can provide additional options such as dropdown select lists.

Additional filter keys include:

.. list-table::
    :widths: 15 20 15 50
    :header-rows: 1

    * - Key
      - Required?
      - Type
      - Description
    * - list
      - OPTIONAL
      - array
      - Used when ``type`` is select for a filter. Provides the dropdown options for a select input. Format should be ``value => label``.
    * - operators
      - OPTIONAL
      - array
      - Custom list of operators to allow for this filter. See ``Mautic\ReportBundle\Builder\MauticReportBuilder::OPERATORS`` for an example.

.. vale off

Generate the QueryBuilder
=========================

.. vale on

The system dispatches the ``ReportEvents::REPORT_ON_GENERATE`` event when it needs to generate and display a report. In this function, the plugin defines the QueryBuilder object used to generate the table data.

Use ``$event->checkContext()`` to determine if the requested report is the subscriber's report.

Note that the ``ReportEvents::REPORT_ON_GENERATE`` event should use Doctrine's DBAL layer QueryBuilder obtained via ``$qb = $event->getQueryBuilder();``.

.. vale off

There are a number of helper functions to append joins for commonly used relationships such as category, leads, IP address, and so on. Refer to the ``ReportGeneratorEvent`` class for more details.

.. vale on

Generating graphs
=================

Use the ``ReportEvents::REPORT_ON_GRAPH_GENERATE`` event to render graphs for your report.

* Check the Report context with ``$event->checkContext()``.
* Clone the base ``QueryBuilder`` to manipulate queries safely.
* Use classes like ``LineChart`` and ``ChartQuery`` to generate and render graph data.

For supported chart types and options, refer to the ``ChartQuery`` and ``LineChart`` helper classes in the Mautic codebase.

.. vale off

Example: HelloWorld Report Subscriber
=====================================

.. vale on

Below is an example Plugin file located at ``plugins\HelloWorldBundle\EventListener\ReportSubscriber.php``.

This file subscribes to Report events and provides custom logic for adding new tables, columns, filters, and graphs.

.. code-block:: php

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\CoreBundle\EventListener\CommonSubscriber;
    use Mautic\CoreBundle\Helper\GraphHelper;
    use Mautic\ReportBundle\Event\ReportBuilderEvent;
    use Mautic\ReportBundle\Event\ReportGeneratorEvent;
    use Mautic\ReportBundle\Event\ReportGraphEvent;
    use Mautic\ReportBundle\ReportEvents;
    use Mautic\CoreBundle\Helper\Chart\ChartQuery;
    use Mautic\CoreBundle\Helper\Chart\LineChart;

    class ReportSubscriber extends CommonSubscriber
    {
        public static function getSubscribedEvents()
        {
            return [
                ReportEvents::REPORT_ON_BUILD => ['onReportBuilder', 0],
                ReportEvents::REPORT_ON_GENERATE => ['onReportGenerate', 0],
                ReportEvents::REPORT_ON_GRAPH_GENERATE => ['onReportGraphGenerate', 0],
            ];
        }

        public function onReportBuilder(ReportBuilderEvent $event)
        {
            if ($event->checkContext(['worlds'])) {
                $prefix = 'w.';
                $columns = [
                    $prefix . 'visit_count' => [
                        'label' => 'mautic.hellobundle.report.visit_count',
                        'type' => 'int',
                    ],
                    $prefix . 'world' => [
                        'label' => 'mautic.hellobundle.report.world',
                        'type' => 'text',
                    ],
                ];

                $columns = $filters = array_merge(
                    $columns,
                    $event->getStandardColumns($prefix),
                    $event->getCategoryColumns()
                );

                $filters[$prefix . 'world']['type'] = 'select';
                $filters[$prefix . 'world']['list'] = [
                    'earth' => 'Earth',
                    'mars' => 'Mars',
                ];

                $event->addTable('worlds', [
                    'display_name' => 'mautic.helloworld.worlds',
                    'columns' => $columns,
                    'filters' => $filters,
                ]);

                $event->addGraph('worlds', 'line', 'mautic.hellobundle.graph.line.visits');
            }
        }

        public function onReportGenerate(ReportGeneratorEvent $event)
        {
            $context = $event->getContext();
            if ($context == 'worlds') {
                $qb = $event->getQueryBuilder();
                $qb->from(MAUTIC_TABLE_PREFIX . 'worlds', 'w');
                $event->addCategoryLeftJoin($qb, 'w');
                $event->setQueryBuilder($qb);
            }
        }

        public function onReportGraphGenerate(ReportGraphEvent $event)
        {
            if (!$event->checkContext('worlds')) {
                return;
            }

            $graphs = $event->getRequestedGraphs();
            $qb = $event->getQueryBuilder();

            foreach ($graphs as $graph) {
                $queryBuilder = clone $qb;
                $options = $event->getOptions($graph);
                $chartQuery = clone $options['chartQuery'];
                $chartQuery->applyDateFilters($queryBuilder, 'date_added', 'v');

                switch ($graph) {
                    case 'mautic.hellobundle.graph.line.visits':
                        $chart = new LineChart(null, $options['dateFrom'], $options['dateTo']);
                        $chartQuery->modifyTimeDataQuery($queryBuilder, 'date_added', 'v');
                        $visits = $chartQuery->loadAndBuildTimeData($queryBuilder);
                        $chart->setDataset(
                            $options['translator']->trans('mautic.hellobundle.graph.line.visits'),
                            $visits
                        );
                        $data = $chart->render();
                        $data['name'] = $graph;
                        $data['iconClass'] = 'fa-tachometer';
                        $event->setGraph($graph, $data);
                        break;
                }
            }
        }
    }
