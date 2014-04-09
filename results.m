%=======Results=======
load hw3_netflix.mat
warning('off');

%optimal lambda from cross validation
optimal_lambda = 1;

%*****problems with lambda=0 == RMSE is NaN

%RMSE for optimal lambda

[U,M] = alt_min(trR, optimal_lambda);
PredictedRatings = U*M';
rsme_optimal = sqrt(sum(sum((PredictedRatings(testIdx)-Ratings(testIdx)).^2))/length(testIdx))

%optimal lambda's rmse = 1.0811
