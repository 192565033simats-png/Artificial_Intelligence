% Weather Prediction System
% Weather Facts
weather(cloudy).
weather(windy).
% Rules for Weather Prediction
predict(rain) :-
    weather(rainy).
predict(rain) :-
    weather(cloudy),
    weather(windy).
predict(no_rain) :-
    weather(sunny),
    \+ weather(cloudy),
    \+ weather(rainy).
% Display Prediction
show_prediction :-
    predict(Result),
    write('Weather Prediction: '),
    write(Result),
    nl.