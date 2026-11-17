% Diet Suggestion System Based on Disease

% Diet Recommendations

diet(diabetes,
     'Choose balanced meals, high-fiber foods, and limit added sugar').

diet(hypertension,
     'Reduce salt intake and choose fruits and vegetables').

diet(anemia,
     'Include iron-rich foods such as beans, leafy greens, and fortified cereals').

diet(obesity,
     'Choose balanced meals with vegetables, whole grains, and appropriate portions').

diet(heart_disease,
     'Choose fruits, vegetables, whole grains, and limit saturated fats').

% Rule to suggest diet based on disease

suggest_diet(Disease, Recommendation) :-
    diet(Disease, Recommendation).