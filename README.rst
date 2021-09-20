=======================================================
Point of Sale Require Customer / CLIMBING GYM EXTENSION
=======================================================

ADDED NEW FUNCTIONALITY
-----------------------

* check membership
* check membership status


This module was written to extend the functionality of odoo pos
and allows you to require a customer for each pos order.  In the
pos session configuration, you can choose to require the customer for pos
orders.

If a customer is not selected, the pos ui will display an error message.
In the backend the customer field is required when needed.

Two new options are available:

* Customer 'Required before starting the order';
* Customer 'Required before paying';

'Required before starting the order' Option
-------------------------------------------
In the frontend PoS, the default screen is the screen to select customers.

* Users are not allowed to start selling before having selected a customer;
* Users can not 'deselect a customer', only select an other one;

'Required before paying' Option
-------------------------------
In the frontend PoS, the user can start selling, but if the user tries to
make payment and if a customer is not selected, the pos ui will display an
error message.


.. image:: https://raw.githubusercontent.com/pos_customer_required/static/description/frontend_pos_error_message.png

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure this module, you need to:

* go to point of sale -> configuration -> point of sales
* select the point of sales you want configure
* search for the "Require Customer" and choose between the following values:
    * 'Optional'; (this module has no effect on this PoS config)
    * 'Required before paying';
    * 'Required before starting the order';

Usage
=====

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/184/9.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/pos/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/OCA/pos/issues/new?body=module:%20pos_customer_required%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Apertoso NV
* La Louve

Contributors
~~~~~~~~~~~~

* Jos De Graeve <Jos.DeGraeve@apertoso.be>
* Sylvain LE GAL <https://twitter.com/legalsylvain>
* Pedro M. Baeza  <pedro.baeza@gmail.com> ( reviews & feedback )
* Druidoo <https://www.druidoo.io>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/pos <https://github.com/OCA/pos/tree/12.0/pos_customer_required>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
