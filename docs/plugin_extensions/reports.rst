.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Reports
#######

To add and render custom Reports in Mautic, your Plugin needs to listen to the following events:

* ``\Mautic\ReportBundle\ReportEvents::REPORT_ON_BUILD``
* ``ReportEvents::REPORT_ON_GENERATE``
* ``ReportEvents::REPORT_ON_GRAPH_GENERATE``

.. code-block:: php

   <?php
   // plugins\HelloWorldBundle\EventListener\ReportSubscriber
   
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

               $event->addGraph('worlds', 'line', 'mautichellobundle.graph.line.visits');
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

.. vale off

Defining a Report
*****************

.. vale on

Mautic dispatches the ``ReportEvents::REPORT_ON_BUILD`` event to define a report. In this event, the Plugin defines:

* The Report context
* Available columns for table data
* Available filters for the table data - defaults to columns
* Available graphs

Column definition
=================

Each column array can include the following properties:

.. list-table::
    :widths: 20 20 60
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``label``
      - string
      - **Required.**
      
        The language string for the column.
    * - ``type``
      - string
      - **Required.**
      
        Column type.
    * - ``alias``
      - string
      - An alias for the returned value. Useful in conjunction with ``formula``.
    * - ``formula``
      - string
      - SQL formula instead of a column. For example, ``SUBSTRING_INDEX(e.type, \'.\', 1)``.
    * - ``link``
      - string
      - Route name to convert the value into a hyperlink. Typically used with the ID of an entity. The route must accept ``objectAction`` and ``objectId`` parameters.

Filter definition
=================

Filters are optional. If you don't define them, the system defaults to using the column definitions. However, filters can provide additional options such as dropdown select lists.

Additional filter keys include:

.. list-table::
    :widths: 20 20 60
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``list``
      - array
      - Used when ``type`` is select for a filter. Provides the dropdown options for a select input. Format should be ``value => label``.
    * - ``operators``
      - array
      - Custom list of operators to allow for this filter.
      
        See the ``OPERATORS`` constant in the :xref:`MauticReportBuilder` class for examples.

.. vale off

Generating the QueryBuilder
===========================

.. vale on

Mautic dispatches the ``ReportEvents::REPORT_ON_GENERATE`` event when it generates and displays a report. Use this event to define the QueryBuilder object that generates the table data.

* Use ``$event->checkContext()`` to determine if the requested report belongs to the subscriber.
* Use Doctrine's DBAL layer QueryBuilder by obtaining it via ``$qb = $event->getQueryBuilder();``.

The ``ReportGeneratorEvent`` class provides several helper functions to append joins for common relationships such as Categories, Contacts, and IP addresses. Refer to the :xref:`Mautic ReportGeneratorEvent` class for more details.

Generating graphs
=================

Mautic dispatches the ``ReportEvents::REPORT_ON_GRAPH_GENERATE`` event to generate graphs for a report. Use this event to define the visual data representation.

* Verify the Report context with ``$event->checkContext()``.
* Clone the base ``QueryBuilder`` to safely manipulate queries for multiple graphs.
* Use the ``LineChart`` and ``ChartQuery`` classes to generate and render graph data.

For supported chart types and options, refer to the ``ChartQuery`` and ``LineChart`` helper classes - located in the :xref:`Mautic CoreBundle Chart Helpers` namespace.


