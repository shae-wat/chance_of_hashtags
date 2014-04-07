%hw3

load hw3_netflix.mat

%alt_min.m contains learning function

%=======Crossvalidation=======


trR1=trR;
trR1(cvSet(1,:))=0;
 %Now you train using trR1 data and after you find out the solution matrix U1 and M1, calculate RMSE using:
[U1,M1] = alt_min(trR1);
PredictedRatings1 = U1*M1';
RMSE1 = sqrt(sum(sum((PredictedRatings1(cvSet(1,:))-trR(cvSet(1,:))).^2))/length(cvSet(1,:)))

%=======Plot RMSE=======

%=======Results=======

%optimal lambda

%problems with lambda=0

%RMSE for optimal lambda
