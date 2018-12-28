.. . Kicking page rebuild 2014-10-30 17:00:08
.. include:: defs.hrst

.. index:: Tender, Auction
.. _tender:

Tender
======

Schema
------

:title:
   string, multilingual

   Additionally in :ref:`openeu`, :ref:`esco` and :ref:`competitivedialogue` (stage2_EU):

       uk (title) and en (title_en) translations are required

   The name of the tender, displayed in listings. You can include the following items:

   * tender code (in procuring organization management system)
   * periodicity of the tender (annual, quarterly, etc.)
   * item being procured
   * some other info

:description:
   string, multilingual

   Detailed description of tender.

:tenderID:
   string, auto-generated, read-only

   The tender identifier to refer tender to in "paper" documentation. 

   |ocdsDescription|
   TenderID should always be the same as the OCID. It is included to make the flattened data structure more convenient.

:procuringEntity:
   :ref:`ProcuringEntity`, required

   Organization conducting the tender.

   |ocdsDescription|
   The entity managing the procurement, which may be different from the buyer who is paying / using the items being procured.

   If :code:`procurementMethodType` is :code:`negotiation` or :code:`negotiation.quick`, then possible values of :code:`ProcuringEntity.kind` are limited to :code:`['general', 'special', 'defense']`.

:procurementMethod:
    string, auto-generated

    :`limited`:

    Procurement Method of the Tender.

    Only in :ref:`limited`


:procurementMethodType:
    string

    :`aboveThresholdUA`:
        above threshold procedure indentifier

    :`aboveThresholdEU`:
        above threshold EU procedure indentifier

    :`aboveThresholdUA.defense`:
        defense procedure indentifier

    :`reporting`:
        reporting procedure indentifier

    :`negotiation`:
        negotiation procedure indentifier

    :`negotiation.quick`:
        negotiation.quick procedure indentifier

    :`esco`:
        esco procedure indentifier

    Possible values in :ref:`competitivedialogue` stage1:

    :`competitiveDialogueEU`:

    :`competitiveDialogueUA`:

    Possible values in :ref:`competitivedialogue` stage2:

    :`competitiveDialogueEU.stage2`:

    :`competitiveDialogueUA.stage2`:


:value:
   :ref:`value`, required

   Total available tender budget. Bids greater then ``value`` will be rejected.

   |ocdsDescription|
   The total estimated value of the procurement.

   Absent in :ref:`esco`

:guarantee:
    :ref:`Guarantee`

    Bid guarantee

:date:
    string, :ref:`date`, auto-generated
    
:items:
   list of :ref:`item` objects, required

   List that contains single item being procured. 

   |ocdsDescription|
   The goods and services to be purchased, broken into line items wherever possible. Items should not be duplicated, but a quantity of 2 specified instead.

:features:
   list of :ref:`Feature` objects

   Features of tender.

:documents:
   List of :ref:`document` objects
 
   |ocdsDescription|
   All documents and attachments related to the tender.

:questions:
   List of :ref:`question` objects

   Questions to ``procuringEntity`` and answers to them.

:complaints:
   List of :ref:`complaint` objects

   Complaints to tender conditions and their resolutions.

:bids:
   List of :ref:`bid` objects

   A list of all bids placed in the tender with information about tenderers, their proposal and other qualification documentation.

   |ocdsDescription|
   A list of all the companies who entered submissions for the tender.

:minimalStep:
   :ref:`value`, required

   The minimal step of auction (reduction). Validation rules:

   * `amount` should be less then `Tender.value.amount`
   * `currency` should either be absent or match `Tender.value.currency`
   * `valueAddedTaxIncluded` should either be absent or match `Tender.value.valueAddedTaxIncluded`

    Absent in :ref:`esco`

:awards:
    List of :ref:`award` objects

    All qualifications (disqualifications and awards).

:contracts:
    List of :ref:`Contract` objects

:enquiryPeriod:
   :ref:`period`, required

   Period when questions are allowed. At least `endDate` has to be provided.

   |ocdsDescription|
   The period during which enquiries may be made and will be answered.

   Additionally in :ref:`defense`, :ref:`openua` and :ref:`openeu`:
      `enquiryPeriod` has additional fields:

      * ``invalidationDate`` - date of the last tender conditions modification, when all bid proposals became `invalid`. Broker (eMall) should take action in order for bids to be activated or re-submitted.

      * ``clarificationsUntil`` - time before which answers for questions and claims can be provided. After this time the procedure will be blocked.

:dateModified:
    string, :ref:`date`, auto-generated

:owner:
    string, auto-generated

:tenderPeriod:
   :ref:`period`, required

   Period when bids can be submitted. At least `endDate` has to be provided.

   |ocdsDescription|
   The period when the tender is open for submissions. The end date is the closing date for tender submissions.

:qualificationPeriod:
   :ref:`period`, read-only

   This period consists of qualification and 10 days of stand still period.

   |ocdsDescription|
   Period when qualification can be submitted with stand still period.

   Only in :ref:`openeu`, :ref:`esco` and :ref:`competitivedialogue`

:auctionPeriod:
   :ref:`period`, read-only

   Period when Auction is conducted.

:auctionUrl:
    url

    A web address for view auction.

:awardPeriod:
   :ref:`period`, read-only

   Awarding process period.

   |ocdsDescription|
   The date or period on which an award is anticipated to be made.

:mainProcurementCategory:
   string

   :`goods`:
       The primary object of this tender involves physical or electronic goods or supplies.

   :`services`:
       The primary object of this tender involves construction, repair, rehabilitation, demolition, restoration or maintenance of some asset or infrastructure.

   :`works`:
       The primary object of this tender involves professional services of some form, generally contracted for on the basis of measurable outputs or deliverables.

   |ocdsDescription|
   The primary category describing the main object of the tender.

:milestones:

   List of :ref:`Milestone` objects.

:status:
   string

   :`active.enquiries`:
       Enquiries period (enquiries)
   :`active.tendering`:
       Tendering period (tendering)
   :`active.auction`:
       Auction period (auction)
   :`active.qualification`:
       Winner qualification (qualification)
   :`active.awarded`:
       Standstill period (standstill)
   :`unsuccessful`:
       Unsuccessful tender (unsuccessful)
   :`complete`:
       Complete tender (complete)
   :`cancelled`:
       Cancelled tender (cancelled)

   Status of the Tender.

   Different in :ref:`defense`, :ref:`openua` and and :ref:`competitivedialogue` (UA):

   :`active.tendering`:
       Tendering period (tendering)
   :`active.auction`:
       Auction period (auction)
   :`active.qualification`:
       Winner qualification (qualification)
   :`active.awarded`:
       Standstill period (standstill)
   :`unsuccessful`:
       Unsuccessful tender (unsuccessful)
   :`complete`:
       Complete tender (complete)
   :`cancelled`:
       Cancelled tender (cancelled)

   Different in :ref:`limited`:

   :`active`:
       Active tender (default)
   :`complete`:
       Completed tender
   :`cancelled`:
       Cancelled tender
   :`unsuccessful`:
       Unsuccessful tender

   Different in :ref:`openeu`, :ref:`esco` and :ref:`competitivedialogue` (EU):

   :`active.tendering`:
       Enquiries and tendering period
   :`active.pre-qualification`:
       Pre qulification period
   :`active.pre-qualification.stand-still`:
       Standstill before auction
   :`active.auction`:
       Auction period (auction)
   :`active.qualification`:
       Winner qualification (qualification)
   :`active.awarded`:
       Standstill period (standstill)
   :`complete`:
       Complete tender (complete)
   :`unsuccessful`:
       Unsuccessful tender (unsuccessful)
   :`cancelled`:
       Cancelled tender (cancelled)

:lots:
   List of :ref:`lot` objects.

   Contains all tender lots.

   In :ref:`limited`: Only if `tender.procurementMethodType` is `negotiation` or `negotiation.quick`.

:qualifications:

   List of :ref:`Qualification` objects.

   Contains all tender qualifications.

   Only in :ref:`openeu` and :ref:`competitivedialogue`

:cancellations:
   List of :ref:`cancellation` objects.

   Contains 1 object with `active` status in case of cancelled Tender.

   The :ref:`cancellation` object describes the reason of tender cancellation contains accompanying
   documents  if any.

:funders:
  List of :ref:`organization` objects.

  Optional field.

  The funder is an entity providing money or finance for contracting process.

:revisions:
   List of :ref:`revision` objects, auto-generated

   Historical changes to Tender object properties.


:cause:
    string, required for **negotiation** procedure/ optional for **negotiation.quick** procedure

    Causes for using negotiation or negotiation.quick procedures. For more details see Article 35 of the Law of Ukraine "On Public Procurement".

    Possible values for **negotiation** and **negotiation.quick** procedures:

        * `artContestIP` Purchase of art or intellectual property

        * `noCompetition` Lack of competition

        * `twiceUnsuccessful` Two tenders have already been cancelled due to lack of participants

        * `additionalPurchase` Need to use the same supplier for unification, standardization, etc.

        * `additionalConstruction` Need of additional construction works

        * `stateLegalServices` Purchase of legal services connected with protection of rights and interests of Ukraine

    Possible values for **negotiation.quick** procedure:

        * `quick` Procurement is urgent

    Only in :ref:`limited`

:causeDescription:
    string, multilingual, required for **negotiation** and **negotiation.quick** procedures

    Reasoning behind usage of negotiation or negotiation.quick procedures.

    Only in :ref:`limited`

:stage2TenderID:
   string, auto-generated, read-only

   The tender identifier on second stage

   Only in :ref:`competitivedialogue` stage1

:shortlistedFirms:

    :ref:`shortlistedFirms`, auto-generated, read-only

    |ocdsDescription|
    List of firm which can register bid on tender

    Only in :ref:`competitivedialogue` stage2

Additionally in :ref:`esco`:

:NBUdiscountRate:
    float, required

    NBU Discount Rate as of tender notice publication date. Possible values: from 0 to 0.99 (from 0% to 99% respectively), with 3-digit precision after comma (e.g. 00.000). NBUdiscountRate change is interpreted as a change of tender conditions.


:minimalStepPercentage:
   :ref:`value`, Float, required.

   Minimum step increment of the energy service contract performance indicator during auction that is calculated from  participant’s bid.
   Possible values: from 0.005 to 0.03 (from 0.5% to 3%), with 3-digit precision after comma.

:fundingKind:
    string, required.

    Tender funding source. Possible values:
        * budget -  Budget funding.
        * other - exclusively supplier’s funding.

    Default value: other

:yearlyPaymentsPercentageRange:
    float, required

    Fixed percentage of participant's cost reduction sum, with 3-digit precision after comma.
    Possible values:

        * from 0.8 to 1 (from 80% to 100% respectively) if tender:fundingKind:other.
        * from 0 to x, where x can vary from 0 to 0.8 (from 0% to x% respectively) if tender:fundingKind:budget.

:noticePublicationDate:
    string, :ref:`date`

    Read-only, autogenerated.

    Date of tender announcement.


.. important::

    The Tender dates should be sequential:

        * Current time
        * `enquiryPeriod.startDate`
        * `enquiryPeriod.endDate`
        * `tenderPeriod.startDate`
        * `tenderPeriod.endDate`


Tender workflow :ref:`limited`
--------------------------------

.. graphviz::

    digraph G {
        A [ label="active*" ]
        B [ label="complete"]
        C [ label="cancelled"]
         A -> B;
         A -> C;
    }

\* marks initial state