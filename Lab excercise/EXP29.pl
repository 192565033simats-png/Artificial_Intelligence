
% Medical Diagnosis System

% Symptoms
symptom(fever).
symptom(cough).
symptom(sore_throat).
symptom(runny_nose).
symptom(headache).

% Diagnosis Rules
diagnosis(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(headache).

diagnosis(common_cold) :-
    symptom(cough),
    symptom(runny_nose),
    symptom(sore_throat).

diagnosis(throat_infection) :-
    symptom(fever),
    symptom(sore_throat).

% Display Diagnosis
show_diagnosis :-
    findall(Disease, diagnosis(Disease), Diseases),
    display_result(Diseases).

display_result([]) :-
    write('No matching diagnosis found.'), nl.

display_result([H|T]) :-
    write('Possible diagnosis: '),
    write(H), nl,
    display_result(T).