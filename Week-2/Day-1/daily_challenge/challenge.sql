-- ============================
-- Création de la table actors
-- ============================
CREATE TABLE actors (
    id INT PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL
);

-- ============================
-- Exemple de données (facultatif)
-- ============================
INSERT INTO actors (id, firstname, lastname) VALUES
(1, 'Tom', 'Hanks'),
(2, 'Meryl', 'Streep'),
(3, 'Denzel', 'Washington');

-- ============================
-- 1. Compter combien d'acteurs sont dans la table
-- ============================
SELECT COUNT(*) AS total_actors FROM actors;

-- ============================
-- 2. Essayer d'ajouter un acteur avec des champs vides
-- ============================

-- Exemple 1 : Champ firstname vide (chaîne vide, pas NULL)
INSERT INTO actors (id, firstname, lastname)
VALUES (4, '', 'Smith');
-- Résultat : l'insertion réussira (chaine vide acceptée).

-- Exemple 2 : Champ lastname NULL (devrait échouer à cause du NOT NULL)
INSERT INTO actors (id, firstname, lastname)
VALUES (5, 'Tom', NULL);
-- Résultat attendu : Erreur !
-- ERROR: null value in column "lastname" violates not-null constraint

-- ============================
-- Vérifier le contenu de la table
-- ============================
SELECT * FROM actors;
