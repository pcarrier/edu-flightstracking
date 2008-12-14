========================
flighttracking en Python
========================

-------------------------------------------------------------------------------
Projet de MSI L3 MIAGE 2008-2009, Jean-Christophe Saad-Dupuy & Geoffroy Carrier
-------------------------------------------------------------------------------

.. sectnum::
.. contents:: Index

Choix technologiques
====================

Python
------

Nous avons eu le plaisir de pouvoir développer ce projet en Python, en alternative à Java initialement spécifié. Tous nos remerciements à Jacques Lemordant pour cette liberté.

Ce document
-----------

Dans la logique *pythoniste* donc, nous avons naturellement choisi le format reStructuredText. Outre l'aisance de son apprentissage, la lisibilité de ses sources, son intégration dans ``vim`` et ses multiples possibilités de publication (HTML, LaTeX, S5, etc.), il bénéficie d'une importante communauté puisqu'il s'agit de format de balisage utilisé pour les ``docstrings`` Python et les JEP.

Formats internes
----------------

Technologies ``W3C`` : ``XML`` (dont ``RELAX NG``, ``XSLT``/``XPath`` et ``XHTML``), CSS, ECMAScript.

Assurance qualité
-----------------

Réalisation de tests unitaires à l'aide du module ``unittest``.

Interface
---------

Puisque l'ébauche du cahier des charges suggérait un déploiement Web, nous avons anticipé en travaillant directement sur une solution entièrement Web, avec ``web.py`` en raison de sa simplicité et du minimum d'abstractions impliquées. De plus, nous avons très largement utilisé la librairie ``prototype`` pour simplifier les interactions avec le ``DOM``. Les tests n'ont été effectués que sous Firefox et Midori, Internet Explorer est probablement très mal pris en charge.

Performance
-----------

Nous avons, à titre récréatif, intégré le support de ``memcached`` dans le service de géolocalisation.

Gestion des sources
-------------------

Ce projet fut également l'occasion d'expérimenter avec les méthodologies de développement. Nous avons notamment délégué la gestion des sources à ``git``.


Etablissement du format XML
----------------------------
Notre premier travail fût d'établir un format XML cohérent avec la représeantation
des données voulues.

Etablissement du schéma RELAX-NG
--------------------------------

Geocodage des aéroports :
-------------------------
Nous avons développé un programme d'essais permettant de géocoder les   
noeuds de type **location**
