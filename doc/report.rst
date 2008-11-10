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

Nous avons le plaisir de pouvoir développer ce projet en Python, en alternative à Java initialement spécifié. Tous nos remerciements à Jacques Lemordant pour cette liberté.

Ce document
-----------

Dans la logique *pythoniste* donc, nous avons naturellement choisi le format reStructuredText. Outre l'aisance de son apprentissage, la lisibilité de ses sources, son intégration dans ``vim`` et ses multiples possibilités de publication (HTML, LaTeX, S5, etc.), il bénéficie d'une importante communauté puisqu'il s'agit de format de balisage utilisé pour les ``docstrings`` Python et les JEP.

Formats internes
----------------

Nous avons décidé d'explorer nombre de langages utilisés professionnellement dans un contexte d'interopérabilité. Au-delà de ``XML`` (dont ``RELAX NG``, ``XSLT``/``XPath`` et ``XHTML``) dictés par le cahier des charges du projet, nous avons intégré ``JSON`` et ``Protocol Buffers``.

Assurance qualité
-----------------

Le choix s'est porté sur la réalisation de tests unitaires à l'aide du module ``unittest``.

Interface
---------

Puisque l'ébauche du cahier des charges suggérait un déploiement Web, nous avons anticipé en travaillant directement sur une solution entièrement Web, avec ``web.py`` en raison de sa simplicité et du minimum d'abstractions impliquées.

Performance
-----------

Nous avons, à titre récréatif, intégré le support de ``memcached`` dans le service de géolocalisation.

Construction
------------

La concision et l'extensibilité de ``SCons``, lui-même écrit en Python, nous ont immédiatement poussé à adopter ce système de construction.

Gestion des sources
-------------------

Ce projet fut également l'occasion d'expérimenter avec les méthodologies de développement. Nous avons notamment délégué la gestion des sources à ``git``.

