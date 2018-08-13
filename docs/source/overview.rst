Overview
========

The Open Procurement Open UA procedure is plugin to `Open Procurement API
<http://api-docs.openprocurement.org/>`_ software.  It requires 0.12 version
of `openprocurement.api package
<https://github.com/openprocurement/openprocurement.api>`_ to work.

REST-ful interface to plugin is in line with core software design principles. 


Conventions
-----------

This plugin conventions follow the `Open Procurement API conventions
<http://api-docs.openprocurement.org/en/latest/overview.html#conventions>`_.

Main responsibilities
---------------------

Open Procurement Open UA procedure is dedicated to Open Tender procedure for
Ukrainian above threshold procurements.  The code for that type of procedure
is `aboveThresholdUA`.

Business logic
--------------

The approach to Open UA procedure is different from core Open Procurement API
procedure (that is used for below threshold procurements) mainly in
:ref:`stage that precedes <tendering>` auction.  Differences are in the
following aspects:

1) Tender can be edited through the whole tenderPeriod (while in
   active.tendering state), but any edit that is close to
   tenderPeriod.endDate would require extending that period.

2) There is no dedicated active.enguiries state. 

3) Questions can be asked within enquiryPeriod that is based upon
   tenderPeriod.

4) Answers are provided during the whole tenderPeriod.

5) Bids can be placed during the whole tenderPeriod.

6) Placed bids are invalidated after any tender condition editing and have to
   be re-confirmed.
   
Project status
--------------

The project is in active development and has pilot installations.

The source repository for this project is on GitHub: https://github.com/openprocurement/openprocurement.tender.openua

You can leave feedback by raising a new issue on the `issue tracker
<https://github.com/openprocurement/openprocurement.tender.openua/issues>`_ (GitHub
registration necessary).  For general discussion use `Open Procurement
General <https://groups.google.com/group/open-procurement-general>`_ maillist.


Documentation of related packages
---------------------------------

* `OpenProcurement API <http://api-docs.openprocurement.org/en/latest/>`_

* `Open tender procedure with publication in English (OpenEU) <http://openeu.api-docs.openprocurement.org/en/latest/>`_

* `Reporting, negotiation procurement procedure and negotiation procedure for the urgent need  <http://limited.api-docs.openprocurement.org/en/latest/>`_

* `Defense open tender <http://defense.api-docs.openprocurement.org/en/latest/>`_

* `Contracting API interface to OpenProcurement database <http://contracting.api-docs.openprocurement.org/en/latest/>`_


API stability
-------------
API is highly unstable, and while API endpoints are expected to remain
relatively stable the data exchange formats are expected to be changed a
lot.  The changes in the API are communicated via `Open Procurement API
maillist <https://groups.google.com/group/open-procurement-api>`_.

Change log
----------

0.2
~~~
Released: unreleased

 New features:

 - Above Threshold :ref:`Complaint workflow <complaint_workflow>`

 Modifications:

0.1
~~~

Released: 2016-01-25

 New features:

 - no `active.enquiries` status
 - Bid invalidation
 - Open Tender UA validation rules

Next steps
----------
You might find it helpful to look at the :ref:`tutorial`, or the
:ref:`reference`.
