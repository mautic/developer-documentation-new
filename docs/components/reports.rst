Reports
#######
To add and render custom reports in Mautic, your plugin needs to listen to three events:

- ``\Mautic\ReportBundle\ReportEvents::REPORT_ON_BUILD``
- ``ReportEvents::REPORT_ON_GENERATE``
- ``ReportEvents::REPORT_ON_GRAPH_GENERATE``

This guide walks you through defining a custom report, generating report data, and rendering graphs.

Defining the Report
-------------------

Use the ``ReportEvents::REPORT_ON_BUILD`` event to define:

- The report context
- Available columns
- Available filters (defaults to columns)
- Available graphs

Column Definition
-----------------

Each column array can include the following properties:

+-------------+-----------+--------+---------------------------------------------------------------+
| Key         | Required? | Type   | Description                                                   |
+=============+===========+========+===============================================================+
| ``label``   | Yes       | string | The language string for the column                            |
+-------------+-----------+--------+---------------------------------------------------------------+
| ``type``    | Yes       | string | Column data type (e.g. ``int``, ``text``)                     |
+-------------+-----------+--------+---------------------------------------------------------------+
| ``alias``   | No        | string | Alias for the returned value, useful with SQL formulas        |
+-------------+-----------+--------+---------------------------------------------------------------+
| ``formula`` | No        | string | SQL formula instead of a column (e.g. ``SUBSTRING_INDEX(...)``) |
+-------------+-----------+--------+---------------------------------------------------------------+
| ``link``    | No        | string | Route name to turn value into a hyperlink                     |
+-------------+-----------+--------+---------------------------------------------------------------+

Filter Definition
-----------------

Filters are optional. If not defined, Mautic will default to using the column definitions. However, filters can provide additional options such as dropdown select lists.

Additional filter keys include:

+-------------+-----------+--------+-------------------------------------------------------------+
| Key         | Required? | Type   | Description                                                 |
+=============+===========+========+=============================================================+
| ``list``    | No        | array  | Dropdown options when type is ``select`` (e.g. ``earth`` => ``Earth``) |
+-------------+-----------+--------+-------------------------------------------------------------+
| ``operators`` | No      | array  | Custom list of allowed filter operators                     |
+-------------+-----------+--------+-------------------------------------------------------------+

Generating the QueryBuilder
---------------------------

Use the ``ReportEvents::REPORT_ON_GENERATE`` event to define how the report data is retrieved.

- Use ``$event->checkContext()`` to check if the report belongs to this subscriber.
- Use Doctrine's DBAL QueryBuilder via ``$event->getQueryBuilder()``.
- Join commonly used relationships using helper methods like ``addCategoryLeftJoin()``.

Generating Graphs
-----------------

Use the ``ReportEvents::REPORT_ON_GRAPH_GENERATE`` event to render graphs for your report.

- Check the report context with ``$event->checkContext()``.
- Clone the base ``QueryBuilder`` to manipulate queries safely.
- Use classes like ``LineChart`` and ``ChartQuery`` to generate and render graph data.

For supported chart types and options, refer to the ``ChartQuery`` and ``LineChart`` helper classes in the Mautic codebase.

Example: HelloWorld Report Subscriber
-------------------------------------

Below is an example plugin file located at::

    plugins\HelloWorldBundle\EventListener\ReportSubscriber.php

This file subscribes to report events and provides custom logic for adding new tables, columns, filters, and graphs.

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

