.. |google| image:: google.png

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

Puisque l'ébauche du cahier des charges suggérait un déploiement Web, nous avons anticipé en travaillant directement sur une solution entièrement Web, avec ``web.py`` en raison de sa simplicité et du minimum d'abstractions impliquées. De plus, nous avons très largement utilisé la librairie ``prototype`` pour simplifier les interactions avec le ``DOM``. Les tests n'ont été effectués que sous Firefox et Midori (WebKit), Internet Explorer est probablement très mal pris en charge.


Gestion des sources
-------------------

Ce projet fut également l'occasion d'expérimenter avec les méthodologies de développement. Nous avons notamment délégué la gestion des sources à ``git``.


Établissement du format XML
----------------------------

Notre premier travail fût d'établir un format XML cohérent avec la représentation des données voulues.
D'après l'énoncé et le site nous avons établi le document XML suivant :

Établissement du schéma RELAX-NG
--------------------------------

Nous avons par la suite développé le diagramme relax-ng **tracking.rng**, situé dans le répertoire ``rng/``.

Représentation objet de notre document XML
------------------------------------------

Nous avons développé des classes ``python`` ayant en charge toutes les opérations sur le document XML.

La classe principale est la classe FlightTracking. Elle contient deux objets permettant d'effectuer les
opérations sur les vols et les localisations.

Ces deux objets contiennent des listes d'objets **flight** et **location**, indexés par leur nom.

Nous avons choisi d'implémenter des méthodes d'ajout et de suppression, afin de garder une cohérence
sur l'indexation de ces objets lors d'un changement de nom. L'édition dans l'interface Web n'a pas
été implémentée faute de temps.

La classe **FlightTracking** contient la méthode **geocode** qui fait appel à l'interface
au webservice de géocodage de |google| située dans le module **service**.

Le diagramme UML de ces classes est donné ci-dessous :

.. image:: flighttracking.png


Geocodage des aéroports :
-------------------------
Nous avons développé un programme d'essais permettant de géocoder les noeuds de type **location**

Appelé **demo_geocoder**, il effectue des opérations simples :

#. Chargement du fichier XML en mémoire ;
#. Geocodage et ajout d'un noeud **coordinates** pour chaque noeud **location** ;
#. Sauvegarde dans un fichier.

Transformation en KML
---------------------


Programmes intermédiaires.
--------------------------
Comme demandé dans l'énnoncé, nous avons au cour de notre développement crées de simples scripts utilisants
la librairie python ``lxml`` afin d'appliquer  le geocodage et d'appliquer le fichier **xsl** décrit plus haut.
Ces deux scripts sont situés dans le répertoire 

