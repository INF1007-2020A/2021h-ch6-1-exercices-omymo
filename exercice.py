#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
from collections import Counter


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        while len(values) < 5:
            values.append(input("saisir une valeur:\n"))

    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = ()
        words1 = input("saisir un mot:\n")
        words2 = input("saisir un autre mot:\n")
        words = (words1, words2)
        if sorted(words1) == sorted(words2):
            return True

    return False


def contains_doubles(items: list) -> bool:
    # return len(set(items)) != len(items)
    for i in items:
        if items.count(i) > 1:
            return True
        else:
            return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict()
    for key, value in student_grades.items():
        average = sum(value) / len(value)
        if len(best_student) == 0 or list(best_student.values())[0] < average:
            best_student = {key: average}
    return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequency: {letter: sentence.count(letter) for letter in sentence}
    sorted_keys = sorted(frequency, reverse=True, key=frequency.__getitem__)
    for key in sorted_keys:
        if frequency[key] > 5:
            print(f"le caractere {key} revient {frequency[key]} fois.")

    return frequency


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("quel est le nom de votre recette\n")
    ingredient = input("entrer la liste d'ingredients? separer les ingredients par une, \n").split(",")
    return {name: ingredient}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("quel est le nom de votre recette\n")
    if name not in ingredients:
        print("cette recette n'existe pas")
    else:
        print(ingredients[name])


def main() -> None:
    # print(f"On essaie d'ordonner les valeurs...")
    #  print(order())

    # print(f"On vérifie les anagrammes...")
    # print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    # print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
