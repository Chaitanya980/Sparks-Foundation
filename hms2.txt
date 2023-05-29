% Facts defining symptoms and conditions

% Symptoms
symptom(fever).
symptom(cough).
symptom(headache).
symptom(sore_throat).
symptom(rash).
symptom(chest_pain).
symptom(fatigue).
symptom(shortness_of_breath).
symptom(dizziness).
symptom(nausea).

% Conditions
condition(common_cold, [cough, headache, sore_throat]).
condition(influenza, [fever, cough, headache, fatigue]).
condition(measles, [fever, rash]).
condition(strep_throat, [sore_throat, fever]).
condition(pneumonia, [fever, cough, chest_pain, shortness_of_breath, fatigue]).
condition(angina, [chest_pain, shortness_of_breath, dizziness, nausea]).

% Rules for diagnosis
diagnose(common_cold) :-
  condition(common_cold, Symptoms),
  has_symptoms(Symptoms).

diagnose(influenza) :-
  condition(influenza, Symptoms),
  has_symptoms(Symptoms).

diagnose(measles) :-
  condition(measles, Symptoms),
  has_symptoms(Symptoms).

diagnose(strep_throat) :-
  condition(strep_throat, Symptoms),
  has_symptoms(Symptoms).

diagnose(pneumonia) :-
  condition(pneumonia, Symptoms),
  has_symptoms(Symptoms).

diagnose(angina) :-
  condition(angina, Symptoms),
  has_symptoms(Symptoms).

% Helper rule to check if the user has specific symptoms
has_symptoms([]).
has_symptoms([Symptom | Rest]) :-
  write('Do you have '), write(Symptom), write('? (yes/no) '),
  read(Response),
  (Response == yes ; Response == y),
  has_symptoms(Rest).

% Main entry point for diagnosis
start_diagnosis :-
  write('Welcome to the medical diagnosis expert system.'), nl,
  write('Please answer the following questions with yes/no.'), nl,
  diagnose(Condition),
  write('Based on your symptoms, you may have '), write(Condition), write('.'), nl.
