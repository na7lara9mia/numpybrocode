# Abaque de chiffrage — Plateforme Microsoft Fabric, SAP S/4HANA vers Bronze

**Unité :** jours-personnes (j.p.). Estimations indicatives à confirmer après cadrage des extractions SAP et des contraintes d'accès.

## Scénario 1 — Plateforme et première alimentation Bronze

**Hypothèse :** premier lot de 5 objets SAP S/4HANA ; chargement initial puis incrémental.

| Lot | Périmètre | Estimation |
|---|---|---:|
| Cadrage technique | Objets SAP, volumétrie, fréquence, mode d'extraction, critères de recette | 3–5 j.p. |
| Technical foundation | Workspaces, capacité, identités, accès, réseau, Git et déploiement | 8–15 j.p. |
| Socle Bronze | Lakehouse, conventions, journalisation, paramètres, erreurs et relance | 6–10 j.p. |
| Connexion SAP S/4 | Accès, mécanisme d'extraction, connectivité et performance | 5–12 j.p. |
| Premier objet | Chargement initial, incrémental, contrôles et recette | 4–7 j.p. |
| Objets suivants | Configuration, adaptation et recette | 1–3 j.p./objet |
| Documentation et transfert | Exploitation, procédures et passation | 2–4 j.p. |

**Total pour 5 objets : 32–65 j.p.** Avec une provision de 10–15 % pour pilotage et aléas : **environ 36–75 j.p.**

## Scénario 2 — Plateforme industrialisée pilotée par métadonnées

**Hypothèse :** environnements DEV/TEST/PROD ; une source SAP S/4HANA ; ingestion Bronze initiale et incrémentale ; framework réutilisable.

| Lot | Périmètre | Estimation |
|---|---|---:|
| Cadrage et conception | Contrat d'extraction SAP, volumétrie, incrément, architecture, exploitation | 8–12 j.p. |
| Technical foundation | Workspaces, identités, accès, réseau, Git, CI/CD et promotion entre environnements | 15–25 j.p. |
| Framework de métadonnées | Schedules → Batches → Phases → Tasks → Entities, paramètres, dépendances, versionnement | 15–25 j.p. |
| Moteur d'orchestration | Exécution pilotée par métadonnées, parallélisme, reprises, rejets, journaux et alertes | 20–35 j.p. |
| Framework d'ingestion Bronze | Chargement initial et incrémental, Delta, traçabilité, contrôles techniques et rejeu | 15–25 j.p. |
| Intégration SAP S/4 | Connectivité, authentification, extraction et tests de performance | 10–20 j.p. |
| Tests et mise en exploitation | Intégration, recette, documentation, runbook et transfert | 12–20 j.p. |
| **Socle industrialisé** | **Avant déploiement des objets SAP** | **95–162 j.p.** |

**Déploiement par objet SAP :** 3–6 j.p. pour un objet standard ; 7–12 j.p. si l'extraction nécessite une logique particulière.

**Exemple pour 20 objets standards : 155–282 j.p.** Avec une provision de 10–15 % : **environ 171–324 j.p.**

## Points à valider avant engagement

- Disponibilité du mécanisme d'extraction SAP et responsabilité des éventuels développements côté SAP.
- Accès réseau et sécurité entre Fabric et SAP.
- Clés, colonnes d'incrément, gestion des suppressions et volumétrie par objet.
- Performance du chargement initial et fenêtres d'extraction autorisées.

Un **objet pilote** permet de mesurer ces facteurs avant de figer le coût par objet. Les deux scénarios s'arrêtent à **Bronze** : Silver, Gold, modèles sémantiques et licences/capacité Fabric sont hors périmètre.


## Répartition de la charge par rôle

**Lecture :** les fourchettes par rôle s'additionnent ligne par ligne ; elles représentent une charge, et non une durée calendaire ni une affectation à plein temps.

### Scénario 1 — 5 objets SAP

| Lot | Architecte | Tech lead | Data engineer(s) | Total |
|---|---:|---:|---:|---:|
| Cadrage technique | 2–3 | 1–2 | 0 | 3–5 |
| Technical foundation | 2–3 | 4–7 | 2–5 | 8–15 |
| Socle Bronze | 1–1 | 3–5 | 2–4 | 6–10 |
| Connexion SAP S/4 | 1–2 | 2–4 | 2–6 | 5–12 |
| Premier objet | 0 | 1–2 | 3–5 | 4–7 |
| Quatre objets suivants | 0 | 0–2 | 4–10 | 4–12 |
| Documentation et transfert | 0 | 1–2 | 1–2 | 2–4 |
| **Total** | **6–9** | **12–24** | **14–32** | **32–65** |

**Équipe conseillée :** 1 architecte à temps partiel, 1 tech lead et **1 data engineer**. Prévoir un renfort ponctuel pour la connexion SAP si elle nécessite une expertise SAP spécifique. Le chiffrage reste **32–65 j.p.**, ou **environ 36–75 j.p.** avec provision.

### Scénario 2 — Socle industrialisé et 20 objets SAP

| Lot du socle | Architecte | Tech lead | Data engineers | Total |
|---|---:|---:|---:|---:|
| Cadrage et conception | 4–6 | 3–4 | 1–2 | 8–12 |
| Technical foundation | 4–6 | 6–10 | 5–9 | 15–25 |
| Framework de métadonnées | 3–5 | 6–9 | 6–11 | 15–25 |
| Moteur d'orchestration | 3–5 | 8–12 | 9–18 | 20–35 |
| Framework d'ingestion Bronze | 2–3 | 5–8 | 8–14 | 15–25 |
| Intégration SAP S/4 | 1–2 | 2–5 | 7–13 | 10–20 |
| Tests et mise en exploitation | 1 | 2–4 | 9–15 | 12–20 |
| **Total socle** | **18–28** | **32–52** | **45–82** | **95–162** |
| Déploiement de 20 objets standards | 0 | 10–20 | 50–100 | 60–120 |
| **Total projet** | **18–28** | **42–72** | **95–182** | **155–282** |

**Équipe conseillée :** 1 architecte à temps partiel (surtout au cadrage et sur les choix structurants), 1 tech lead responsable du framework et des revues, et **2 data engineers**. Pendant le socle, l'un se concentre sur l'orchestration et les métadonnées, l'autre sur l'extraction SAP et l'ingestion Bronze ; ensuite, ils déploient les objets en parallèle. Un troisième data engineer n'est justifié que pour raccourcir le calendrier avec de nombreux objets indépendants et un accès SAP déjà stabilisé.

**Ordre de grandeur du calendrier :** 16–24 semaines pour le scénario à 20 objets avec cette équipe, sous réserve des disponibilités, validations de sécurité et accès SAP. L'effort projet reste **155–282 j.p.**, ou **environ 171–324 j.p.** avec une provision de 10–15 %. La provision ne correspond pas à une personne supplémentaire dédiée.


### Tableau de chiffrage par profil — Scénario industrialisé (20 objets)

| Profil | Responsabilité principale | Socle | 20 objets | Total |
|---|---|---:|---:|---:|
| Architecte | Architecture cible, sécurité, décisions d'intégration SAP et revues | 18–28 j.p. | 0 | **18–28 j.p.** |
| Tech lead | Conception détaillée du framework, CI/CD, supervision, revues et coordination technique | 32–52 j.p. | 10–20 j.p. | **42–72 j.p.** |
| Data engineer 1 | Orchestration, métadonnées, contrôles et première moitié des objets | 25–45 j.p. | 25–50 j.p. | **50–95 j.p.** |
| Data engineer 2 | Connectivité SAP, ingestion Bronze, tests et seconde moitié des objets | 20–37 j.p. | 25–50 j.p. | **45–87 j.p.** |
| **Total** | | **95–162 j.p.** | **60–120 j.p.** | **155–282 j.p.** |

La répartition entre les deux data engineers est indicative : les deux doivent pouvoir intervenir sur l'ensemble du framework. Pour obtenir un **budget en euros**, multiplier les jours de chaque profil par son TJM contractuel, puis ajouter la provision de 10–15 % si elle est retenue. Aucun TJM n'est supposé dans cet abaque.
