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
| **Socle industrialisé** | **Avant déploiement des objets SAP** | **95–157 j.p.** |

**Déploiement par objet SAP :** 3–6 j.p. pour un objet standard ; 7–12 j.p. si l'extraction nécessite une logique particulière.

**Exemple pour 20 objets standards : 155–277 j.p.** Avec une provision de 10–15 % : **environ 170–320 j.p.**

## Points à valider avant engagement

- Disponibilité du mécanisme d'extraction SAP et responsabilité des éventuels développements côté SAP.
- Accès réseau et sécurité entre Fabric et SAP.
- Clés, colonnes d'incrément, gestion des suppressions et volumétrie par objet.
- Performance du chargement initial et fenêtres d'extraction autorisées.

Un **objet pilote** permet de mesurer ces facteurs avant de figer le coût par objet. Les deux scénarios s'arrêtent à **Bronze** : Silver, Gold, modèles sémantiques et licences/capacité Fabric sont hors périmètre.
